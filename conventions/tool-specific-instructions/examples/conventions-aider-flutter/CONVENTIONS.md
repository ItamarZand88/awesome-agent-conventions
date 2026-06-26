<!-- source: conventions-aider-flutter — https://raw.githubusercontent.com/Aider-AI/conventions/main/flutter/CONVENTIONS.md -->
# Flutter Development Conventions

These conventions are designed to ensure a maintainable, readable, and scalable Flutter codebase using the following stack and patterns:
- GetX for state management and navigation
- Dio for HTTP requests
- Material Design 3 for UI (as default)
- Functional programming principles
- Short, modular, and reusable functions
- Clean, readable, and maintainable code

---

## 1. Separation of Concerns

- **UI Layer**: Widgets only handle presentation logic. No business logic or direct state manipulation.
- **Controller Layer (GetX Controllers)**: All business logic, state management, and API calls are handled in GetX Controllers.
- **Data Layer**: Data fetching, storage, and transformation logic (repositories, services).
- **Routing Layer**: All navigation must be performed using GetX’s routing system.

---

## 2. Folder Structure (GetX Pattern)

```plaintext
/lib
  /core
    /theme             # Theme management
    /utils             # Common utilities, extensions, helpers
    /network           # Dio client and API interceptors, etc.
  /data
    /models            # Data models
    /repositories      # Data repositories
  /modules
    /feature_name
      /controllers     # GetX Controllers
      /views           # Screens/widgets
      /bindings        # GetX Bindings for dependency injection
      /widgets         # Feature-specific widgets
  /routes
    app_pages.dart     # App routes using GetX
  main.dart
```

- Each feature/module is self-contained, using GetX’s modular pattern.

---

## 3. State Management (GetX)

- Use GetX Controllers for all state and business logic.
- Controllers must be kept lean; delegate logic to services/repositories where possible.
- Use `Obx`/`GetBuilder` only in the UI layer.
- Dispose controllers properly to avoid memory leaks.

---

## 4. Theme Management

- Default to Material Design 3 (use `ThemeData(useMaterial3: true)`).
- Centralize all theme and color definitions in `/core/theme`.
- Use GetX to manage dynamic themes (light/dark/system).

---

## 5. HTTP Requests (Dio)

- Configure a single Dio client in `/core/network`.
- Use interceptors for logging, error handling, auth, etc.
- All HTTP requests must go through repositories in `/data/repositories`.
- Never call Dio directly from controllers or widgets.

---

## 6. Functional Programming Principles

- Prefer pure functions and stateless widgets where possible.
- Avoid shared mutable state.
- Use extension methods for utility logic.
- Functions should be short, modular, and reusable; break down complex logic.

---

## 7. Code Quality

- **Short Functions:** Each function should do one thing. Prefer functions under 20 lines.
- **Modular:** Isolate features, logic, and utilities for reuse and testability.
- **Clean Code:** Use descriptive names, avoid magic numbers, document complex logic inline.
- **Readability:** Consistent formatting, avoid deep nesting, prefer early returns.

---

## 8. UI Guidelines

- Default to Material Design 3 widgets.
- Avoid third-party UI libraries unless necessary.
- Keep widgets stateless unless local state is required.
- Use custom widgets for repeated UI patterns.

---

## 9. Example: Feature Module Structure

```plaintext
/modules/todo/
  controllers/
    todo_controller.dart
  views/
    todo_list_view.dart
    todo_detail_view.dart
  bindings/
    todo_binding.dart
  widgets/
    todo_item.dart
```

---

## 10. Example: Short Modular Functions

```dart
// Bad: long, multi-purpose function
void fetchAndDisplayTodos() {
  // fetch from API, transform, update UI
}

// Good: short, reusable functions
Future<List<Todo>> fetchTodos() { ... }
List<Todo> filterTodos(List<Todo> todos, String query) { ... }
Widget buildTodoList(List<Todo> todos) { ... }
```

---

## 11. References

- [GetX Documentation](https://pub.dev/packages/get)
- [Dio Documentation](https://pub.dev/packages/dio)
- [Material 3 Guidelines](https://m3.material.io/)
