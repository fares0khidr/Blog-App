# Blog Platform Architecture

## 1. Architecture Overview

The application will use Django as a monolithic web framework with
server-rendered Django Templates.

The initial architecture consists of:

- Django
- Django Templates
- Django ORM
- Django Authentication
- SQLite

The frontend implementation will be developed after the provided Figma
design is available.

---

## 2. High-Level Request Flow

A typical request follows this flow:

Browser
    ↓
Django URL routing
    ↓
View
    ↓
Forms / Authentication / ORM
    ↓
Database
    ↓
View
    ↓
Django Template
    ↓
HTML response
    ↓
Browser

---

## 3. Project Structure

The project will initially contain one main Django application.

django-blog/
│
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
│
├── static/
│
├── docs/
│   ├── requirements.md
│   └── architecture.md
│
└── db.sqlite3

---

## 4. Django Application

The `blog` application will contain the core blog functionality.

Responsibilities include:

- Blog post management
- Categories
- Tags
- Post forms
- Post views
- Post URLs
- Post ownership checks
- Blog-related templates

Django's built-in authentication system will be used for users,
authentication, sessions, and password management.

---

## 5. Data Model

### User

Django's built-in User model will be used.

A user can own multiple posts.

Relationship:

User 1 ──── * Post

---

### Post

A post contains:

- title
- content
- author
- category
- created_at
- updated_at
- published

The author relationship identifies the owner of the post.

---

### Category

A category contains:

- name

A category can contain multiple posts.

Relationship:

Category 1 ──── * Post

---

### Tag

A tag contains:

- name

A post can have multiple tags, and a tag can belong to multiple posts.

Relationship:

Post * ──── * Tag

---

## 6. Authentication

Django's built-in authentication system will handle:

- Registration
- Login
- Logout
- Password hashing
- User sessions

Authenticated requests will expose the current user through Django's
request authentication system.

---

## 7. Authorization

Authentication and authorization are separate concerns.

Authentication answers:

"Who is this user?"

Authorization answers:

"Is this user allowed to perform this action?"

For post modification:

- An authenticated user may create a post.
- Only the post owner may edit the post.
- Only the post owner may delete the post.

These rules must be enforced on the server.

Hiding buttons in the frontend is not considered sufficient authorization.

---

## 8. Views

The application will provide views for:

- Public post list
- Post detail
- User dashboard
- Create post
- Edit post
- Delete post
- Authentication pages

Django's generic class-based views may be used where they simplify
standard CRUD operations.

---

## 9. Forms

Django Forms / ModelForms will be used for model-backed user input.

The initial post form will handle:

- title
- category
- content
- published status

Validation will be performed server-side.

---

## 10. Database

SQLite will be used during development.

Database schema changes will be managed exclusively through Django
migrations.

The database will not be manually modified.

---

## 11. Frontend

The frontend implementation is intentionally postponed until the
provided Figma design has been reviewed.

Once the design is available, templates, CSS, and any required
JavaScript will be implemented according to the design.

---

## 12. Architecture Principles

The project should follow these principles:

1. Keep the architecture simple.
2. Use Django's built-in functionality where appropriate.
3. Use the Django ORM instead of manually writing SQL for normal
   application operations.
4. Keep authentication and authorization separate.
5. Enforce permissions on the server.
6. Avoid unnecessary dependencies.
7. Make small, testable changes.
8. Do not introduce technologies that are not required by the project.
9. Keep documentation synchronized with significant architectural
   decisions.