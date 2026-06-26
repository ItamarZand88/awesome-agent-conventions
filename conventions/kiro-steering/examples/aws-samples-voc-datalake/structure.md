<!-- source: aws-samples-voc-datalake — https://raw.githubusercontent.com/aws-samples/sample-voice-of-customer-datalake/main/.kiro/steering/structure.md -->
# VoC Data Lake - Project Structure

## Repository Layout

```
voice-of-customer-datalake/       # Root repository
├── docs/                         # Documentation
│   ├── data-lake-structure.md    # Data lake architecture documentation
│   ├── deployment.md             # Deployment guide
│   ├── feedback-forms.md         # Feedback forms documentation
│   ├── getting-started-plugins.md # Plugin development guide
│   ├── plugin-architecture.md    # Plugin system architecture
│   ├── processing-pipeline.md    # Processing pipeline documentation
│   └── scrapers.md               # Web scraper documentation
├── scripts/                      # Root-level scripts
│   └── find-*.sh                 # Dead code analysis scripts
├── static/                       # Static assets (demo videos, thumbnails)
├── package.json                  # Root scripts (shortcuts)
└── voc-datalake/                 # Main CDK project
    ├── bin/
    │   └── voc-datalake.ts           # CDK app entry point - defines all stacks
    ├── lib/stacks/                   # CDK stack definitions (TypeScript) - 5 stacks
    │   ├── api-stack.ts              # API Gateway, split API Lambdas (20KB policy limit), Webhooks, WAF
    │   ├── bedrock-access-stack.ts   # Bedrock model access configuration
    │   ├── core-stack.ts             # Core infrastructure (DynamoDB, S3, Cognito, CloudFront, KMS)
    │   ├── ingestion-stack.ts        # Plugin Lambdas, EventBridge schedules, SQS, Secrets
    │   └── processing-stack-consolidated.ts # Processing + Research (Bedrock, Step Functions)
    ├── lambda/                       # Python Lambda functions
    │   ├── processor/handler.py      # SQS consumer - Bedrock/Comprehend enrichment
    │   ├── aggregator/handler.py     # DynamoDB Streams consumer - real-time metrics
    │   ├── research/
    │   │   └── research_step_handler.py  # Step Functions task handler
    │   ├── shared/                   # Shared utilities across Lambdas (12 modules)
    │   │   ├── __init__.py
    │   │   ├── api.py                # API response helpers
    │   │   ├── auth.py               # Authentication utilities
    │   │   ├── avatar.py             # Avatar generation utilities
    │   │   ├── aws.py                # AWS client helpers
    │   │   ├── converse.py           # Bedrock conversation utilities
    │   │   ├── feedback.py           # Feedback data utilities
    │   │   ├── http.py               # HTTP utilities
    │   │   ├── idempotency.py        # Idempotency helpers
    │   │   ├── logging.py            # Logging utilities
    │   │   ├── project_chat.py       # Project chat utilities
    │   │   └── prompts.py            # Prompt management utilities
    │   ├── api/                      # Split into domain-specific Lambdas (20KB IAM policy limit) - 15 handlers
    │   │   ├── metrics_handler.py        # /feedback/*, /metrics/* (read-only queries)
    │   │   ├── chat_handler.py           # /chat/* (conversations)
    │   │   ├── chat_stream_handler.py    # Streaming chat (Lambda Function URL)
    │   │   ├── integrations_handler.py   # /integrations/*, /sources/* (credentials, schedules)
    │   │   ├── scrapers_handler.py       # /scrapers/* (web scraper management)
    │   │   ├── settings_handler.py       # /settings/* (brand, categories config)
    │   │   ├── projects_handler.py       # /projects/* (research projects, personas)
    │   │   ├── users_handler.py          # /users/* (Cognito user administration)
    │   │   ├── feedback_form_handler.py  # /feedback-form/*, /feedback-forms/* (embeddable forms)
    │   │   ├── data_explorer_handler.py  # /data-explorer/* (S3 raw data & DynamoDB browser)
    │   │   ├── logs_handler.py           # /logs/* (system logs)
    │   │   ├── manual_import_handler.py  # /manual-import/* (manual data import)
    │   │   ├── manual_import_processor.py # Manual import processing logic
    │   │   ├── projects.py               # Projects business logic (shared)
    │   │   └── prompts/                  # LLM prompt templates (6 templates)
    │   │       ├── avatar-generation.json
    │   │       ├── persona-generation.json
    │   │       ├── persona-import.json
    │   │       ├── prd-generation.json
    │   │       ├── prfaq-generation.json
    │   │       └── research-analysis.json
    │   └── layers/
    │       ├── ingestion-deps/       # Layer: requests, aws-lambda-powertools, beautifulsoup4
    │       └── processing-deps/      # Layer: aws-lambda-powertools
    ├── plugins/                      # Data source plugins
    │   ├── _shared/                  # Shared plugin utilities
    │   ├── _template/                # Template for new plugins
    │   └── webscraper/               # Configurable web scraper
    ├── frontend/                     # React dashboard (Vite + Tailwind)
    │   ├── src/
    │   │   ├── api/
    │   │   │   ├── client.ts         # API client, fetch helpers
    │   │   │   ├── types.ts          # API type definitions
    │   │   │   ├── projectsApi.ts    # Projects API (lazy-loaded)
    │   │   │   └── streamApi.ts      # Streaming API helpers (lazy-loaded)
    │   │   ├── services/auth.ts      # Cognito authentication service
    │   │   ├── components/           # Each component in its own folder with index.tsx (23 total)
    │   │   │   ├── AdminRoute/           # Admin-only route wrapper
    │   │   │   ├── Breadcrumbs/          # Navigation breadcrumbs
    │   │   │   ├── CategoriesManager/    # Category management UI
    │   │   │   ├── ChatExportMenu/       # Export chat conversations
    │   │   │   ├── ChatFilters/          # Chat filter controls
    │   │   │   ├── ChatMessage/          # Chat message component
    │   │   │   ├── ChatSidebar/          # Chat conversation sidebar
    │   │   │   ├── ConfirmModal/         # Confirmation dialog
    │   │   │   ├── DataSourceWizard/     # Data source setup wizard
    │   │   │   ├── DocumentExportMenu/   # Export documents
    │   │   │   ├── FeedbackCard/         # Feedback item display
    │   │   │   ├── FeedbackCarousel/     # Carousel for feedback items
    │   │   │   ├── Layout/               # Main layout with sidebar (reads menu-config.json)
    │   │   │   ├── MetricCard/           # Dashboard metric card
    │   │   │   ├── PageLoader/           # Page loading indicator
    │   │   │   ├── PersonaExportMenu/    # Export personas
    │   │   │   ├── ProtectedRoute/       # Auth-protected route wrapper
    │   │   │   ├── S3ImportExplorer/     # S3 file browser
    │   │   │   ├── SentimentBadge/       # Sentiment indicator
    │   │   │   ├── SocialFeed/           # Live social media feed
    │   │   │   ├── TimeRangeSelector/    # Date range picker
    │   │   │   ├── UserAdmin/            # User administration
    │   │   │   └── UserProfileModal/     # User profile modal
    │   │   ├── pages/                # Each page in its own folder (14 total)
    │   │   │   ├── Categories/       # Category breakdown and analysis
    │   │   │   ├── Chat/             # AI chat interface
    │   │   │   ├── Dashboard/        # Overview with charts and social feed
    │   │   │   ├── DataExplorer/     # S3 raw data and DynamoDB browser
    │   │   │   ├── Feedback/         # Filterable feedback list
    │   │   │   ├── FeedbackDetail/   # Single feedback item view
    │   │   │   ├── FeedbackForms/    # Feedback form management
    │   │   │   ├── Login/            # Cognito login page
    │   │   │   ├── Prioritization/   # Issue prioritization
    │   │   │   ├── ProblemAnalysis/  # Problem analysis dashboard
    │   │   │   ├── ProjectDetail/    # Single project view
    │   │   │   ├── Projects/         # Research projects list
    │   │   │   ├── Scrapers/         # Web scraper configuration
    │   │   │   └── Settings/         # Configuration and integrations (uses getEnabledPlugins)
    │   │   ├── store/
    │   │   │   ├── configStore.ts    # Zustand state (config, time range, custom dates)
    │   │   │   ├── chatStore.ts      # Chat conversation state
    │   │   │   ├── authStore.ts      # Authentication state
    │   │   │   └── manualImportStore.ts # Manual import state
    │   │   ├── plugins/              # Frontend plugin system
    │   │   │   ├── index.ts          # Plugin loader (getEnabledPlugins, getPluginManifests)
    │   │   │   ├── types.ts          # Plugin type definitions (with enabled field)
    │   │   │   └── manifests.json    # Generated plugin manifests
    │   │   ├── config/
    │   │   │   └── menu-config.json  # Generated menu visibility config
    │   │   ├── constants/
    │   │   │   └── filters.ts        # Filter constants and options
    │   │   └── utils/
    │   │       └── dateUtils.ts      # Date utility functions
    │   ├── package.json
    │   └── vite.config.ts
    ├── schemas/
    │   └── feedback-event.schema.json
    ├── scripts/
    │   ├── build-layers.sh           # Build Lambda layers with Docker (ARM64)
    │   ├── test-api.sh               # API validation script
    │   ├── generate-manifests.ts     # Generate plugin manifests with enabled status
    │   ├── generate-menu-config.ts   # Generate menu config from cdk.context.json
    │   ├── generate-integrity.ts     # Generate plugin integrity hashes
    │   ├── validate-plugins.ts       # Validate plugin configurations
    │   └── test-plugin-loader.ts     # Test plugin loading
    ├── cdk.json
    ├── tsconfig.json
    └── package.json
```

## Storage

### S3 Raw Data Lake

| Bucket | Structure | Purpose |
|--------|-----------|---------|
| `voc-raw-data-{account}-{region}` | `raw/{source}/{year}/{month}/{day}/{id}.json` | Raw scraped/ingested data archival |
| `voc-raw-data-{account}-{region}` | `avatars/{project_id}/{persona_id}.png` | AI-generated persona avatars |

### DynamoDB Tables

| Table | PK | SK | Purpose |
|-------|----|----|---------|
| `voc-feedback` | `SOURCE#{platform}` | `FEEDBACK#{id}` | Processed feedback with GSIs for date, category, urgency |
| `voc-aggregates` | `METRIC#{type}` | `{date}` | Pre-computed metrics, brand config, form configs |
| `voc-watermarks` | `{source}` | - | Ingestion state tracking |
| `voc-projects` | `PROJECT#{id}` | `META\|PERSONA#{id}\|PRD#{id}\|PRFAQ#{id}` | Projects with personas, PRDs, PR/FAQs |
| `voc-jobs` | `PROJECT#{id}` | `JOB#{id}` | Long-running async jobs (research, persona generation) |
| `voc-conversations` | `USER#{id}` | `CONV#{id}` | AI chat conversation history |
| `voc-idempotency` | `{id}` | - | Lambda Powertools idempotency tracking |

## API Endpoints

### Metrics (metrics_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/feedback` | List feedback with filters (days, source, category, sentiment) |
| GET | `/feedback/{id}` | Get single feedback item |
| GET | `/feedback/{id}/similar` | Get similar feedback items |
| GET | `/feedback/urgent` | Get high-urgency items |
| GET | `/feedback/entities` | Get keywords, categories, issues for filters |
| GET | `/metrics/summary` | Dashboard summary metrics |
| GET | `/metrics/sentiment` | Sentiment breakdown |
| GET | `/metrics/categories` | Category breakdown |
| GET | `/metrics/sources` | Source breakdown |
| GET | `/metrics/personas` | Persona breakdown |

### Chat (chat_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| POST | `/chat` | AI chat endpoint |
| GET | `/chat/conversations` | List conversations |
| GET | `/chat/conversations/{id}` | Get conversation |
| DELETE | `/chat/conversations/{id}` | Delete conversation |

### Integrations (integrations_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/integrations/status` | Integration status |
| PUT | `/integrations/{source}/credentials` | Update credentials |
| POST | `/integrations/{source}/test` | Test integration |
| GET | `/sources/status` | Source schedule status |
| PUT | `/sources/{source}/enable` | Enable source |
| PUT | `/sources/{source}/disable` | Disable source |

### Scrapers (scrapers_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/scrapers` | List scraper configs |
| POST | `/scrapers` | Save scraper config |
| DELETE | `/scrapers/{id}` | Delete scraper |
| GET | `/scrapers/templates` | Get scraper templates |
| POST | `/scrapers/{id}/run` | Trigger scraper run |

### Settings (settings_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/settings/brand` | Get brand configuration |
| PUT | `/settings/brand` | Save brand configuration |
| GET | `/settings/categories` | Get category configuration |
| PUT | `/settings/categories` | Save category configuration |
| POST | `/settings/categories/generate` | AI-generate categories |

### Users (users_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/users` | List Cognito users |
| POST | `/users` | Create user |
| PUT | `/users/{username}` | Update user |
| DELETE | `/users/{username}` | Delete user |
| POST | `/users/{username}/reset-password` | Reset password |

### Feedback Forms (feedback_form_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/feedback-form/config` | Get form config (public) |
| PUT | `/feedback-form/config` | Update form config |
| POST | `/feedback-form/submit` | Submit feedback (public) |
| GET | `/feedback-form/embed` | Get embed code |
| GET | `/feedback-forms` | List all forms |
| POST | `/feedback-forms` | Create form |
| GET | `/feedback-forms/{id}` | Get form (public) |
| PUT | `/feedback-forms/{id}` | Update form |
| DELETE | `/feedback-forms/{id}` | Delete form |

### Projects (projects_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/projects` | List projects |
| POST | `/projects` | Create project |
| GET | `/projects/{id}` | Get project with personas/documents |
| PUT | `/projects/{id}` | Update project |
| DELETE | `/projects/{id}` | Delete project |
| POST | `/projects/{id}/personas/generate` | Generate personas from feedback |
| POST | `/projects/{id}/research` | Run research job (Step Functions) |
| POST | `/projects/{id}/chat` | Project-scoped chat |

### Webhooks
| Method | Path | Description |
|--------|------|-------------|
| POST | `/webhooks/{plugin}` | Plugin webhook receiver (public) |

### Logs (logs_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/logs` | Get system logs |
| GET | `/logs/errors` | Get error logs |

### Manual Import (manual_import_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| POST | `/manual-import` | Import data manually |
| GET | `/manual-import/status` | Get import status |
| POST | `/manual-import/validate` | Validate import data |

### Data Explorer (data_explorer_handler.py)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/data-explorer/s3` | Browse S3 raw data bucket with folder navigation |
| GET | `/data-explorer/s3/preview` | Preview JSON file content from S3 |
| PUT | `/data-explorer/s3` | Create or update S3 file (with optional DynamoDB sync) |
| DELETE | `/data-explorer/s3` | Delete S3 file |
| PUT | `/data-explorer/feedback` | Update DynamoDB feedback record (with optional S3 sync) |
| DELETE | `/data-explorer/feedback` | Delete DynamoDB feedback record |
| GET | `/data-explorer/stats` | Get data lake statistics |

## Adding a New Data Source

1. Create plugin in `plugins/{source}/` with `manifest.json` and `handler.py`
2. Follow the template in `plugins/_template/`
3. Run `npm run validate:plugins` to verify configuration
4. Add source config to `ingestion-stack.ts` (schedule, timeout)
5. Add credentials to Secrets Manager template
6. Update frontend Settings page with source fields

## CDK Stack Dependencies

```
VocCoreStack (DynamoDB tables, S3 raw data bucket, KMS, Cognito, CloudFront)
       │
       ├──▶ VocIngestionStack (Plugin Lambdas, EventBridge, SQS, Secrets)
       │           │
       │           └──▶ VocProcessingStackConsolidated (Processor, Aggregator, Step Functions, Bedrock)
       │
       ├──▶ VocApiStack (API Gateway, API Lambdas, Webhooks, WAF)
       │           │
       │           └── Depends on: processingQueue, secretsArn, researchStateMachine, userPool
       │
       └──▶ VocBedrockAccessStack (Bedrock model access configuration)
```
