# Architecture

## Overview

TheBlog is a small Django monolith. Django owns URL routing, authentication, authorization, form validation, ORM access, template rendering, and static-file integration. The application is intentionally server-rendered: there is no separate frontend service or API layer.

```text
Browser
  -> config.urls -> blog.urls
  -> class-based view
  -> form and/or authenticated request
  -> Django ORM
  -> SQLite (development)
  -> template + static CSS
  -> HTML response
```

This structure keeps the ownership and security rules close to the data access that enforces them.

## Repository Structure

```text
blogapp/
├── manage.py
├── config/
│   ├── settings.py       Project configuration and installed apps
│   ├── urls.py           Root URL configuration
│   ├── asgi.py           ASGI entry point
│   └── wsgi.py           WSGI entry point
├── blog/
│   ├── models.py         Post, Category, and Tag
│   ├── forms.py          Signup and post forms
│   ├── views.py          Public browsing, auth, and post CRUD
│   ├── urls.py           Application routes
│   ├── admin.py          Admin registrations
│   └── migrations/       Versioned database schema
├── templates/            Django templates grouped by feature
├── static/css/           Shared application stylesheet
└── docs/                 Requirements, architecture, and plan
```

Local visual references under `docs/design/`, `figma/`, and `figma-designs/` are excluded from version control. The runtime uses `templates/` and `static/css/style.css`.

## Responsibilities

### `config`

The project configuration registers Django's built-in apps and the `blog` app, configures the SQLite database, exposes the project template directory, and includes the application URL configuration at the site root.

### `blog.models`

The data model uses Django's built-in user model:

```text
User 1 ---- * Post
Category 1 ---- * Post
Post * ---- * Tag
```

`Post.author` is required and cascades when a user is deleted. `Post.category` is optional and is set to `NULL` if its category is removed. Tags are optional and use a many-to-many relationship.

### `blog.forms`

`SignUpForm` extends Django's `UserCreationForm`. `PostForm` exposes only post content fields; the author is never accepted from the browser and is assigned in `PostCreateView` from `request.user`.

### `blog.views`

- `PublishedPostListView` returns published posts and applies search, category/tag filtering, sorting, and pagination.
- `PublishedPostDetailView` can resolve only published posts.
- `MyPostsView` returns only posts owned by the authenticated user.
- `PostCreateView` requires authentication and assigns ownership server-side.
- `OwnedPostMixin` scopes update and delete querysets to the authenticated owner.
- `UserLoginView`, `UserLogoutView`, and `SignUpView` use Django authentication primitives.

### Templates and static files

Templates are grouped into shared layout, registration, and blog pages. `templates/base.html` owns the shared navigation and loads `static/css/style.css`. The visual design is a functional responsive interpretation of the supplied reference material.

## Request and Authorization Flow

Public list and detail views always start from `published=True`, so drafts cannot leak through search, filters, pagination, or direct URLs. Authenticated views use `LoginRequiredMixin`. Mutation views use the current user's identity from the request, and `OwnedPostMixin` narrows the update/delete queryset before Django resolves the object. A missing or foreign object therefore receives Django's normal not-found response rather than being modified.

Logout is a POST action protected by Django's CSRF middleware. Password storage and sessions are handled by Django's authentication system.

## Database and Migrations

SQLite is the development database. Every schema change must be represented by a migration in `blog/migrations/`. The database file is local and ignored by Git. Use `makemigrations`, review the generated migration, then run `migrate`; never edit the SQLite file manually.

## Operational Conventions

- Keep domain behavior in the `blog` app and use Django's built-in APIs first.
- Keep authorization server-side; template visibility is only a usability concern.
- Keep the dependency list minimal.
- Use the project README for setup and manual verification.
- Add automated tests as behavior grows, especially for ownership and public draft isolation.

## Current State

The backend foundation, authentication, post CRUD, ownership enforcement, public discovery features, dashboard, templates, and responsive styling are implemented. The remaining quality gap is automated test coverage; deployment hardening and a production database are intentionally outside the current scope.
