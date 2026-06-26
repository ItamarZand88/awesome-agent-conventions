<!-- source: repo-sprint-digest — https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/activeContext.md -->
# Active Context: Repository Sprint Digest

## Current Focus
The current focus is on enhancing the Repository Sprint Digest project with AI-powered PR summarization capabilities. While the core functionality (monitoring merged PRs and recording change history) is stable, we are now planning to add AI-driven features to automatically summarize PR content and provide more valuable insights to teams.

## Recent Changes
1. Created comprehensive documentation for the AI summarization feature in `docs/ai-summary-feature.md`
2. Designed the implementation approach using LangChain and OpenAI API
3. Established cost optimization strategies to keep API usage efficient

## Active Decisions
1. **Configuration Approach**: The project uses a combination of GitHub Action inputs and environment variables for configuration, providing flexibility for both GitHub Actions and local execution.
2. **Output Format Strategy**: The project supports multiple output formats (Markdown, JSON, YAML) with format-specific handling for each.
3. **Duplicate Prevention**: The system checks for existing PR entries to prevent duplicates when run multiple times.
4. **Date-Based Organization**: PRs are organized by merge date rather than other potential organizing principles.

## Current Considerations
1. **Active Enhancement**: We are actively working on implementing the first enhancement mentioned in the README:
   - AI-powered PR summary generation ← Currently in planning phase

   Other potential enhancements for future consideration include:
   - Weekly/sprint rollup summaries
   - Customizable PR filtering options
   - Statistical analysis of PR trends
   - Integration with notification platforms
   - Automated meeting agenda generation

2. **Configuration Files**: The VSCode tabs show `config/repos.yaml`, but this file doesn't exist in the repository. It might be a planned feature or local configuration file not included in the repository.

3. **Local Testing**: The project includes support for local testing with command-line arguments or environment variables, making it easier to develop and test changes.

4. **Pagination Limits**: The current implementation limits PR fetching to 3 pages (300 PRs), which might need adjustment for repositories with high PR volume.

## Next Steps
1. **Implement AI Summarization Feature**:
   - Install required dependencies (LangChain, OpenAI SDK)
   - Create new module for AI processing (`src/ai.js`)
   - Extend GitHub API interaction to fetch PR details
   - Implement summarization logic
   - Integrate summaries into output formats

2. **Understand Potential Configuration Files**: Investigate the purpose of the non-existent `config/repos.yaml` file mentioned in the VSCode tabs.

3. **Testing Strategy**:
   - Develop tests for the new AI summarization feature
   - Ensure reliability with different PR content types and sizes
   - Test token optimization strategies

4. **Documentation Updates**:
   - Update README to include information about the new AI feature
   - Add examples of AI-summarized PR digests

## Open Questions
1. What is the purpose of the `config/repos.yaml` file mentioned in the VSCode tabs?
2. What is the optimal balance between summary detail and token usage for cost efficiency?
3. Should we implement a feedback mechanism for improving AI summaries over time?
4. What specific aspects of PRs are most important to highlight in the summaries?
