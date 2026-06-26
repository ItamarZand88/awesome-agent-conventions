<!-- source: eloc-control-panel — https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/techContext.md -->
# ELOC Control Panel - Technical Context

## Technology Stack

### Platform & Language
| Component | Technology |
|-----------|------------|
| Platform | Android |
| Primary Language | Kotlin |
| Legacy Code | Java (in `old/` package) |
| Min SDK | 21 (Android 5.0 Lollipop) |
| Target SDK | 35 (Android 15) |
| Compile SDK | 35 |

### Build System
- **Gradle** with Kotlin DSL
- **Android Gradle Plugin**
- **View Binding** enabled
- **BuildConfig** enabled
- **ProGuard/R8** for release builds (minify + shrink resources)

### Key Dependencies

#### Android/AndroidX
```gradle
androidx.appcompat:appcompat:1.7.0
androidx.recyclerview:recyclerview:1.4.0
androidx.constraintlayout:constraintlayout:2.2.1
androidx.lifecycle:lifecycle-runtime-ktx:2.8.7
androidx.lifecycle:lifecycle-viewmodel-ktx:2.8.7
androidx.swiperefreshlayout:swiperefreshlayout:1.2.0-beta01
androidx.work:work-runtime:2.10.0
androidx.credentials:credentials:1.5.0
androidx.preference:preference-ktx:1.2.1
androidx.activity:activity-ktx:1.10.1
```

#### Google Services
```gradle
com.google.android.gms:play-services-maps:19.2.0
com.google.android.gms:play-services-auth:21.3.0
com.google.android.gms:play-services-base:18.7.0
com.google.maps.android:android-maps-utils:3.8.0
com.google.android.material:material:1.12.0
```

#### Firebase (BOM 32.6.0 - supports API 21)
```gradle
com.google.firebase:firebase-auth
com.google.firebase:firebase-storage
com.google.firebase:firebase-firestore
```

#### Other
```gradle
com.android.volley:volley:1.2.1  // HTTP requests
org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1
com.android.tools:desugar_jdk_libs:2.1.5  // Java 8+ API backport
```

## Development Setup

### Prerequisites
1. Android Studio (latest stable)
2. JDK 8 or higher
3. Android SDK with API 35
4. Google Services JSON file (`app/google-services.json`)
5. Google Maps API key (in `local.properties` or secrets)

### Building
```bash
# Debug build
./gradlew assembleDebug

# Or use the batch file
tomBuildDebug.bat
```

### Configuration Files
| File | Purpose |
|------|---------|
| `app/google-services.json` | Firebase configuration |
| `local.properties` | Local SDK path, API keys |
| `gradle.properties` | Gradle settings |

## Technical Constraints

### Bluetooth Limitations
- **Command Max Length**: 512 bytes per command
- **Protocol**: Bluetooth SPP (Serial Port Profile)
- **UUID**: `00001101-0000-1000-8000-00805F9B34FB`
- **Message Terminator**: EOT byte (0x04)
- **Required Permissions**:
  - `BLUETOOTH`, `BLUETOOTH_ADMIN` (SDK ≤ 30)
  - `BLUETOOTH_CONNECT`, `BLUETOOTH_SCAN` (SDK > 30)
  - `ASSOCIATE_COMPANION_DEVICES`

### Android Permissions Required
```xml
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
<uses-permission android:name="android.permission.BLUETOOTH_SCAN" />
<uses-permission android:name="android.permission.ASSOCIATE_COMPANION_DEVICES" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

### Firebase Constraints
- BOM version 32.6.0 for API 21 compatibility
- Firestore for document storage
- Firebase Storage for profile pictures
- Firebase Auth for user management

## Code Organization

### Package Structure
```
de.eloc.eloc_control_panel/
├── App.kt                    # Application class
├── activities/
│   ├── ActivityExtensions.kt
│   └── themable/             # All activities extend ThemableActivity
│       ├── ThemableActivity.kt
│       ├── HomeActivity.kt
│       ├── DeviceActivity.kt
│       ├── DeviceSettingsActivity.kt
│       ├── editors/          # Settings editors
│       └── media/            # Profile/media activities
├── data/
│   ├── *.kt                  # Data classes (enums, models)
│   ├── adapters/             # RecyclerView adapters
│   ├── helpers/              # Utility classes
│   │   ├── BluetoothHelper.kt
│   │   ├── firebase/         # Firebase helpers
│   │   └── ...
│   ├── util/
│   │   └── Preferences.kt    # SharedPreferences wrapper
│   └── viewholders/
├── dialogs/
├── driver/                   # Device communication
│   ├── DeviceDriver.kt       # Main driver (singleton)
│   ├── Microphone.kt
│   ├── Battery.kt
│   └── ... (component classes)
├── interfaces/               # Callbacks and listeners
├── old/                      # Legacy Java code
├── receivers/                # Broadcast receivers
├── services/                 # Background services
└── widgets/                  # Custom views
```

### Naming Conventions
- Activities: `*Activity.kt` → `activity_*.xml`
- Layouts: `layout_*.xml` for reusable components
- Drawables: lowercase with underscores
- Strings: `strings.xml` for user-facing, `code_strings.xml` for technical

## Tool Usage Patterns

### Android Studio
- View Binding for UI access
- Layout Inspector for debugging
- Logcat with tag filtering

### Testing
- Manual testing on physical devices
- Bluetooth testing requires real ELOC hardware

### Version Control
- Git with GitHub remote
- Feature branches, merge to main

## ELOC Firmware Communication

### JSON Command Format
Commands sent to ELOC device:
```json
{
  "id": 123,
  "cmd": "getStatus"
}
```

### Response Format
Responses from device (EOT-terminated):
```json
{
  "id": 123,
  "cmd": "getStatus",
  "ecode": 0,
  "payload": {
    "session": { ... },
    "device": { ... },
    "battery": { ... }
  }
}
```

### Key Commands
| Command | Description |
|---------|-------------|
| `getStatus` | Get device status (battery, recording, etc.) |
| `getConfig` | Get device configuration |
| `setConfig` | Update configuration setting |
| `setTime` | Sync device time |
| `setRecordMode` | Start/stop recording |
