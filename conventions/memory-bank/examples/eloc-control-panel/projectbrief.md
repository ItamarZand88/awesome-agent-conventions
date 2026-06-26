<!-- source: eloc-control-panel — https://raw.githubusercontent.com/EDsteve/ELOC-Control-Panel/main/memory-bank/projectbrief.md -->
# ELOC Control Panel - Project Brief

## Project Overview
The ELOC Control Panel is an Android application designed to connect to and control ELOC (Electronic Logger of Calls) recording devices via Bluetooth. The app serves as the primary interface for managing wildlife acoustic monitoring devices used in conservation efforts.

## Core Requirements

### Primary Functions
1. **Bluetooth Connectivity** - Connect to ELOC devices (ESP32-based) via Bluetooth Serial Port Profile (SPP)
2. **Device Configuration** - Configure ELOC device settings (microphone, recording, detection, etc.)
3. **Recording Control** - Start/stop recording sessions on connected ELOC devices
4. **Status Monitoring** - View real-time device status (battery, SD card, recording state)
5. **Data Upload** - Upload device status and configuration data to Firebase cloud
6. **Map Integration** - Display ELOC device locations on Google Maps

### Target Devices
- **ELOC 3.0 and up** - Primary target (app ID: `de.eloc.eloc_control_panel_2`)
- **ELOC 2.7** - Legacy support via separate app

### Platform
- **OS**: Android (minSdk 21, targetSdk 35)
- **Language**: Kotlin (with some legacy Java code)

## Project Goals
1. Provide reliable Bluetooth communication with ELOC devices
2. Enable field researchers to configure and monitor recording devices
3. Track device locations and status via cloud integration
4. Support user authentication for data management

## Key Constraints
- Bluetooth command length limited to 512 bytes
- Must support Android 5.0+ (API 21+)
- Firebase integration for authentication and data storage
- Google Maps API for location features

## Firmware Reference
The ELOC firmware is developed separately and located at:
`C:\Development\Firmware\ELOC-3.0\eloc610LowPowerPartition`

## Repository
- GitHub: https://github.com/EDsteve/ELOC-Control-Panel
