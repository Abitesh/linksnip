# LinkSnip 🔗

A simple URL shortener built with Django.

Paste a long URL, get a short code, and anyone visiting that short link will be redirected to the original URL. The app also keeps track of how many times each short link was clicked.

This project is mainly for learning Django fundamentals and building a small, end‑to‑end backend service.

---

## Features

- Shorten long URLs into simple codes  
- Redirect short codes to original URLs  
- Track click counts for each short URL  
- Recent links table on the home page  
- Separate page to list all links  

---

## Tech Stack

- **Backend:** Django 6  
- **Database:** SQLite (default Django DB)  
- **Frontend:** HTML, CSS (no frontend framework)  
- **Language:** Python 3  

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Abitesh/linksnip.git
cd linksnip
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS 
# venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open your browser and go to:

```text
http://127.0.0.1:8000/
```

---

## How It Works

### Home page (`/`)

- Shows a form where you can paste a URL.
- On submit, the app:
  - Validates the URL using a simple Django form.
  - Creates (or reuses) a `ShortURL` entry in the database.
  - Generates a unique short code the first time a URL is seen.
- The page then displays your new short link and a table of the 10 most recent links.

### Redirects (`/<code>/`)

- When you visit a short URL like `/abc123/`, the app:
  - Looks up the matching `ShortURL` by `short_code`.
  - Increments its `clicks` counter.
  - Redirects you to the original URL.

### All links (`/links/`)

- Shows a table of all stored links with:
  - Short code  
  - Original URL  
  - Click count  
  - Created date  

---

## Running Tests

There are a few basic tests to make sure the model and views behave as expected.

```bash
python manage.py test
```

---

## Project Structure

```text
linksnip/
├── manage.py
├── linksnip/                  # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── shortener/                 # Main app
    ├── models.py              # ShortURL model
    ├── views.py               # Views for home, redirect, list
    ├── forms.py               # URL form
    ├── urls.py                # App routes
    ├── templates/shortener/   # HTML templates
    │   ├── base.html
    │   ├── home.html
    │   └── list.html
    └── static/shortener/      # CSS
        └── style.css
```

---

## Ideas for Future Improvements

This project is intentionally simple, but there are many ways to extend it:

- User accounts and login so each user can see only their own links  
- Custom short codes (user chooses the code if available)  
- Link expiration after a certain date  
- More detailed analytics (clicks per day, referrers, etc.)  
- Switching from SQLite to PostgreSQL for production use  

---

## Disclaimer

This project is for learning purposes and local use only.  
It is **not** optimized for production or high‑traffic environments.
