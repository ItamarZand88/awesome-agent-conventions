<!-- source: eloc-control-panel — https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/progress.md -->
# ELOC Control Panel - Progress

## What Works

### Core Functionality ✅
- **Bluetooth Connection** - Connect to ELOC devices via BT SPP
- **Device Pairing** - Proper bonding flow with state management (recently fixed)
- **Status Reading** - Get battery, SD card, recording state, firmware info
- **Configuration Reading** - Get all device settings
- **Configuration Writing** - Update individual device settings
- **Recording Control** - Start/stop recording sessions
- **Time Sync** - Synchronize device clock with phone

### User Interface ✅
- **Home Screen** - Device list with Bluetooth scanning
- **Device Status** - Full status display with pull-to-refresh
- **Settings Editor** - Individual setting modification
- **Command Line** - Raw command interface for advanced users
- **Map View** - Google Maps integration for device locations

### Cloud Integration ✅
- **Firebase Auth** - Email/password and Google sign-in
- **Data Upload** - Status/config upload to Firestore
- **Profile Pictures** - Firebase Storage integration
- **Background Upload** - StatusUploadService for queued uploads

### User Accounts ✅
- Sign up with email/password
- Sign up with Google
- Sign in with email/password
- Sign in with Google
- User profile (picture, display name, ranger ID)
- Change email/password
- Delete account

## What's Left to Build

### Bug Fixes 🐛
| Issue | Status | Priority |
|-------|--------|----------|
| Bluetooth ON/OFF toggle not working | Not Started | Medium |
| Refresh only works after scroll | Not Started | Low |
| Google Maps crashes on some devices | Not Started | Medium |

### Features 📋
| Feature | Status | Priority |
|---------|--------|----------|
| Remaining recording time calculation | Not Started | Medium |
| Map auto-zoom to all markers | Not Started | Low |
| "App update required" message system | Not Started | Low |

### Technical Debt 🔧
| Item | Status | Priority |
|------|--------|----------|
| Fix view binding toolbar issue | Not Started | Low |
| Migrate Java code to Kotlin | Not Started | Low |

## Current Status

**Version**: 5.34 AppBeta (versionCode 55)

**Overall Health**: ✅ Stable
- Core functionality working
- Recent Bluetooth pairing fix resolved major connection issues
- Ready for field testing

## Known Issues

### Bluetooth Toggle
The Bluetooth ON/OFF button in settings doesn't work. This may be related to Android permission changes in newer API levels.

### Pull-to-Refresh Behavior
The swipe-to-refresh on the status page:
2. Sometimes it refreshes the svreen even though i am in the middle of the status page and not on top.

### Google Maps Crashes
Some devices experience crashes with Google Maps. Details in `maps.log`. May be device-specific or related to map utils version.

## Evolution of Project Decisions

### Bluetooth Connection Strategy
- **Initial**: Direct socket connection on device selection
- **Problem**: Race condition with pairing on unpaired devices
- **Current**: Bond state check → initiate bonding → wait → connect

### Firebase BOM Version
- **Current**: 32.6.0 (pinned for API 21 support)
- **Trade-off**: Newer Firebase features unavailable
- **Reason**: Support older Android devices in field use

### UI Architecture
- **Pattern**: Single Activity per screen, ThemableActivity base
- **Binding**: View Binding (modern approach)
- **Navigation**: Intent-based between activities

## Milestones

### Completed ✅
- [x] Initial app structure and UI
- [x] Bluetooth SPP connection
- [x] Device command protocol
- [x] Firebase authentication
- [x] Data upload service
- [x] Google Maps integration
- [x] User profile management
- [x] Bluetooth pairing fix (Jan 2026)
- [x] Memory Bank initialization (Feb 2026)
- [x] Database upload optimization (Feb 2026)
- [x] Google Sign-In implementation (Feb 2026)
- [x] Duty Cycle settings implementation (Feb 2026)
- [x] LoRa RSSI signal strength indicator (Feb 2026)
- [x] Map document: added batteryType and recordingState fields (Feb 2026)
- [x] Status document stale timestamp bug fix (Mar 2026)

### Upcoming 🎯
- [ ] Fix remaining bugs (BT toggle, refresh)
- [ ] Implement recording time calculation
- [ ] Kotlin migration for legacy code
- [ ] Performance testing with multiple devices
