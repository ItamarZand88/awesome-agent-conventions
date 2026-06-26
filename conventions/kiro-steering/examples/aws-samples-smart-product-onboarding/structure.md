<!-- source: aws-samples-smart-product-onboarding — https://raw.githubusercontent.com/aws-samples/aws-smart-product-onboarding/main/.kiro/steering/structure.md -->
# Project Structure

## Monorepo Organization

This is a **Projen-managed monorepo** using Nx for build orchestration and pnpm workspaces. All project configuration is defined in `.projenrc.ts` - modify this file and run `pnpm pdk` to regenerate project files.

## Root Level

- `.projenrc.ts` - **Primary project configuration** (modify this, not generated files)
- `package.json` - Generated root package.json (do not edit directly)
- `nx.json` - Nx configuration for build system
- `pnpm-workspace.yaml` - Workspace configuration
- `notebooks/` - Jupyter notebooks for system configuration
- `samples/` - Sample product data for testing
- `documentation/` - Architecture diagrams and guides

## Core Packages (`packages/`)

### API (`packages/api/`)

**Type-Safe API** generated from OpenAPI specification:

- `model/` - OpenAPI specification files
- `handlers/` - Lambda function implementations
  - `python/` - Python handlers (runtime: Python 3.13)
  - `typescript/` - TypeScript handlers (runtime: Node.js 22)
- `generated/` - Auto-generated code (do not edit)
  - `infrastructure/typescript/` - CDK constructs
  - `runtime/python/` - Python client library
  - `libraries/typescript-react-query-hooks/` - React hooks

### Infrastructure (`packages/infra/`)

**CDK Infrastructure** project:

- `src/` - CDK stack definitions
- `cdk.json` - CDK configuration
- Uses AWS PDK patterns for accelerated development

### Website (`packages/website/`)

**Cloudscape React demo** application:

- `src/` - React application source
- `public/` - Static assets
- Uses Cloudscape Design System components
- Requires runtime config from S3 for deployment

### Smart Product Onboarding (`packages/smart-product-onboarding/`)

**Python microservices** for AI processing:

#### Core Utils (`core-utils/`)

- Shared utilities and base classes
- Pydantic models for data validation
- AWS service integrations

#### Product Categorization (`product-categorization/`)

- Bottom-up categorization logic
- Category tree processing
- Jinja2 templates for prompts

#### Metaclasses (`metaclasses/`)

- Word vector processing with FAISS
- NLTK text processing
- Metaclass generation and matching

#### API Runtime (`api/`)

- Generated directly from `packages/api/generated/runtime/python/` into workspace
- Contains `api/runtime/` (generated) and `api/handlers/` (Lambda handlers)
- Used by Lambda handlers for API interactions

## Configuration Workflow

### 1. Notebooks (`notebooks/`)

**Required setup steps** after deployment:

- `1 - category tree prep.ipynb` - Prepare category hierarchies
- `2 - metaclasses generation.ipynb` - Generate word vectors
- Uses uv for Python dependency management

### 2. Sample Data (`samples/`)

Example product data structure:

```
samples/
├── B074M5HPBD/          # Product ID
│   ├── *.jpg            # Product images
│   └── metadata.txt     # Product metadata
└── README.md
```

## Development Patterns

### Projen Workflow

1. Modify `.projenrc.ts` for project changes
2. Run `pnpm pdk` to regenerate files
3. Never edit generated files directly

### Python Package Dependencies

- `core-utils` is a dependency of other Python packages
- `api` runtime is generated directly to `smart-product-onboarding/api/runtime/`
- Use uv for Python dependency management (workspace at `packages/smart-product-onboarding/`)

### API Development

- Define OpenAPI spec in `packages/api/model/`
- Handlers auto-generated with type safety
- Infrastructure constructs generated from API spec

### Build Dependencies

```
infra → api (infrastructure + runtime)
infra → website (for deployment)
infra → smart-product-onboarding packages
metaclasses → core-utils
product-categorization → core-utils
```

## Key Files to Modify

- `.projenrc.ts` - Project configuration
- `packages/api/model/` - API specifications
- `packages/infra/src/` - Infrastructure code
- `packages/website/src/` - Frontend code
- `packages/smart-product-onboarding/*/` - AI processing logic
- `notebooks/*.ipynb` - Configuration notebooks

## Generated Files (Do Not Edit)

- `package.json`, `nx.json`, workspace configs
- `packages/api/generated/` - All generated API code
- Python `pyproject.toml` files in packages
- CDK `cdk.out/` directories
