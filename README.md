# TheBlog

TheBlog is a Django blog application where registered users can create and manage their own posts. Published posts are publicly browsable, while drafts remain private to their owners.

The project includes:

- Django authentication with signup, login, and logout
- User-owned blog posts
- Categories and tags
- Published posts and private drafts
- Search by title and content
- Category and tag filtering
- Combined filtering with pagination
- A My Posts dashboard
- Django templates and responsive plain CSS

## Requirements

- Python
- Django 5.2.17
- Conda is recommended for the project environment
- SQLite for development

The project uses the existing Conda environment `djangounchainted`. An equivalent Python environment can be used if it has the dependencies listed in `requirements.txt`.

## Setup

From the project root, activate the environment:

```cmd
conda activate djangounchainted
```

Install the project dependency if needed:

```cmd
python -m pip install -r requirements.txt
```

Apply the database migrations:

```cmd
python manage.py migrate
```

Create an administrator account if one does not already exist:

```cmd
python manage.py createsuperuser
```

Run Django's system checks:

```cmd
python manage.py check
python manage.py makemigrations --check
```

Start the development server:

```cmd
python manage.py runserver
```

Open the development site at `http://127.0.0.1:8000/`.

## Important Routes

| Route | Purpose |
| --- | --- |
| `/` | Public list of published posts |
| `/my-posts/` | Authenticated user's posts, including drafts |
| `/accounts/signup/` | Create a user account |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | CSRF-protected POST logout; redirects to `/` |
| `/auth/status/` | Display the current authentication state |
| `/posts/<id>/` | Published post detail |
| `/posts/new/` | Create a post; authentication required |
| `/posts/<id>/edit/` | Edit an owned post |
| `/posts/<id>/delete/` | Confirm deletion of an owned post |
| `/admin/` | Django administration site |

The public post list accepts these GET parameters:

- `q` searches post titles and content.
- `category` filters by category ID.
- `tag` filters by tag ID.
- `page` selects a result page.

Examples:

```text
/?q=django
/?category=1&tag=2
/?q=django&category=1&tag=2&page=2
```

Search and filter parameters are preserved when navigating through public pagination.

## Authentication and Ownership

Anonymous users can browse published posts and use public search and filters. They cannot create posts or access `/my-posts/`.

Authenticated users can create posts. The author is assigned automatically from the logged-in Django user; there is no author selector in the normal post form.

Only the post owner can edit or delete a post. These checks are enforced server-side. Deletion uses a CSRF-protected POST request.

Drafts are excluded from the public list, public search and filters, and public detail pages. Owners can manage their drafts through `/my-posts/`.

Logout uses Django's authentication system, invalidates the session, and redirects to `/`.

## Project Structure

```text
blogapp/
├── manage.py                 Django command-line entry point
├── config/                   Project settings and URL configuration
├── blog/                     Blog models, forms, views, URLs, admin, migrations
├── templates/                Shared and page-specific Django templates
├── static/css/               Plain CSS served through Django static files
├── docs/                     Requirements, architecture, plan, and design source
├── db.sqlite3                Development SQLite database
└── requirements.txt          Python dependency list
```

The `blog/migrations/` directory contains Django-generated schema history. Do not edit the SQLite database manually; use Django migrations for schema changes.

## Admin

After creating a superuser, visit `/admin/` to manage existing blog data. The admin includes:

- Posts
- Categories
- Tags

## Frontend

The frontend uses server-rendered Django templates, plain CSS, and Django static files. The local visual reference is `docs/design/frontend design.pdf`. The implementation is a functional responsive interpretation of that design, not a claim of pixel-perfect reproduction.

## Development Verification

The project instructions require Django and Python commands to be run manually from the developer's activated CMD environment. Before handoff or submission, run:

```cmd
python manage.py check
python manage.py makemigrations --check
python manage.py showmigrations
python manage.py runserver
```

Manual browser checks should cover signup, login, POST logout, published/draft visibility, search, filtering, pagination, My Posts ownership, create/edit/delete, and admin access.

## Scope

The project intentionally does not include comments, likes, profiles, avatars, notifications, APIs, deployment configuration, or other features outside the documented blog requirements.
