<!-- source: repo-sprint-digest — https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/techContext.md -->
# Technical Context: Repository Sprint Digest

## Technology Stack

### Core Technologies
- **Node.js**: Runtime environment for executing JavaScript code
- **GitHub Actions**: CI/CD platform for automation
- **GitHub API**: Data source for repository information

### Key Dependencies
- **@actions/core**: Core functionality for GitHub Actions
- **@octokit/rest**: Official GitHub REST API client
- **dotenv**: Environment variable management for local development
- **js-yaml**: YAML parsing and generation for output formats

### Development Dependencies
- **@vercel/ncc**: Compiler for creating single-file builds for distribution

## Development Setup

### Local Development Environment
To set up a local development environment:

1. Clone the repository
2. Install dependencies with `npm install`
3. Create a `.env` file based on `.env.example`
4. Obtain a GitHub Personal Access Token with `repo` scope
5. Configure the target repository and other parameters in the `.env` file
6. Run locally with `npm start`

### Build Process
The project uses `@vercel/ncc` to compile the application into a single file for distribution:

```bash
npm run build
```

This creates a standalone `dist/index.js` file that includes all dependencies, making it suitable for use in GitHub Actions.

## Technical Constraints

### GitHub API Limitations
- **Rate Limiting**: Subject to GitHub API rate limits (5,000 requests per hour for authenticated requests)
- **Pagination**: Limited to fetching 100 PRs per page, requiring pagination for repositories with many PRs
- **Authentication**: Requires a GitHub token with appropriate permissions

### File System Constraints
- **Concurrency**: No built-in locking mechanism for file access, potential for conflicts if multiple instances run simultaneously
- **File Size**: No explicit handling for very large output files that might accumulate over time

### GitHub Actions Constraints
- **Execution Time**: Limited to 6 hours maximum runtime per job
- **Environment**: Runs in a clean environment each time, requiring all state to be persisted externally
- **Permissions**: Requires appropriate permissions to commit changes back to the repository

## Configuration Options

### GitHub Action Inputs
- `target_repository`: Repository to monitor (owner/repo format)
- `days_to_check`: Number of days to look back for PRs (default: 1)
- `output_file`: File path to write results
- `output_format`: Output format (markdown/json/yaml, default: markdown)
- `github_token`: GitHub token for API authentication

### Environment Variables (Local Development)
- `GITHUB_TOKEN`: GitHub Personal Access Token
- `INPUT_TARGET_REPOSITORY`: Target repository in owner/repo format
- `INPUT_DAYS_TO_CHECK`: Number of days to check
- `INPUT_OUTPUT_FILE`: Output file path
- `INPUT_OUTPUT_FORMAT`: Output format

## Output Formats

### Markdown Format
```markdown
# PR Change History (2023-04-01)

## 2023-04-01
- [#123](https://github.com/owner/repo/pull/123) PR Title (@author)
```

### JSON Format
```json
{
  "repository": "owner/repo",
  "created_at": "2023-04-01",
  "last_updated": "2023-04-01",
  "pr_history": {
    "2023-04-01": [
      {
        "number": 123,
        "title": "PR Title",
        "url": "https://github.com/owner/repo/pull/123",
        "author": "author",
        "mergedAt": "2023-04-01T14:32:25Z"
      }
    ]
  }
}
```

### YAML Format
```yaml
repository: owner/repo
created_at: '2023-04-01'
last_updated: '2023-04-01'
pr_history:
  '2023-04-01':
    - number: 123
      title: PR Title
      url: https://github.com/owner/repo/pull/123
      author: author
      mergedAt: '2023-04-01T14:32:25Z'
```

## Deployment Process

### GitHub Action Deployment
1. Create a workflow file in the target repository's `.github/workflows/` directory
2. Configure the action with appropriate inputs
3. Set up the workflow trigger (schedule, manual, or other events)
4. Ensure the workflow has appropriate permissions to commit changes

### Version Management
- The action is versioned using semantic versioning
- Users reference specific versions in their workflow files (e.g., `uses: sasamuku/repo-sprint-digest@v1.0.0`)
- Major version tags (e.g., `v1`) are updated to point to the latest compatible release
