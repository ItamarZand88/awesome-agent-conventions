<!-- source: unclesp1d3r-cipherswarm — https://raw.githubusercontent.com/unclesp1d3r/CipherSwarm/main/.kiro/steering/structure.md -->
---
inclusion: always
---

# Project Structure & Organization

## Rails Application Structure

### Core Application (`app/`)

- **`models/`**: Domain models with state machines, validations, and business logic

  - Core entities: `Campaign`, `Attack`, `Task`, `Agent`, `HashList`, `WordList`, `RuleList`, `MaskList`
  - Uses `acts_as_paranoid` for soft deletes on most models
  - State machines for `Campaign`, `Attack`, and `Task` lifecycle management
  - Extensive model annotations with schema information

- **`controllers/`**: RESTful controllers following Rails conventions

  - `admin/` namespace for Administrate admin interface
  - `api/` namespace for API endpoints (documented with Rswag)
  - Nested routes: campaigns contain attacks, which contain tasks

- **`views/`**: ERB templates organized by controller

  - Uses ViewComponent for reusable UI elements
  - Bootstrap-based layouts and components
  - Partials in `shared/` and `partials/` directories

- **`components/`**: ViewComponent classes for reusable UI

  - `railsboot/` contains Bootstrap-based components
  - Custom components: `StatusPillComponent`, `ProgressBarComponent`, `NavbarDropdownComponent`

- **`jobs/`**: Background job classes using Sidekiq

  - `ProcessHashListJob`, `CalculateMaskComplexityJob`, `CountFileLinesJob`, `UpdateStatusJob`

- **`dashboards/`**: Administrate dashboard configurations for admin interface

### Configuration (`config/`)

- **`routes.rb`**: Comprehensive routing with nested resources and admin namespace
- **`application.rb`**: Main app config with autoload paths for components
- **`initializers/`**: Gem configurations (Devise, Sidekiq, ViewComponent, etc.)
- **`environments/`**: Environment-specific configurations

### Database (`db/`)

- **`migrate/`**: Extensive migration history with performance indexes
- **`schema.rb`**: Current database schema
- **`seeds.rb`**: Database seeding for development

### Testing (`spec/`)

- **RSpec** test suite with comprehensive coverage
- **`factories/`**: FactoryBot factories for all models
- **`fixtures/`**: Test files for file uploads and processing
- **`support/`**: Test helpers and configuration
- Component tests in `spec/components/`

## Key Architectural Patterns

### Model Relationships

```text
Project -> Campaign -> Attack -> Task
         -> HashList ----^
         -> WordList, RuleList, MaskList -> Attack
```

### State Management

- Models use `state_machines-activerecord` gem
- State transitions trigger callbacks for business logic
- Broadcasting updates to clients via Turbo streams

### File Handling

- Active Storage for file uploads (word lists, rule lists, hash lists)
- Background jobs for file processing and line counting
- Support for local storage and S3/MinIO

### Authorization

- CanCanCan abilities defined in `app/models/ability.rb`
- Rolify for role-based permissions
- Project-based access control

## Naming Conventions

### Files & Classes

- Models: singular, PascalCase (`Campaign`, `HashList`)
- Controllers: plural, snake_case files (`campaigns_controller.rb`)
- Views: match controller actions, snake_case
- Components: PascalCase with `Component` suffix

### Database

- Tables: plural, snake_case (`campaigns`, `hash_lists`)
- Foreign keys: `model_id` format
- Indexes: descriptive names with `index_` prefix
- Soft delete: `deleted_at` timestamp column

### Routes

- RESTful conventions with nested resources
- Admin routes under `/admin` namespace
- API routes under `/api` namespace

## Development Workflow

### Code Organization

- Keep controllers thin, move logic to models or service objects
- Use ViewComponents for reusable UI elements
- Background jobs for long-running operations
- Comprehensive test coverage with RSpec

### File Locations

- Business logic: models and service objects
- UI components: `app/components/`
- Background processing: `app/jobs/`
- Admin interface: `app/dashboards/`
- API documentation: `swagger/` directory
