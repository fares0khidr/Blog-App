# Blog Platform Requirements

## 1. Project Goal

Build a multi-user personal blog platform using Django.

Each registered user can manage their own blog posts, while published posts can be viewed publicly.

---

## 2. Users

The system must support:

- User registration
- User login
- User logout
- Secure password handling through Django's authentication system

---

## 3. Blog Posts

Each post should have:

- Title
- Content
- Author
- Category
- Publication date
- Updated date
- Published status

Users must be able to:

- Create their own posts
- View their own posts
- Edit their own posts
- Delete their own posts

A user must not be able to edit or delete another user's post.

---

## 4. Categories

Posts can belong to categories.

Users should be able to:

- Create/select categories as appropriate
- Associate posts with categories
- Filter posts by category

---

## 5. Tags

Posts should support tags.

Tags can be associated with multiple posts.

---

## 6. Public Blog

Visitors should be able to:

- View published posts
- Open an individual post
- Search posts by title
- Filter by category
- Filter/sort by date
- Navigate through paginated results

---

## 7. User Dashboard

Authenticated users should have a dashboard where they can:

- View their posts
- Create a post
- Edit their posts
- Delete their posts

---

## 8. Security

The application must enforce permissions on the server side.

Users must only be allowed to modify or delete posts that they own.

Authentication-protected functionality must require an authenticated user.

---

## 9. Database

The application will use Django ORM.

Development database:

- SQLite

Core entities:

- User
- Post
- Category
- Tag

---

## 10. Frontend

The frontend will implement the provided Figma design.

Frontend implementation will be handled after the backend foundation is complete.

---

## 11. Technology

- Python
- Django
- Django ORM
- SQLite
- HTML/CSS/JavaScript as required by the selected frontend approach

---

## 12. Non-Goals for the Initial Version

The following are optional and will not block the core implementation:

- Comments
- Image uploads
- Rich text editor
- Deployment
- Automated tests
- PostgreSQL 