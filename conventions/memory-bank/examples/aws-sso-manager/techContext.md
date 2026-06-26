<!-- source: aws-sso-manager — https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/techContext.md -->
# Tech Context: AWS SSO Manager

## Technology Stack

### Core Technologies
- **Electron** v35.1.2 - Desktop application framework
- **React** v18.3.1 - UI library
- **TypeScript** v5.5.3 - Type-safe JavaScript
- **Vite** v5.4.1 - Build tool and dev server

### AWS Integration
- **@aws-sdk/client-sso** - SSO operations
- **@aws-sdk/client-sso-oidc** - OIDC authentication
- **@aws-sdk/client-ecr** - ECR integration
- **@aws-sdk/client-organizations** - Organization info
- **@aws-sdk/credential-provider-sso** - Credential management
- **@aws-sdk/client-eks** v3.777.0 - EKS cluster management

### UI Framework
- **shadcn/ui** - Component library built on:
  - Radix UI - Unstyled, accessible components
  - Tailwind CSS v3.4.11 - Utility-first CSS
  - class-variance-authority - Component variants
  - tailwind-merge - Class conflict resolution

### State & Data Management
- **TanStack Query** v5.71.3 - Server state management
- **React Context API** - Client state management
- **electron-store** v10.0.1 - Persistent storage
- **React Hook Form** v7.53.0 - Form management
- **Zod** v3.23.8 - Schema validation

### Routing & Navigation
- **React Router** v6.26.2 - Client-side routing
- **cmdk** v1.1.1 - Command palette functionality

### Development Tools
- **Concurrently** - Run multiple processes
- **Nodemon** - Auto-restart on changes
- **ESLint** - Code linting
- **Jest** & **Testing Library** - Testing

## Development Setup

### Prerequisites
- Node.js 18+ (for modern JavaScript features)
- npm or yarn package manager
- AWS CLI v2 (optional, for some features)
- Docker (for ECR features)
- kubectl (optional, for Kubernetes features)

### Environment Setup
```bash
# Clone repository
git clone https://github.com/SensiAI/aws-sso-manager.git
cd aws-sso-manager

# Install dependencies
npm install

# Start development
npm run dev
```

### Build Commands
- `npm run dev` - Start development server with hot reload
- `npm run build` - Build for production
- `npm run build-mac` - Build macOS application
- `npm run build-win` - Build Windows application
- `npm run make-dmg` - Create macOS installer

### Development Ports
- Vite dev server: http://localhost:8084
- Electron inspector: 5858

## Technical Constraints

### Platform Constraints
- **macOS**: Requires 10.15+ for Electron compatibility
- **Windows**: Requires Windows 10/11
- **Linux**: Not officially supported (Electron limitation for some features)

### Security Constraints
- Cannot store credentials in plain text
- Must use secure IPC communication
- Browser-based SSO flow required
- Cannot bypass AWS SSO authentication

### Performance Constraints
- Electron memory overhead (~100MB base)
- React rendering performance for large account lists
- IPC communication latency
- AWS API rate limits

### AWS SDK Constraints
- SSO token expiration (typically 8 hours)
- Region-specific endpoints
- OIDC device code flow requirements
- ECR login token validity (12 hours)

## Dependencies Overview

### Production Dependencies
Key libraries and their purposes:
- **lucide-react** - Icon library
- **sonner** - Toast notifications
- **date-fns** - Date formatting
- **recharts** - Data visualization
- **express** & **cors** - Local server for OAuth callback

### Build Dependencies
- **electron-builder** - Application packaging
- **@vitejs/plugin-react** - React support for Vite
- **autoprefixer** & **postcss** - CSS processing
- **tailwindcss** - CSS framework

## File Structure Conventions

### Source Organization
```
src/
├── components/     # Reusable UI components
├── contexts/       # React contexts
├── hooks/          # Custom React hooks
├── lib/            # Utility functions
├── pages/          # Route components
├── types/          # TypeScript definitions
└── utils/          # Helper functions
```

### Naming Conventions
- Components: PascalCase (e.g., `AccountCard.tsx`)
- Utilities: camelCase (e.g., `formatTimeLeft.ts`)
- Types: PascalCase with descriptive names
- CSS: Component-specific or Tailwind utilities

## Build & Deployment

### Build Process
1. Vite bundles React application
2. TypeScript compilation
3. Asset optimization
4. Electron Builder packages application
5. Code signing (if certificates available)
6. Installer creation

### Distribution
- **macOS**: DMG installer
- **Windows**: NSIS installer
- **Auto-updates**: Not currently implemented

## External Integrations

### AWS Services
- SSO/OIDC for authentication
- STS for temporary credentials
- ECR for container registry
- CodeArtifact for package management
- Organizations for account listing
- EKS for Kubernetes cluster management

### System Integration
- OS keychain for secure storage
- System notifications
- Default browser for SSO flow
- Shell integration for terminal features
