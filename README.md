# Landscape Architect Portfolio

A bilingual (Russian/English) portfolio website for a landscape architect, built with Django.

## Features

- **Landing page** with hero section, about, services, and featured projects
- **Portfolio** with project gallery, category filtering, and lightbox
- **Bilingual** — Russian and English with language switcher (django-modeltranslation)
- **Django Admin** — full content management: edit pages, upload images, manage translations
- **SEO** — sitemap.xml, robots.txt, hreflang, canonical URLs, Open Graph, JSON-LD Schema.org, Yandex/Google verification
- **Modern design** — Tailwind CSS, Alpine.js, GLightbox, responsive (mobile-first)
- **Production-ready** — Cloudinary media storage, WhiteNoise static files, Gunicorn, PostgreSQL

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python 3.12, Django 5.1 |
| Database | PostgreSQL (production), SQLite (development) |
| Translations | django-modeltranslation |
| CSS | Tailwind CSS (CDN) |
| JS | Alpine.js (CDN), GLightbox |
| Media Storage | Cloudinary |
| Static Files | WhiteNoise |
| Hosting | Railway |

## Local Development

```bash
# Clone the repository
git clone https://github.com/grenkoff/landscape-architect-portfolio.git
cd landscape-architect-portfolio

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Set up environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Open http://localhost:8000/ru/ (Russian) or http://localhost:8000/en/ (English).

Admin panel: http://localhost:8000/ru/admin/

## Testing

```bash
python manage.py test apps
```

## Linting

```bash
ruff check .
ruff format .
```

## Deployment (Railway)

1. Create a Railway project and add a PostgreSQL plugin
2. Connect the GitHub repository for auto-deploy
3. Set environment variables in Railway dashboard:
   - `DJANGO_SETTINGS_MODULE=config.settings.production`
   - `SECRET_KEY` — generate a random secret key
   - `ALLOWED_HOSTS` — your domain(s)
   - `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
4. Create a superuser via Railway CLI:
   ```bash
   railway run python manage.py createsuperuser
   ```

## Project Structure

```
├── config/                 # Django project settings
│   └── settings/           # Split settings (base/dev/prod)
├── apps/
│   ├── core/               # Home page, site settings, SEO
│   └── portfolio/          # Projects, categories, gallery
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── locale/                 # Translations (ru, en)
├── Procfile                # Railway/Gunicorn config
└── pyproject.toml          # Dependencies and tooling
```

## License

[MIT](LICENSE)
