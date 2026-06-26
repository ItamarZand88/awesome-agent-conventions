<!-- source: repo-sprint-digest — https://raw.githubusercontent.com/sasamuku/repo-sprint-digest/main/memory-bank/projectbrief.md -->
# Project Brief: Repository Sprint Digest

## Project Overview
Repository Sprint Digest is a GitHub Action that monitors merged Pull Requests (PRs) in specified GitHub repositories and automatically records their change history to a designated file. The changes are organized by date, making it an effective tool for sprint reviews and team progress tracking.

## Core Requirements
1. Monitor merged PRs in specified GitHub repositories
2. Record PR information (number, title, author, merge date) to a designated file
3. Group PRs by their merge date for easy review
4. Support multiple output formats (Markdown, JSON, YAML)
5. Avoid duplicate entries when run multiple times
6. Provide flexible configuration options
7. Function both as a GitHub Action and as a locally executable tool

## Goals
- Facilitate effective sprint reviews and team standups with organized PR history
- Support agile development by providing clear visibility into daily/weekly accomplishments
- Automate the documentation of development activities
- Maintain a comprehensive history of all changes over time
- Integrate seamlessly with GitHub Actions workflows

## Scope
- **In Scope**: PR monitoring, data collection, formatted output generation, GitHub Action integration
- **Out of Scope**: PR content analysis, code quality assessment, performance metrics

## Success Criteria
- Successfully monitors and records merged PRs from specified repositories
- Correctly groups PRs by date and avoids duplicates
- Generates properly formatted output files (Markdown, JSON, YAML)
- Works reliably both as a GitHub Action and as a local tool
- Requires minimal configuration and maintenance
