# Project Instructions

## Project Context

This repository contains a multi-user blog platform built with Django.

The project uses:

* Python
* Django
* Django Templates
* Django ORM
* Django Authentication
* SQLite during development

The frontend implementation is intentionally postponed until the provided Figma design is available and reviewed.

---

## Source of Truth

Before implementing features, read:

1. `docs/requirements.md`
2. `docs/architecture.md`
3. `docs/implementation-plan.md`

These documents describe the intended requirements, architecture, and development order.

Do not invent requirements that are not present in these documents.

If a requirement is ambiguous, explain the ambiguity before making a major architectural decision.

---

## Development Philosophy

Implement the project incrementally.

Do not attempt to build the entire application in one operation.

For each task:

1. Inspect the existing repository.
2. Read the relevant project documentation.
3. Explain the proposed changes.
4. Make the smallest reasonable implementation.
5. Run appropriate Django checks/tests.
6. Report what changed.
7. Report any remaining issues.

Prefer simple, understandable Django solutions over unnecessary abstraction.

---

## Command Execution

The developer manually runs Django, Python, Conda, migration, test, and server commands from their own CMD terminal.

Do not depend on executing commands through PowerShell or another terminal environment.

When verification is needed:

1. Explain which command the developer should run.
2. Do not install or reinstall dependencies automatically.
3. Do not change the Python/Conda environment.
4. Wait for the developer to provide the command output.
5. Use the provided output to diagnose problems and make code changes.

The developer's active environment is:

`djangounchainted`

Typical verification commands include:

```
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

If Django or another dependency appears unavailable in Copilot's own terminal environment, do not assume the project environment is broken. Ask the developer to run the relevant command in their activated CMD environment and provide the output.

---

## Django Principles

Use Django's built-in functionality whenever it is appropriate.

Prefer:

* Django ORM
* Django Forms / ModelForms
* Django Authentication
* Django Sessions
* Django Templates
* Django generic views when they make the code simpler
* Django migrations
* Django admin

Do not introduce third-party packages unless there is a clear project requirement or strong technical reason.

---

## Security

Security must be enforced server-side.

Never rely on hiding frontend buttons as an authorization mechanism.

For user-owned resources:

* verify authentication
* verify ownership
* enforce authorization before modifying or deleting data

A user must never be able to edit or delete another user's post by manually changing a URL or request.

---

## Database

Use Django migrations for schema changes.

Do not manually modify the SQLite database to implement schema changes.

When models change:

1. Create migrations.
2. Review the migration.
3. Apply the migration.
4. Run Django checks/tests.

---

## Code Quality

Prefer:

* clear names
* small functions/classes
* Django conventions
* minimal duplication
* readable code
* explicit behavior

Avoid:

* unnecessary design patterns
* unnecessary abstractions
* unnecessary dependencies
* premature optimization
* large unrelated refactors

Do not modify unrelated files while implementing a focused feature.

---

## Templates and Frontend

The frontend must eventually follow the provided Figma design.

Until the Figma implementation phase begins:

* prioritize backend functionality
* avoid spending significant time on visual styling
* do not invent a frontend design unnecessarily

---

## Testing and Verification

After meaningful changes, run the appropriate checks.

At minimum when applicable:

```bash
python manage.py check
```

For database changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

When automated tests exist:

```bash
python manage.py test
```

Do not claim a feature works without performing appropriate verification.

---

## Communication

When completing a task, report:

### Changed

List the files and major changes.

### Verified

List the commands/checks/tests that were run.

### Remaining

List known issues, assumptions, or follow-up work.

If something is uncertain, say so rather than silently guessing.

---

## Important Constraint

Do not implement future phases unless explicitly asked.

Follow the implementation plan sequentially.

The goal is to build a maintainable Django application while keeping each change understandable and verifiable.
