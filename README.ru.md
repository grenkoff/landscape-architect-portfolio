# Портфолио ландшафтного архитектора

Двуязычный (русский/английский) сайт-портфолио для ландшафтного архитектора на Django.

## Возможности

- **Лендинг** — hero-секция, о себе, услуги, избранные проекты
- **Портфолио** — галерея проектов, фильтрация по категориям, лайтбокс
- **Двуязычность** — русский и английский с переключателем языка (django-modeltranslation)
- **Админка Django** — управление контентом: редактирование страниц, загрузка изображений, переводы
- **SEO** — sitemap.xml, robots.txt, hreflang, canonical URL, Open Graph, JSON-LD Schema.org, верификация Яндекс/Google
- **Современный дизайн** — Tailwind CSS, Alpine.js, GLightbox, адаптивная вёрстка (mobile-first)
- **Готов к продакшену** — Cloudinary для медиа, WhiteNoise для статики, Gunicorn, PostgreSQL

## Технологии

| Компонент | Технология |
|---|---|
| Backend | Python 3.12, Django 5.1 |
| База данных | PostgreSQL (продакшен), SQLite (разработка) |
| Переводы | django-modeltranslation |
| CSS | Tailwind CSS (CDN) |
| JS | Alpine.js (CDN), GLightbox |
| Медиа | Cloudinary |
| Статика | WhiteNoise |
| Хостинг | Railway |

## Локальная разработка

```bash
# Клонировать репозиторий
git clone https://github.com/grenkoff/landscape-architect-portfolio.git
cd landscape-architect-portfolio

# Создать виртуальное окружение и установить зависимости
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Настроить переменные окружения
cp .env.example .env

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser

# Запустить сервер разработки
python manage.py runserver
```

Сайт: http://localhost:8000/ru/ (русский) или http://localhost:8000/en/ (английский)

Админка: http://localhost:8000/ru/admin/

## Тесты

```bash
python manage.py test apps
```

## Линтер

```bash
ruff check .
ruff format .
```

## Деплой (Railway)

1. Создать проект на Railway и добавить PostgreSQL
2. Подключить GitHub-репозиторий для авто-деплоя
3. Настроить переменные окружения в Railway:
   - `DJANGO_SETTINGS_MODULE=config.settings.production`
   - `SECRET_KEY` — сгенерировать случайный ключ
   - `ALLOWED_HOSTS` — ваш домен
   - `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
4. Создать суперпользователя:
   ```bash
   railway run python manage.py createsuperuser
   ```

## Структура проекта

```
├── config/                 # Настройки Django
│   └── settings/           # Разделённые настройки (base/dev/prod)
├── apps/
│   ├── core/               # Главная страница, настройки сайта, SEO
│   └── portfolio/          # Проекты, категории, галерея
├── templates/              # HTML-шаблоны
├── static/                 # CSS, JS, изображения
├── locale/                 # Переводы (ru, en)
├── Procfile                # Конфигурация Railway/Gunicorn
└── pyproject.toml          # Зависимости и инструменты
```

## Лицензия

[MIT](LICENSE)
