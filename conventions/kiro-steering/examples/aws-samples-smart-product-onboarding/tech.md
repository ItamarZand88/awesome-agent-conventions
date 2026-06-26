<!-- source: aws-samples-smart-product-onboarding — https://raw.githubusercontent.com/aws-samples/aws-smart-product-onboarding/main/.kiro/steering/tech.md -->
# Technology Stack

## Build System & Monorepo

- **Projen** - Project configuration and generation (`.projenrc.ts`)
- **Nx** - Monorepo build system and task orchestration
- **pnpm** - Package manager with workspaces
- **TypeScript** - Primary language for infrastructure and frontend

## AWS Infrastructure

- **AWS CDK** v2.195.0 - Infrastructure as Code
- **AWS PDK** v0.26.7 - AWS Project Development Kit for accelerated development
- **Amazon Bedrock** - AI/ML models (Claude 3 Haiku, Claude 3.5 Sonnet, Nova Micro)
- **AWS Step Functions** - Workflow orchestration for batch processing
- **AWS Lambda** - Serverless compute (Python 3.13, Node.js 22)
- **Amazon S3** - Storage for images, configurations, and results
- **Amazon DynamoDB** - Metaclass word vector store and process status
- **Amazon Cognito** - Authentication for demo website
- **AWS API Gateway** - REST API endpoints

## Python Stack

- **uv** - Python dependency management and project management
- **Python 3.12+** - Required runtime version
- **Pydantic** - Data validation and serialization
- **boto3** - AWS SDK
- **NLTK** - Natural language processing
- **NumPy** - Numerical computing
- **FAISS** - Vector similarity search
- **Jinja2** - Template engine

## Frontend

- **React** - UI framework
- **Cloudscape Design System** - AWS design components
- **TypeScript** - Type safety
- **React Query** - API state management

## Development Tools

- **ESLint** - Code linting
- **Prettier** - Code formatting
- **Jest** - Testing framework
- **Docker** - Containerization
- **Jupyter** - Notebooks for configuration

## Package Manager Guidelines

- **Use `pnpm exec` instead of `npx`** - This project uses pnpm as the package manager

## Common Commands

### Initial Setup

```bash
# Install dependencies
pnpm i
pnpm pdk install:ci
pnpm pdk build

# Docker login for public ECR
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

### Development

```bash
# Regenerate project files after .projenrc.ts changes
pnpm pdk

# Build all packages
pnpm pdk build

# Run tests
pnpm test

# Format code
pnpm eslint
```

### Deployment

```bash
# Deploy infrastructure
cd packages/infra
pnpm cdk bootstrap
pnpm cdk deploy smart-product-onboarding

# Deploy with cross-account Bedrock access
pnpm cdk deploy smart-product-onboarding --context BEDROCK_XACCT_ROLE=<ARN_OF_ROLE>
```

### Configuration (Notebooks)

```bash
cd notebooks
uv sync
uv run jupyter notebook
```

### Website Development

```bash
cd packages/website
# Download runtime config from S3
aws s3 cp s3://<ConfigurationBucket>/frontend/runtime-config.json public/runtime-config.json
pnpm pdk dev
```

## Key Dependencies

- Node.js >= 18.0.0 and < 22
- Python >= 3.12
- uv >= 0.5.0 - Python package and project manager
- pnpm >= 8.6.3
- AWS CLI configured
- Docker Desktop
