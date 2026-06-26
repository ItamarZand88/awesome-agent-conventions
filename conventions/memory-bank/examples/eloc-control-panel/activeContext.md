<!-- source: eloc-control-panel — https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/activeContext.md -->
# ELOC Control Panel - Active Context

## Current Work Focus
Status Document Stale Timestamp Bug Fix - fixed `combinedStatusAndConfigTime` not being reset, causing status documents to overwrite existing ones instead of creating new ones.

## Recent Changes

### Status Document Stale Timestamp Bug Fix (March 2026)
**Issue**: When changing device recording mode on a different day than the initial status document was created, the Android app updated the existing Firestore document instead of creating a new one. The `capture_timestamp` stayed at the original date, while `upload_timestamp` was refreshed and session data was updated with the new state.

**Root Cause**: `combinedStatusAndConfigTime` in the `DeviceDriver` singleton was not being reset properly. If a `StatusWithConfig` save partially completed (status saved but config response never arrived due to disconnect/timeout), the timestamp was never cleared. Since `disconnect()` also didn't clear it, the stale timestamp persisted across connections. On the next save cycle, `saveLocal()` checked `if (combinedStatusAndConfigTime == null)` and found it NOT null, so it reused the old timestamp, generating a file with the same name as the previous one. Firestore's `document.set(data)` then overwrote the existing document.

**Fix** (two changes in `DeviceDriver.kt`):
1. **`getElocInformation()`**: Added `combinedStatusAndConfigTime = null` when `saveNextInfoResponse=true`, ensuring every new save cycle starts with a fresh timestamp
2. **`disconnect()`**: Added cleanup of all save-related state (`combinedStatusAndConfigTime`, `configSaved`, `statusSaved`, `cachedStatus`, `cachedConfig`, `infoType`) to prevent stale values from persisting across connections

**Verified via Firestore**: The document `status_2026-03-01-12-17-58-GMT+0700_e_ELOC_00244_r_edsteve2.json` was created on March 1 but updated on March 2 with March 2 device data (1m 30s uptime from device restart, new session ID, new recording state), confirming March 2 data was incorrectly saved with March 1's filename.

### Map Document New Fields (February 2026)
**Feature**: Added `batteryType` and `recordingState` fields to the Firestore map collection document (`eloc_app/uploads/map/map_{deviceName}.json`).

**Key Changes**:
1. `Session.kt` - Added `recordingStateString` property to store the raw recording state string from firmware (e.g., "recordOn_detectOn")
2. `DeviceDriver.kt` - Added parsing of `payload/session/recordingState/state` string in `parseStatus()` method
3. `DeviceDriver.kt` - Added `KEY_BATTERY_TYPE_MAP` ("batteryType") and `KEY_RECORDING_STATE_MAP` ("recordingState") constants
4. `DeviceDriver.kt` - Added both new fields to the map data JSON in `saveLocal()` method

**Technical Details**:
- `batteryType` (String): Sourced from `battery.type` which is already parsed from firmware status at `payload/battery/type`. Values: "LiPo" or "LiFePo"
- `recordingState` (String): Sourced from `session.recordingStateString` parsed from firmware status at `payload/session/recordingState/state`. Values: e.g., "recordOff_detectOff", "recordOn_detectOn", etc.
- Both values come from the `getStatus` firmware command response
- No changes needed to FirestoreHelper or FileSystemHelper since the map data flows through as raw JSON

### LoRa RSSI Signal Strength Indicator (February 2026)
**Feature**: Added LoRa signal strength indicator to the Device Status page, displaying signal quality when LoRa is enabled and connected.

**Key Changes**:
1. `LoraWan.kt` - Added `LoraSignalStrength` enum with 5 levels (Excellent, Good, Fair, Poor, VeryPoor) based on RSSI thresholds, plus new status properties: `joined`, `hasSignalInfo`, `rssi`, `snr`, and computed `signalStrength`
2. `DeviceDriver.kt` - Added LoRa status keys constants, updated `sanitize()` method to handle bracketed keys (`RSSI[dBm]`, `SNR[dB]`), added LoRa status parsing in `parseStatus()` method
3. `activity_device.xml` - Added LoRa signal container with RSSI icon and dBm value display below the "Communication" item
4. `DeviceActivity.kt` - Added `updateLoraSignalDisplay()` method that updates the UI based on LoRa status
5. `strings.xml` - Added string resources: `lora_signal`, `lora_signal_dbm`, `lora_not_joined`, `lora_no_signal`

**Technical Details**:
- LoRa RSSI thresholds: Excellent (> -90 dBm), Good (-90 to -110 dBm), Fair (-110 to -120 dBm), Poor (-120 to -130 dBm), VeryPoor (< -130 dBm)
- Uses existing RSSI drawable icons (rssi_0 through rssi_5)
- Container is hidden when LoRa is disabled
- Shows "Not Joined" when LoRa is enabled but not joined to network
- Shows "No Signal" when joined but no signal info available yet
- Shows dBm value and signal icon when valid signal is available

**JSON Status Data Parsed** (from `getStatus` response):
```json
"lora": {
    "enabled": true,
    "joined": true,
    "hasSignalInfo": true,
    "RSSI[dBm]": -85.5,
    "SNR[dB]": 7.2
}
```

### Duty Cycle Settings Implementation (February 2026)
**Feature**: Added duty cycle configuration settings to the ELOC Device Settings screen, allowing users to enable/disable duty cycling and configure sleep/awake durations.

**Key Changes**:
1. `DutyCycle.kt` - New driver component class with constants for JSON keys, min/max ranges, and default values
2. `DeviceDriver.kt` - Added `dutyCycle` property, parsing logic for duty cycle JSON config keys (`dutyCycle_enable`, `dutyCycle_sleep`, `dutyCycle_awake`)
3. `Command.kt` - Added duty cycle property cases (`setDutyCycleEnable`, `setDutyCycleSleep`, `setDutyCycleAwake`) to the set config command builder
4. `activity_device_settings.xml` - Added collapsible Duty Cycle section with enable toggle, sleep duration, and awake duration items
5. `DeviceSettingsActivity.kt` - Added duty cycle data binding, listeners (toggle + range editors), and section expand/collapse logic
6. `strings.xml` - Added string resources: `duty_cycle`, `sleep_duration`, `awake_duration`, `duty_cycle_sleep_duration`, `duty_cycle_awake_duration`

**Technical Details**:
- Sleep duration range: 10 - 86400 seconds (10s to 24h), default 300s
- Awake duration range: 10 - 86400 seconds (10s to 24h), default 1800s
- Uses RangeEditorActivity for duration settings with prettified time display
- Follows same pattern as LoraWan, Inference, and other existing settings sections

## Previous Changes

### Bluetooth Pairing Fix (January 2026)
**Issue**: Android phones experiencing connection failures and crashes when connecting to ELOC devices.

**Root Cause**: The app was attempting to establish a Bluetooth socket connection before waiting for the pairing/bonding process to complete, creating a race condition.

**Solution**: Implemented proper Bluetooth bonding state management in `DeviceDriver.kt`:
1. Check bonding state before attempting connection
2. Initiate bonding if device is unpaired
3. Wait for bonding completion via broadcast receiver
4. Only connect after successful bonding

**Key Changes**:
- Added `bondingInProgress` flag and pending callbacks
- Created `bondStateReceiver` broadcast receiver
- Modified `connect()` to check `device.bondState` first
- Added `registerBondStateReceiver()` and `proceedWithConnection()` helpers

See `BLUETOOTH_PAIRING_FIX.md` for full documentation.

### Database Upload Optimization (February 2026)
**Issue**: The app was uploading status and config data to Firestore too frequently, filling the database with unnecessary information.

**Previous Behavior**:
- When connecting to ANY ELOC → uploaded status + config to database
- When refreshing status page → uploaded status + config to database  
- When starting recording mode → uploaded status + config, then getStatus again

**Optimized Behavior**:
- **Connect to idle ELOC**: No database upload (just display in UI)
- **Connect to recording ELOC**: Upload status only (no config, no location update)
- **Start recording mode**: Upload status + config with new session ID and location
- **Refresh status page**: No database upload (just display in UI)

**Key Changes**:
1. `DeviceDriver.kt` - Removed automatic `getElocInformation()` call from `setRecordState()`
2. `DeviceActivity.kt` - Modified `onFirstLocationReceived()` to:
   - If device is recording: Call `getStatus()` for DB upload, then `getElocInformation(null, false)` for UI only
   - If device is NOT recording: Call `getElocInformation(location, false)` for UI only (no upload)
3. `DeviceActivity.kt` - Modified `setCommandCompletedCallback` to call `getElocInformation(location, true)` after starting recording mode (uploads to DB)

**Technical Details**:
- `saveNextInfoResponse` parameter in `getElocInformation()` controls DB uploads:
  - `true` = save/upload to Firestore
  - `false` = display in UI only, no upload
- `saveToDatabase` parameter in `getStatus()` controls DB uploads:
  - `true` (default) = save/upload status to Firestore
  - `false` = display in UI only, no upload

**Bug Fix (February 2026)**: Fixed issue where `getStatus` was not uploading when reconnecting to a recording device. The first `getStatus()` call in `showDeviceInfo()` (used just to check recording state) was consuming the upload slot, preventing the second `getStatus()` call in `onFirstLocationReceived()` from uploading. Solution: Added `saveToDatabase` parameter to `getStatus()` function.

### Google Sign-In Implementation (February 2026)
**Issue**: Google Sign-In option was planned but never implemented.

**Solution**: Implemented Google Sign-In using the modern Credential Manager API.

**Key Changes**:
1. `AuthHelper.kt` - Added `signInWithGoogle()`, `handleGoogleSignInResult()`, and `firebaseAuthWithGoogle()` methods
2. `activity_login.xml` - Added "Sign in with Google" button with Material Design styling
3. `activity_register.xml` - Added "Sign in with Google" button
4. `LoginActivity.kt` - Added Google Sign-In handler with `signInWithGoogle()` method
5. `RegisterActivity.kt` - Added Google Sign-In handler
6. `strings.xml` - Added `sign_in_with_google`, `google_sign_in_failed`, `google_sign_in_cancelled`, `web_client_id` strings

**Technical Details**:
- Uses `CredentialManager` API with `GetGoogleIdOption`
- Authenticates with Firebase using `GoogleAuthProvider.getCredential(idToken)`
- Google accounts are automatically verified (skip email verification flow)
- Web Client ID from Firebase: `773327231765-igglaupgt12mct4ii7kiil5ktda2nqfd.apps.googleusercontent.com`

**Configuration Required**:
- Debug SHA-1 fingerprint must be added to Firebase project settings
- SHA-1 for current debug keystore: `74:FD:1E:8A:FA:90:12:7F:4B:D8:C9:06:F0:35:83:CE:AB:E1:BA:04`

## Next Steps

Based on `TODO.md`, the following items need attention:

### Bugs
- [ ] Bluetooth ON/OFF button doesn't work in settings

### Features - Status Page
- [ ] Fix swipe-down refresh (refreshes SD card but not other values)
- [ ] Fix refresh only possible after scrolled down first
- [ ] Show remaining recording time calculation

### Features - Settings Page  
- [ ] Turn ON/OFF Bluetooth toggle not working

### Features - Map
- [ ] Auto-zoom to all ELOC markers (low priority)

### Technical Debt
- [ ] Fix view binding issue with toolbar
- [ ] Investigate Google Maps crashes on some devices (see `maps.log`)
- [ ] Migrate remaining Java code to Kotlin

## Active Decisions and Considerations

### Microphone Type Configuration
The app supports multiple microphone types that must match the ELOC hardware:
- ICS-43434
- SPH0645
- IM69D130
- ICS-43432
- INMP441 (various gain options)

The `MicrophoneType.kt` enum defines these, and settings must be coordinated with firmware.

### Firebase BOM Version
Keeping Firebase BOM at 32.6.0 to maintain API 21 (Android 5.0) support. Do not upgrade without verifying compatibility.

### Portrait-Only Orientation
All activities are locked to portrait orientation for field usability.

## Important Patterns and Preferences

### Error Handling
- Use try-catch with empty catch blocks for non-critical operations
- Log errors via `Logger.kt` with traffic direction indicators
- Show user-friendly error messages via callbacks

### Bluetooth Communication
- Always check `bluetoothSocket?.isConnected` before operations
- Use 15-second timeout for command responses
- EOT byte (0x04) terminates all messages

### State Management
- `DeviceDriver` singleton holds all device state
- UI observes via listener callbacks
- Disconnect clears all state and callbacks

## Learnings and Project Insights

### Bluetooth Pairing
- Android requires BOND_BONDED state before socket connection
- Bonding can fail silently - must handle BOND_NONE after BOND_BONDING
- Some Android ROMs (MIUI) need higher `maxSdkVersion` for legacy permissions

### ELOC Communication
- 512-byte command limit is hardware constraint
- JSON parsing must handle missing/malformed fields gracefully
- Device sends greeting JSON on connect - wait for it before commands

### User Experience
- Field conditions require simple, large UI elements
- Offline functionality is critical (no cellular in forests)
- Battery and SD card status are most-viewed information
