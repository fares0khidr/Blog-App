# TheBlog

TheBlog is a multi-user blog platform built with Django. Visitors can browse published posts, search and filter the public feed, and authenticated users can manage their own posts and drafts.

## Features

- Account registration, login, logout, and Django password hashing
- Public feed of published posts with title/content search
- Category and tag filters, newest/oldest sorting, and pagination
- Post creation, editing, and deletion for authenticated users
- Server-side ownership checks for every edit and delete operation
- Draft visibility limited to the owning user
- Django admin management for posts, categories, and tags
- Server-rendered templates with responsive plain CSS

## Technology

- Python
- Django 5.2.17
- Django ORM
- SQLite for local development
- Django Templates and static files

## Design Choices

- **Django monolith:** Django handles routing, authentication, authorization, forms, database access, and template rendering in one application. This keeps the project simple and makes server-side security rules easy to enforce.
- **Server-rendered frontend:** Django Templates and plain CSS were chosen to match the supplied design while avoiding an unnecessary frontend framework or separate API.
- **Class-based views:** Django's built-in generic views provide the standard list, detail, create, update, and delete behavior with less repeated code.
- **Built-in authentication:** Django's authentication system provides password hashing, sessions, login, logout, and the user model.
- **SQLite for development:** SQLite keeps local setup lightweight. Database access still uses the Django ORM, so a production database can be introduced later.
- **Server-side ownership checks:** Post update and delete querysets are restricted to the logged-in owner. Hiding controls in templates is not treated as authorization.

## Quick Start

Run these commands from the project root in an activated Python environment:

```cmd
conda activate djangounchainted
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

Create an administrator account when admin access is needed:

```cmd
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`.

## Routes

| Route | Access | Purpose |
| --- | --- | --- |
| `/` | Public | Browse published posts |
| `/posts/<id>/` | Public | Read a published post |
| `/accounts/signup/` | Public | Create an account |
| `/accounts/login/` | Public | Log in |
| `/accounts/logout/` | Authenticated | Log out with a CSRF-protected POST |
| `/my-posts/` | Authenticated | Manage the current user's posts and drafts |
| `/posts/new/` | Authenticated | Create a post |
| `/posts/<id>/edit/` | Owner only | Edit an owned post |
| `/posts/<id>/delete/` | Owner only | Delete an owned post |
| `/admin/` | Staff | Use the Django administration site |

The public feed accepts these query parameters:

- `q`: search title and content
- `category`: filter by category ID
- `tag`: filter by tag ID
- `sort`: use `oldest` for oldest-first ordering; the default is newest-first
- `page`: select a pagination page

Example: `/?q=django&category=1&sort=oldest&page=2`

## Data Model

- `User` is Django's built-in authentication model.
- `Post` belongs to one author, may belong to one category, and may have many tags.
- `Category` has many posts.
- `Tag` has many-to-many relationships with posts.

Schema changes must be made through Django migrations. Do not edit `db.sqlite3` manually.

## Security Rules

Authentication is required for post management and the user dashboard. The author is assigned from the logged-in user rather than from form input. Update and delete views restrict their querysets to the current user, so changing a post ID in a URL cannot bypass ownership checks. Drafts are excluded from all public views.

## Project Structure

```text
blogapp/
├── manage.py                 Django command-line entry point
├── config/                   Project settings and root URLs
├── blog/                     Models, forms, views, URLs, admin, migrations
├── templates/                Server-rendered Django templates
├── static/css/               Application stylesheet
├── docs/                     Requirements, architecture, and implementation plan
├── requirements.txt          Python dependency list
└── db.sqlite3                Local database, ignored by Git
```

The local `figma/`, `figma-designs/`, and `docs/design/` folders are visual reference material and are ignored by Git. They are not required to run the application.

## Verification

Run these checks before pushing:

```cmd
python manage.py check
python manage.py makemigrations --check
python manage.py showmigrations
python manage.py test
```

There is currently no automated test suite, so `python manage.py test` should complete with zero discovered tests. Manually verify signup, login/logout, public/draft visibility, search, filtering, sorting, pagination, dashboard ownership, CRUD operations, and admin access.

## Scope and Future Work

The current application intentionally does not include comments, likes, profiles, avatars, notifications, image uploads, a rich-text editor, an API, or deployment configuration. PostgreSQL and production deployment can be added later without changing the core Django architecture.

## Assumptions

- A post has one author and may have one category and multiple tags.
- Only published posts are public; drafts are visible to their owners through the dashboard.
- Users manage their own posts, while staff users manage content through Django admin.
- Categories and tags are maintained through the admin interface rather than a separate public management workflow.
- SQLite, `DEBUG=True`, and the local secret key are development settings and must be changed before production deployment.
- Automated tests are not included yet; the documented manual verification steps are the current validation baseline.

See [docs/requirements.md](docs/requirements.md), [docs/architecture.md](docs/architecture.md), and [docs/implementation-plan.md](docs/implementation-plan.md) for the project contract and implementation history.
