<!-- source: aws-soln-agentic-data-explorer — https://raw.githubusercontent.com/aws-solutions-library-samples/guidance-for-agentic-data-exploration-on-aws/main/.kiro/steering/tech.md -->
# Technology Stack & Build System

## Core Technologies

### Backend
- **Python 3.13+** - Main application language
- **FastAPI** - Web framework for agent service
- **Strands Agents** - Multi-agent framework with OpenTelemetry tracing
- **LangChain** - LLM integration and tooling
- **Boto3** - AWS SDK for Python
- **Bedrock AgentCore** - AWS Bedrock agent memory and tools

### Frontend
- **Flask** - Web UI framework
- **Jinja2 templates** - Server-side rendering
- **JavaScript/jQuery** - Client-side interactions
- **D3.js** - Data visualization
- **DataTables** - Interactive tables

### Infrastructure
- **AWS CDK (TypeScript)** - Infrastructure as Code
- **Docker/Podman** - Containerization
- **AWS Fargate** - Container orchestration
- **Amazon CloudFront** - CDN and HTTPS termination
- **Application Load Balancer** - Load balancing
- **Amazon Cognito** - Authentication
- **Amazon Neptune** - Graph database (optional)

### Development Tools
- **TypeScript** - CDK infrastructure code
- **Node.js 18+** - Build tooling
- **Prettier** - Code formatting
- **pytest** - Python testing framework

## Common Commands

### Development Setup
```bash
# Install dependencies
npm install
pip install -r docker/requirements.txt

# Bootstrap CDK (one-time)
npx cdk bootstrap
```

### Local Development
```bash
# Run complete system locally with tracing
./dev-tools/run-with-tracing.sh

# Run UI locally (connects to local agent service)
./dev-tools/run-ui-local.sh

# Run UI locally (connects to AWS agent service)
./dev-tools/run-ui-local.sh --aws

# Run both services locally
./dev-tools/run-all-local.sh
```

### Testing
```bash
# Run all tests (agent + UI)
./dev-tools/test-all.sh

# Run agent tests only
./dev-tools/test-agent.sh                # Fast tests
./dev-tools/test-agent.sh --all         # All tests including integration
./dev-tools/test-agent.sh --coverage    # With coverage report

# Run UI tests only
./dev-tools/test-ui.sh

# Run evaluation framework
./dev-tools/run-evaluation.sh
./dev-tools/run-evaluation.sh --baseline --runs 5
```

### Deployment
```bash
# Deploy to AWS
./dev-tools/deploy.sh

# Deploy with Neptune graph database
./dev-tools/deploy.sh --with-graph-db

# Deploy with existing VPC
./dev-tools/deploy.sh --vpc-id vpc-123

# CloudShell deployment
./scripts/cloudshell-deploy.sh
```

### Container Operations
```bash
# Build container locally
podman build ./docker/ -t agent_container

# Run container locally
podman run -p 127.0.0.1:8000:8000 -t agent_container

# Start container runtime (Podman)
podman machine start
```

## Build System Notes
- Uses **CDK_DOCKER=podman** environment variable for container builds
- TypeScript compilation handled by CDK automatically
- Python dependencies managed via requirements.txt files
- Container images built during CDK deployment
- Supports both Docker and Podman for local development