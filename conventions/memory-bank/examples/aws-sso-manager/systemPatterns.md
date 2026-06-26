<!-- source: aws-sso-manager — https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/systemPatterns.md -->
# System Patterns: AWS SSO Manager

## Architecture Overview

### Application Structure
```
┌─────────────────────────────────────────────────────────┐
│                    Electron Main Process                 │
│  - Window Management                                     │
│  - IPC Communication                                     │
│  - AWS SDK Integration                                   │
│  - Secure Storage (electron-store)                      │
└─────────────────────────────────────────────────────────┘
                           │
                    IPC Bridge (preload.js)
                           │
┌─────────────────────────────────────────────────────────┐
│                  React Renderer Process                  │
│  - UI Components (shadcn/ui)                            │
│  - State Management (Context API)                       │
│  - Routing (React Router)                               │
│  - Data Fetching (TanStack Query)                      │
└─────────────────────────────────────────────────────────┘
```

### Key Design Patterns

## 1. Context-Based State Management
The application uses React Context API for global state management:

- **SsoContext**: Manages authentication state, session info, and SSO operations
- **ElectronContext**: Provides access to Electron IPC methods
- **ThemeContext**: Handles dark/light mode preferences

## 2. Component Architecture

### Page Components
- `Login.tsx` - SSO authentication flow
- `Accounts.tsx` - Main account listing and management
- `Splash.tsx` - Loading/initialization screen
- `Callback.tsx` - OAuth callback handler

### Feature Components
- `AccountCard.tsx` - Individual account display (deprecated in favor of AccountItem)
- `AccountItem.tsx` - Modern account display with expandable roles
- `RoleItem.tsx` - **NEW**: Individual role display for Quick Access tab
- `RoleSelector.tsx` - Role selection interface
- `QuickAccess.tsx` - Quick role switching
- `Terminal.tsx` - Integrated terminal for AWS CLI
- `SettingsForm.tsx` - Application configuration with kubectl context display
- `KubernetesClustersDialog.tsx` - EKS cluster management with auto-context saving
- `BuyMeCoffeeButton.tsx` - Professional donation support component
- `SessionTimer.tsx` - **ENHANCED**: Professional session timer with HH:MM:SS format

### UI Components
Leveraging shadcn/ui for consistent design:
- Pre-built, customizable components
- Radix UI primitives for accessibility
- Tailwind CSS for styling
- **NEW: Portal component for proper modal rendering**
- **NEW: ModernToaster for toast notifications**
- **NEW: Footer component with branding**

## 3. Data Flow Patterns

### Authentication Flow
```
User Action → React Component → Electron IPC → AWS SDK → SSO Service
                    ↓                              ↓
              Update Context ← IPC Response ← Credentials
```

### Settings Management
- Persistent storage using `electron-store`
- Cached in memory to reduce disk I/O
- Settings include: SSO config, favorites, quick access roles, **kubectl context**
- **NEW**: Automatic kubectl context tracking and updates
- **NEW**: Real-time context display in settings UI

## 4. Security Patterns

### Credential Handling
- No credentials stored in renderer process
- All AWS operations in main process
- Secure IPC communication
- Session tokens with expiration tracking

### Storage Security
- System keychain integration via electron-store
- Encrypted storage for sensitive data
- No plain text credential storage

## 5. Error Handling Patterns

### Graceful Degradation
- Session expiration → Redirect to login
- API failures → User-friendly error messages
- Network issues → Retry mechanisms

### User Feedback
- Toast notifications for operations
- Loading states for async operations
- Progress modals for long-running tasks

## 6. Performance Patterns

### Lazy Loading
- Route-based code splitting
- Component lazy loading
- On-demand AWS SDK client creation

### Caching Strategy
- Settings cached in memory
- Account list refresh on demand
- Session state persistence

## 7. Communication Patterns

### IPC Channels
Main process exposes these channels:
- `aws-sso:*` - SSO operations (including kubectl context setting)
- `ecr:*` - ECR operations
- `codeartifact:*` - CodeArtifact operations
- `settings:*` - Settings management (including kubectl context storage)
- `open:*` - External URL/file operations
- `eks:*` - EKS cluster operations
- `kubectl:*` - kubectl configuration operations
- **NEW**: Enhanced kubectl context management through existing channels

### Event-Driven Updates
- Session timer updates
- Authentication state changes
- Settings modifications

## Component Relationships

### Hierarchical Structure
```
App
├── Router
│   ├── Login Page
│   ├── Accounts Page
│   │   ├── Header
│   │   ├── SearchBar
│   │   ├── AccountsList
│   │   │   └── AccountCard[]
│   │   └── Terminal
│   └── Settings Dialog
└── Contexts (SSO, Electron, Theme)
```

### Data Dependencies
- Components consume contexts for state
- Pages orchestrate component interactions
- Shared hooks for common operations

## 8. Professional Design System (v2.0.0)

### Professional Color Palette
- Primary: Indigo (#4F46E5) - trustworthy and professional
- Secondary: Light Indigo (#6366F1) - complementary accent
- Success: Emerald (#059669) - muted green for positive states
- Warning: Amber (#D97706) - less bright than original
- Error: Red (#DC2626) - standard error color

### Subtle Glass Effects
- Increased opacity (0.95 vs 0.8) for better readability
- Reduced blur effects (8px vs 16px)
- Professional borders and shadows
- Enterprise-suitable transparency levels

### Conservative Animation Patterns
- Subtle transitions (0.2s max duration)
- Simple hover effects (translateY(-1px))
- No pulse or glow animations
- Professional loading states

### Typography & Spacing
- Better contrast ratios for accessibility
- Consistent font weights and hierarchy
- Professional spacing system
- Clean, readable interface

### Component Styling
```css
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
}

.btn-primary {
  background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
}
```

## Technology Choices Rationale

1. **Electron**: Cross-platform desktop support with native OS integration
2. **React**: Component-based UI with strong ecosystem
3. **TypeScript**: Type safety and better developer experience
4. **TanStack Query**: Efficient data fetching and caching
5. **shadcn/ui**: Modern, accessible UI components
6. **Tailwind CSS**: Utility-first styling approach
7. **Vite**: Fast development and optimized builds
8. **@aws-sdk/client-eks**: Native EKS integration for cluster management
