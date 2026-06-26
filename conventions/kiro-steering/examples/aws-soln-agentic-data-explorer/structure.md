<!-- source: aws-soln-agentic-data-explorer — https://raw.githubusercontent.com/aws-solutions-library-samples/guidance-for-agentic-data-exploration-on-aws/main/.kiro/steering/structure.md -->
# Project Structure & Organization

## Root Directory Layout

```
├── bin/                    # CDK application entry point
├── lib/                    # CDK infrastructure stacks (TypeScript)
├── docker/                 # Agent service containerization
│   ├── app/               # Python FastAPI application
│   │   ├── agents/        # Specialized agent implementations
│   │   ├── guardrails/    # Bedrock guardrails integration
│   │   └── tests/         # Agent service tests
│   ├── Dockerfile         # Container build configuration
│   └── requirements.txt   # Python dependencies
├── ui/                    # Flask web interface
│   ├── static/           # CSS, JS, and static assets
│   ├── templates/        # Jinja2 HTML templates
│   └── tests/            # UI integration tests
├── dev-tools/            # Development and deployment scripts
├── scripts/              # CloudShell deployment scripts
├── data/                 # Sample data and knowledge base content
├── evaluation/           # LLM evaluation framework
└── docs/                 # Architecture documentation
```

## Key Directories

### `/docker/app/` - Agent Service
- **Main application**: `app.py` (FastAPI server)
- **Agent implementations**: `agents/` directory with specialized agents
- **Supervisor agent**: Routes queries to appropriate specialized agents
- **Streaming support**: Real-time response streaming
- **Telemetry**: OpenTelemetry tracing configuration

### `/lib/` - Infrastructure (CDK)
- **agent-fargate-stack.ts**: Main Fargate service stack
- **graph-db-stack.ts**: Neptune graph database stack
- **monitoring-dashboard-stack.ts**: CloudWatch dashboards
- **lambda/**: ETL and data loading Lambda functions

### `/ui/` - Web Interface
- **Flask application**: `app.py` with chat interface
- **Templates**: Jinja2 templates in `templates/`
- **Static assets**: CSS, JavaScript, and external libraries
- **Mobile-responsive**: Amazon Q-style chat interface

### `/dev-tools/` - Development Scripts
- **deploy.sh**: Main deployment script with options
- **test-*.sh**: Testing scripts for different components
- **run-*.sh**: Local development server scripts

## File Naming Conventions

### Python Files
- **Snake case**: `supervisor_agent.py`, `data_visualizer_assistant.py`
- **Test files**: `test_*.py` pattern for pytest discovery
- **Agent files**: `*_assistant.py` for specialized agents

### TypeScript Files
- **Kebab case**: `agent-fargate-stack.ts`, `graph-db-stack.ts`
- **CDK stacks**: `*-stack.ts` pattern

### Configuration Files
- **Docker**: `Dockerfile`, `docker-compose.yml`
- **CDK**: `cdk.json`, `tsconfig.json`
- **Python**: `requirements.txt` files in relevant directories

## Agent Organization

### Agent Structure Pattern
```python
# Each agent follows this pattern:
from strands import Agent

agent_name = Agent(
    name="Agent Name",
    instructions="System prompt and instructions",
    model="bedrock-model-id",
    tools=[list_of_tools]
)
```

### Specialized Agents
- **supervisor_agent.py**: Main routing logic
- **general_assistant.py**: Fallback for unspecialized queries  
- **supply_chain_assistant.py**: Supply chain operations and weather functionality
- **schema_assistant.py**: Database schema conversion
- **data_visualizer_assistant.py**: Chart and visualization creation
- **image_assistant.py**: Image processing and generation
- **help_assistant.py**: Application help and guidance
- **product_analyst.py**: Product knowledge base queries

## Testing Structure

### Agent Tests (`docker/app/tests/`)
- **test_fast.py**: Quick unit tests without API calls
- **test_agents.py**: Integration tests with real agent calls
- **test_supervisor.py**: Supervisor routing validation
- **pytest.ini**: Test configuration

### UI Tests (`ui/tests/`)
- **test_ui_integration.py**: Flask application testing
- **run_tests.sh**: Test execution script

## Configuration Management

### Environment Variables
- **AWS credentials**: Handled by IAM roles in production
- **Model configurations**: Bedrock model IDs and parameters
- **Tracing settings**: OpenTelemetry configuration
- **CORS settings**: Allowed origins for web UI

### CDK Context
- **VPC configuration**: Optional existing VPC integration
- **Neptune settings**: Graph database connection parameters
- **Guardrails**: Bedrock guardrails configuration

## Data Organization

### `/data/` Directory
- **csv/**: Sample CSV data for testing and demos
- **kb/**: Knowledge base content (product reviews, etc.)
- **tariffs/**: US Harmonized Tariff Schedule data
- **upload/**: User-uploaded files for analysis

This structure supports clean separation of concerns between infrastructure, application logic, web interface, and supporting tools.