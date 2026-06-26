<!-- source: eloc-control-panel — https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/systemPatterns.md -->
# ELOC Control Panel - System Patterns

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Android App                               │
├─────────────────────────────────────────────────────────────────┤
│  Activities (UI Layer)                                          │
│  ├── ThemableActivity (base class)                              │
│  ├── HomeActivity (device list + map)                           │
│  ├── DeviceActivity (device status)                             │
│  ├── DeviceSettingsActivity (configuration)                     │
│  └── Various editors and account activities                     │
├─────────────────────────────────────────────────────────────────┤
│  Driver Layer (Business Logic)                                  │
│  ├── DeviceDriver (singleton - BT connection + commands)        │
│  ├── Microphone, Battery, SdCard, etc. (component settings)     │
│  └── Command processing + JSON parsing                          │
├─────────────────────────────────────────────────────────────────┤
│  Data Layer                                                     │
│  ├── Helpers (Bluetooth, Firebase, Location, etc.)              │
│  ├── Data classes (ElocDeviceInfo, GpsData, etc.)               │
│  └── Preferences (local storage)                                │
├─────────────────────────────────────────────────────────────────┤
│  Services                                                       │
│  ├── StatusUploadService (background Firebase uploads)          │
│  └── SerialService (legacy)                                     │
└─────────────────────────────────────────────────────────────────┘
           │                              │
           ▼                              ▼
┌──────────────────┐          ┌──────────────────────┐
│   ELOC Device    │          │      Firebase        │
│   (ESP32 BT)     │          │  Auth/Store/Storage  │
└──────────────────┘          └──────────────────────┘
```

## Key Design Patterns

### 1. Singleton DeviceDriver
The `DeviceDriver` is an `object` (Kotlin singleton) that:
- Manages single Bluetooth connection to ELOC device
- Queues and processes commands sequentially
- Parses JSON responses and updates component states
- Notifies listeners of connection/command changes

```kotlin
object DeviceDriver {
    val microphone = Microphone()
    val battery = Battery()
    val sdCard = SdCard()
    // ... other components
    
    fun connect(deviceAddress: String, callback, onError)
    fun disconnect()
    fun processCommandQueue(command: Command?)
}
```

### 2. Command Queue Pattern
Commands are queued and processed sequentially with timeouts:
```kotlin
processCommandQueue(Command) → commandProcessor() → write to BT → wait for response
```

### 3. Listener/Callback Pattern
Multiple listener maps for loose coupling:
- `connectionChangedListeners` - UI updates on connect/disconnect
- `onSetCommandCompletedListeners` - Handle SET command responses
- `onGetCommandCompletedListeners` - Handle GET command responses

### 4. Component-Based Configuration
Device settings are organized into component objects:
- `Microphone` - sample rate, channel, type, volume
- `Battery` - level, voltage, type, update intervals
- `SdCard` - size, free space
- `General` - node name, file header, location
- `Inference` - AI detection settings
- `Intruder` - intrusion detection settings
- `Logs` - logging configuration
- `BtConfig` - Bluetooth behavior settings

### 5. JSON Path Parsing
Configuration and status use nested JSON with path-based extraction:
```kotlin
val path = "payload/microphone/MicSampleRate"
val value = JsonHelper.getJSONNumberAttribute(path, jsonObject)
```

## Critical Implementation Paths

### Bluetooth Connection Flow
```
1. User selects device
2. Check bond state (BONDED, BONDING, NONE)
3. If not bonded → initiate bonding, wait for completion
4. Create RFCOMM socket
5. Connect socket
6. Start listening thread
7. Wait for greeting message
8. Connection active
```

### Command Communication Flow
```
1. Create Command object with callback
2. Add to pendingCommands queue
3. Executor thread writes command to BT socket
4. Listener thread reads response (EOT-terminated JSON)
5. Parse JSON, update component states
6. Invoke command callback
7. Notify listeners
```

### Data Upload Flow
```
1. Get status/config from device
2. Cache JSON responses
3. Save to local files (FileSystemHelper)
4. StatusUploadService reads files
5. Upload to Firebase Firestore
6. Delete local files on success
```

## Component Relationships

```
DeviceDriver (singleton)
    │
    ├── BluetoothSocket (connection)
    │
    ├── Component Objects (state)
    │   ├── Microphone
    │   ├── Battery
    │   ├── SdCard
    │   ├── General
    │   ├── Session
    │   ├── Inference
    │   ├── Intruder
    │   ├── Logs
    │   ├── BtConfig
    │   ├── Cpu
    │   ├── LoraWan (config + status with signal strength)
    │   └── DutyCycle
    │
    ├── Command Queue (pendingCommands)
    │
    └── Listener Maps
        ├── connectionChangedListeners
        ├── onSetCommandCompletedListeners
        └── onGetCommandCompletedListeners
```

## Key Files by Function

| Function | Files |
|----------|-------|
| BT Connection | `DeviceDriver.kt`, `BluetoothHelper.kt` |
| UI Base | `ThemableActivity.kt`, `ActivityExtensions.kt` |
| Device Status | `DeviceActivity.kt`, `layout_eloc_info.xml` |
| Settings | `DeviceSettingsActivity.kt`, `*EditorActivity.kt` |
| Map | `MapActivity.kt`, `LocationHelper.kt` |
| Firebase | `AuthHelper.kt`, `FirestoreHelper.kt`, `StorageHelper.kt` |
| Data Upload | `StatusUploadService.kt`, `FileSystemHelper.kt` |
