<!-- source: namuan-wt-manager — https://raw.githubusercontent.com/namuan/wt-manager/main/.kiro/steering/tech.md -->
# Technology Stack

## Core Technologies

- **Python 3.12+**: Primary programming language
- **PyQt6**: GUI framework for cross-platform desktop application
- **uv**: Modern Python package manager and build system
- **Git**: Version control system integration

## Development Tools

- **pytest**: Testing framework with pytest-qt for GUI testing
- **ruff**: Fast Python linter and formatter
- **pre-commit**: Git hooks for code quality
- **pyinstaller**: Application packaging for distribution
- **tox-uv**: Testing across multiple environments

## Build System

The project uses `uv` as the modern Python package manager with the following configuration:

- Build backend: `uv_build`
- Dependency management via `pyproject.toml`
- Virtual environment management with `uv sync`

## Common Commands

### Development Setup

```bash
make install          # Install dependencies and pre-commit hooks
```

### Development Workflow

```bash
make run             # Run the application
make test            # Run all tests
make test ARGS="path/to/test.py::TestClass::test_method -v -s"  # Run specific test
make check           # Run linting and pre-commit checks
```

### Code Quality

```bash
uv run pre-commit run -a    # Run all pre-commit hooks
uv run ruff check          # Lint code
uv run ruff format         # Format code
```

## Architecture Patterns

- **MVC Pattern**: Model-View-Controller separation
- **Service Layer**: Business logic abstraction
- **Dataclasses**: Immutable data models with validation
- **Async Operations**: QThread for non-blocking Git operations
- **Configuration Management**: OS-appropriate config storage

## Testing Strategy

- **Unit Tests**: Service layer and model validation
- **Integration Tests**: Git operations and file system interactions
- **UI Tests**: Critical user workflows with pytest-qt
- **Mock Strategy**: Mock external dependencies and Git operations
