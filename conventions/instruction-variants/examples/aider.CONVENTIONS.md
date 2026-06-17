<!-- source: aider — https://raw.githubusercontent.com/Aider-AI/conventions/main/golang/CONVENTIONS.md -->
# Go (Golang) Development Conventions

These conventions ensure a scalable, maintainable, and clean Go codebase that prioritizes simplicity, modularity, and readability. They integrate modern Go best practices, including concurrency, error management, and project organization.

---

## 1. Project Structure

Use the following pattern for scalable Go applications:

```plaintext
/cmd
  /<appname>     # Main application entrypoint(s), minimal logic (calls /internal)
/internal
  /<module>      # Each domain or feature as a separate module
    handlers.go
    service.go
    repository.go
    model.go
/pkg
  /utils         # Utility functions/libraries for use across modules
  /vector        # Vector computation helpers (prefer vector ops over loops)
/errors
  errors.go      # Centralized error definitions and handling
/logging
  logger.go      # Centralized logging setup and helpers
```

- Place only the main entrypoint in `/cmd/<appname>/main.go`.
- Keep all implementation logic within `/internal` modules.
- Use `/pkg` for shared libraries and utilities.
- All error handling and logging are centralized.

---

## 2. Modularity & Simplicity

- **Single Responsibility:** Every file, type, and function should do one thing.
- **Short Functions:** Keep functions under 30 lines when possible.
- **Descriptive Names:** Use meaningful file, type, and function names (follow [Google Go standards](https://google.github.io/styleguide/go/decisions)).
- **No Printing/Direct Error Handling:** Never log or print errors except via centralized logging and error handling modules.

---

## 3. Concurrency

- Use goroutines and channels where suitable (for parallelism and asynchronous tasks).
- Avoid concurrency when it makes code less readable or more complex.
- Prefer vectorized computations (use slices and helper methods in `/pkg/vector`) over manual loops for data processing.
- Always document concurrent code for clarity.

---

## 4. Error Management

- **Centralize Errors:** Define all error types and helpers in `/errors/errors.go`.
- **Propagate Errors:** Always return errors to a single handling point, never handle or print errors directly in business logic.
- **Error Wrapping:** Use Go’s error wrapping (`fmt.Errorf("context: %w", err)`) for stack traces.
- **No Silent Failures:** Always check and return errors, never ignore them.

---

## 5. Logging

- **Centralized Logging:** Implement all logging in `/logging/logger.go` using a standard Go logger or a third-party package.
- Never log directly in modules; always call the logging package.
- Keep log messages meaningful and context-rich.

---

## 6. Code Quality

- **DRY:** Avoid duplication—use helpers or utility packages for repeated logic.
- **Readability:** Prefer clarity over cleverness. Add comments for complex logic.
- **Scalability:** Organize code into modules and packages so new features can be added without major refactoring.

---

## 7. Naming Conventions

- File, function, and variable names should be descriptive and follow Go’s camelCase/snake_case conventions.
- No abbreviations except common ones (ctx, err, req, resp, cfg, etc.).
- Use singular names for files and types unless a plural is more semantically correct.

---

## 8. Example: Error Handling

```go
// internal/user/service.go
func (s *Service) GetUser(ctx context.Context, id string) (*User, error) {
    user, err := s.repo.FindByID(ctx, id)
    if err != nil {
        return nil, errors.WrapUserNotFound(err, id)
    }
    return user, nil
}

// errors/errors.go
func WrapUserNotFound(err error, id string) error {
    return fmt.Errorf("user %s not found: %w", id, err)
}
```

---

## 9. Example: Vector Computation

```go
// pkg/vector/vector.go
func Add(a, b []float64) ([]float64, error) {
    if len(a) != len(b) {
        return nil, errors.New("length mismatch")
    }
    result := make([]float64, len(a))
    for i := range a {
        result[i] = a[i] + b[i]
    }
    return result, nil
}
```

---

## 10. References

- [Go Project Layout](https://github.com/golang-standards/project-layout)
- [Google Go Style Guide](https://google.github.io/styleguide/go/decisions)
- [Effective Go](https://go.dev/doc/effective_go)
