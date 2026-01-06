# Django Portofolio (Beginner)

Portofolio sederhana menggunakan Django:
- Home / About / Projects / Contact
- Admin panel untuk mengelola Projects
- Upload Thumbnail project (media)

## Tech Stack
- Python
- Django
- SQLite (default)

## Setup (Local)
```bash
python -m venv .venv
# aktifkan venv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver