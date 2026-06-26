<!-- source: raccoonyy-awspirin — https://raw.githubusercontent.com/raccoonyy/awspirin/main/.kiro/steering/structure.md -->
# Project Structure

## Directory Layout

```
├── awspirin/              # Main application directory
│   ├── app/               # Next.js App Router pages
│   │   └── page.tsx       # Main application page with layout and state
│   └── components/        # Reusable React components
│       ├── action-selector.tsx    # AWS action selection interface
│       ├── policy-preview.tsx     # JSON policy preview and validation
│       └── resource-selector.tsx  # AWS resource selection interface
├── .kiro/                 # Kiro AI assistant configuration
└── .vscode/              # VS Code workspace settings
```

## Component Architecture

### Main Page (`awspirin/app/page.tsx`)
- Central state management for the entire application
- Defines TypeScript interfaces for data models
- Contains initial data for AWS resources and actions
- Implements the main layout with 3-column grid (30%-40%-30%)

### Component Responsibilities
- **ResourceSelector**: AWS service selection with search functionality
- **ActionSelector**: Hierarchical permission selection with categories and dependencies
- **PolicyPreview**: Real-time JSON policy generation and validation

## Data Models
- `AWSResource`: Service definitions with icons and descriptions
- `AWSAction`: Permission definitions with categories and dependencies
- `PolicyConfiguration`: Saved policy templates

## Naming Conventions
- Components use PascalCase with descriptive names
- Files use kebab-case matching component names
- Props interfaces follow `ComponentNameProps` pattern
- State variables use camelCase with descriptive names

## Import Patterns
- Relative imports for local components (`@/components/...`)
- UI components from shadcn/ui (`@/components/ui/...`)
- External libraries imported directly

- DRY 원칙과 SOLID 원칙을 준수해요.
- 컴포넌트를 새로 만들기보다는 기존 컴포넌트를 재사용해요.
- 오버 엔지니어링하지 않게 항상 유의해요.

- UI는 #[[file:awspirin/app/page.tsx]], #[[awspirin/components/action-selector.tsx]], #[[awspirin/components/policy-preview.tsx]], #[[awspirin/components/resource-selector.tsx]] 파일을 참고하되, shadcn을 활용해요.
