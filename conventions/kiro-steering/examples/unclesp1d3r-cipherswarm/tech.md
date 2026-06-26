<!-- source: unclesp1d3r-cipherswarm — https://raw.githubusercontent.com/unclesp1d3r/CipherSwarm/main/.kiro/steering/tech.md -->
---
inclusion: always
---

# Technology Stack & Build System

## Core Framework & Language

- **Ruby**: 3.4.5 (see `.ruby-version`)
- **Rails**: 7.2+ (modern Rails with latest features)
- **Database**: PostgreSQL with Active Record
- **Background Jobs**: Sidekiq with Redis
- **Asset Pipeline**: esbuild + Sass + PostCSS

## Key Dependencies

### Backend

- **Authentication**: Devise
- **Authorization**: CanCanCan + Rolify
- **Admin Interface**: Administrate
- **API Documentation**: Rswag (Swagger)
- **File Storage**: Active Storage (with AWS S3 support)
- **State Machines**: state_machines-activerecord
- **Soft Deletes**: Paranoia (acts_as_paranoid)
- **View Components**: ViewComponent for reusable UI components

### Frontend

- **CSS Framework**: Bootstrap 5.3.3 with Bootstrap Icons
- **JavaScript**: Stimulus + Turbo (Hotwire)
- **File Uploads**: Dropzone
- **Build Tools**: esbuild, Sass, PostCSS with Autoprefixer

### Development & Testing

- **Testing**: RSpec with FactoryBot, Capybara for integration tests
- **Code Quality**: RuboCop (rails-omakase config), Brakeman, Bundler Audit
- **Documentation**: Annotaterb for model annotations

## Common Commands

### Development Setup

```bash
# Install dependencies
bundle install
bun install

# Database setup
rails db:create db:migrate db:seed

# Start development server (uses Procfile.dev)
bin/dev
```

### Asset Building

```bash
# Build CSS
bun run build:css

# Watch CSS changes
bun run watch:css

# Build JavaScript
bun run build
```

### Testing

```bash
# Run all tests
bundle exec rspec

# Run with coverage
COVERAGE=true bundle exec rspec

# Run specific test file
bundle exec rspec spec/models/campaign_spec.rb
```

### Code Quality

```bash
# Run RuboCop
bundle exec rubocop

# Auto-fix RuboCop issues
bundle exec rubocop -A

# Security scan
bundle exec brakeman

# Dependency audit
bundle exec bundle-audit
```

### Docker

```bash
# Development
docker compose up

# Production
docker compose -f docker-compose-production.yml up
```

## Configuration Notes

- **Frozen String Literals**: All Ruby files use `# frozen_string_literal: true`
- **SPDX Headers**: All files include SPDX license headers
- **Time Zone**: Eastern Time (US & Canada)
- **Job Queue**: Sidekiq with Redis backend
- **File Storage**: Configurable between local and S3 (MinIO in development)
