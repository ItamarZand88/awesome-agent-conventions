<!-- source: eloc-control-panel — https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/productContext.md -->
# ELOC Control Panel - Product Context

## Why This Project Exists
ELOC (Electronic Logger of Calls) devices are acoustic monitoring units used for wildlife conservation, particularly for detecting elephant calls and other sounds in forest environments. Field researchers need a mobile interface to:
- Deploy and configure recording devices in remote locations
- Monitor device health (battery, storage) without physical access
- Start/stop recordings based on research schedules
- Track device locations across large forest areas

## Problems It Solves

### For Field Researchers
1. **Remote Configuration** - Configure microphone settings, recording schedules, and detection parameters without connecting to a computer
2. **Quick Deployment** - Set up multiple devices efficiently in the field
3. **Health Monitoring** - Check battery levels and SD card space before they become critical
4. **Location Tracking** - Know where all devices are deployed via map view

### For Conservation Teams
1. **Centralized Data** - Device status uploaded to Firebase for team visibility
2. **User Management** - Track which ranger configured which device
3. **Historical Data** - Access past configurations and status readings

## How It Should Work

### Typical User Flow
1. **Launch App** → Sign in with email/password or Google
2. **Home Screen** → See list of nearby ELOC devices via Bluetooth scan
3. **Connect to Device** → Select device, pair if needed, establish connection
4. **View Status** → See battery, SD card space, recording state, firmware version
5. **Configure Settings** → Modify microphone, detection, Bluetooth, and other settings
6. **Control Recording** → Start or stop recording sessions
7. **View on Map** → See device locations with status indicators

### Key User Interactions
- **Pull-to-refresh** - Update device status
- **Settings editor** - Modify individual parameters with validation
- **Command line** - Advanced users can send raw commands
- **Profile management** - Save/load device configuration profiles

## User Experience Goals

### Reliability
- Stable Bluetooth connections (recent fix for pairing race conditions)
- Clear error messages when connections fail
- Automatic reconnection handling

### Simplicity
- One-tap device connection
- Clear status indicators (battery, recording state)
- Intuitive settings organization

### Field-Friendly
- Works offline for local device control
- Large, easy-to-tap UI elements
- Portrait-only orientation for one-handed use

## Target Users
1. **Field Rangers** - Deploy and monitor devices in forest areas
2. **Researchers** - Configure detection parameters and analyze results
3. **Conservation Team Leads** - Track all devices across deployment area
