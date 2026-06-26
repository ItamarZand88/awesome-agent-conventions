<!-- source: app-med-ai-gen — https://raw.githubusercontent.com/ModusCreateOrg/app-med-ai-gen/main/memory-bank/techContext.md -->
# Technical Context

## Core Technologies
1. Frontend
   - Ionic + React
   - TypeScript
   - Tailwind CSS
   - TanStack Query
   - Remark Markdown

2. Backend
   - Node.js
   - Express
   - TypeScript
   - AWS Services
   - MongoDB

3. AI Services
   - Perplexity API
   - Amazon Bedrock
   - OCR Services
   - NLP Processing

4. Testing
   - Vitest
   - React Testing Library
   - Mock Service Worker
   - Jest

## Development Setup
1. Environment
   - Node.js v18+
   - npm/yarn
   - Git
   - Docker

2. IDE Requirements
   - VS Code
   - Ionic CLI
   - TypeScript support
   - ESLint/Prettier

3. Development Tools
   - Git hooks (Husky)
   - Linting
   - Formatting
   - Type checking

## Technical Constraints
1. Mobile-First
   - iOS/Android support
   - No web browser support
   - Responsive design
   - Native features

2. Performance
   - Fast document processing
   - Efficient state management
   - Optimized image handling
   - Minimal network usage

3. Security
   - HIPAA compliance
   - Data encryption
   - Secure storage
   - Access control

4. Testing
   - 60% code coverage
   - Unit test requirements
   - Integration tests
   - E2E testing

## Dependencies
1. Frontend Dependencies
   ```json
   {
     "dependencies": {
       "@ionic/react": "latest",
       "react": "latest",
       "typescript": "latest",
       "tailwindcss": "latest",
       "@tanstack/react-query": "latest",
       "remark": "latest"
     }
   }
   ```

2. Development Dependencies
   ```json
   {
     "devDependencies": {
       "vitest": "latest",
       "@testing-library/react": "latest",
       "msw": "latest",
       "eslint": "latest",
       "prettier": "latest"
     }
   }
   ```

## Build & Deployment
1. Build Process
   - TypeScript compilation
   - Asset optimization
   - Bundle generation
   - Environment configuration

2. Deployment
   - CI/CD pipeline
   - Environment management
   - Version control
   - Release process

3. Monitoring
   - Error tracking
   - Performance metrics
   - Usage analytics
   - Health checks 