<!-- source: namuan-wt-manager — https://raw.githubusercontent.com/namuan/wt-manager/main/.kiro/steering/structure.md -->
# Project Structure

## Directory Organization

```
wt-manager/
├── src/wt_manager/           # Main application package
│   ├── __init__.py
│   ├── app.py               # Application entry point and lifecycle
│   ├── models/              # Data models and structures
│   │   ├── project.py       # Project model with validation
│   │   └── worktree.py      # Worktree model with metadata
│   ├── services/            # Business logic layer
│   │   └── base.py          # Base service classes
│   ├── ui/                  # PyQt6 user interface components
│   │   └── main_window.py   # Main application window
│   └── utils/               # Utility modules
│       ├── exceptions.py    # Custom exception classes
│       ├── logging_config.py # Logging configuration
│       └── path_manager.py  # OS-appropriate path management
├── tests/                   # Test suite
│   ├── test_models.py       # Model validation tests
│   └── test_init.py         # Basic initialization tests
├── assets/                  # Application assets
│   ├── generate-icons.sh    # Icon generation script
│   └── *.png, *.ico, *.icns # Application icons
├── scripts/                 # Build and deployment scripts
└── .kiro/                   # Kiro configuration and specs
    ├── specs/               # Feature specifications
    └── steering/            # AI assistant guidance
```

## Code Organization Patterns

### Models (`src/wt_manager/models/`)

- Use `@dataclass` for immutable data structures
- Include validation in `__post_init__` methods
- Provide serialization methods (`to_dict`, `from_dict`, `to_json`, `from_json`)
- Implement proper `__eq__`, `__hash__`, `__str__`, and `__repr__` methods

### Services (`src/wt_manager/services/`)

- Implement business logic separate from UI
- Use dependency injection for testability
- Handle Git operations and external system interactions
- Provide async operations using QThread for UI responsiveness

### UI Components (`src/wt_manager/ui/`)

- Follow PyQt6 conventions and patterns
- Separate UI logic from business logic
- Use signals and slots for component communication
- Implement proper resource cleanup

### Utilities (`src/wt_manager/utils/`)

- Cross-platform path management
- Centralized logging configuration
- Custom exception hierarchies
- Common helper functions

## Naming Conventions

- **Files**: Snake case (`main_window.py`, `path_manager.py`)
- **Classes**: Pascal case (`MainWindow`, `ProjectService`)
- **Methods/Functions**: Snake case (`get_worktrees`, `validate_project`)
- **Constants**: Upper snake case (`DEFAULT_TIMEOUT`, `CONFIG_DIR`)
- **Private methods**: Leading underscore (`_validate_git_repository`)

## Import Organization

Follow this import order:

1. Standard library imports
2. Third-party imports (PyQt6, etc.)
3. Local application imports (relative imports)

## Configuration Storage

- **Development**: Local `.kiro/` directory for specs and steering
- **Runtime**: OS-appropriate directories via `PathManager`
  - macOS: `~/Library/Application Support/GitWorktreeManager/`
  - Windows: `%APPDATA%/GitWorktreeManager/`
  - Linux: `~/.config/git-worktree-manager/`

## Testing Structure

- **Unit tests**: Test individual components in isolation
- **Integration tests**: Test component interactions
- **UI tests**: Test critical user workflows with pytest-qt
- **Mock external dependencies**: Git operations, file system, etc.
