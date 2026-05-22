
![Alt Text](images/tempo_dashboard)
============================================================

CLONE REPOSITORY ============================================================

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git cd YOUR_REPO

Replace YOUR_USERNAME and YOUR_REPO with your GitHub details.

============================================================ 2. CREATE VIRTUAL ENVIRONMENT

WINDOWS: python -m venv venv venv\Scripts\activate

MAC / LINUX: python3 -m venv venv source venv/bin/activate

============================================================ 3. INSTALL DEPENDENCIES

pip install -r requirements.txt

============================================================ 4. RUN DATABASE MIGRATIONS

python manage.py migrate

If successful you will see "OK" for each migration.

============================================================ 5. START DEVELOPMENT SERVER

python manage.py runserver

Open in browser: http://127.0.0.1:8000

Expected response: { "status": "ok", "message": "TEMPO Dashboard Running" }

============================================================ PROJECT STRUCTURE

project/ ├── config/ │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── dashboard/ │ ├── views.py │ └── urls.py ├── manage.py ├── requirements.txt ├── Procfile └── runtime.txt

============================================================ LOCAL DEVELOPMENT COMMANDS

Start server: python manage.py runserver

Create migrations: python manage.py makemigrations

Apply migrations: python manage.py migrate

Create admin user: python manage.py createsuperuser

============================================================ GIT WORKFLOW

git init git add . git commit -m "initial commit" git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git git branch -M main git push -u origin main

============================================================ DEPLOY TO RENDER
Go to https://render.com
Create New Web Service
Connect GitHub repo

BUILD COMMAND: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input

START COMMAND: gunicorn config.wsgi

============================================================ ENVIRONMENT VARIABLES (RENDER)

DEBUG = False SECRET_KEY = change-me-later ALLOWED_HOSTS = *

============================================================ COMMON ISSUES

Virtual environment not activated: Windows: venv\Scripts\activate Mac/Linux: source venv/bin/activate

Port already in use: python manage.py runserver 8001

Procfile must NOT be Procfile.txt Must be named exactly: Procfile

============================================================ NEXT STEPS
Add PostgreSQL database
Add API endpoints
Add maps (Leaflet)
Add charts (Plotly)
Add TEMPO ingestion pipeline
Add filtering and sorting
============================================================ STACK

Backend: Django Frontend: Django Templates or React Database: SQLite → PostgreSQL Hosting: Render Storage: Cloudflare R2

============================================================ DONE

Your app will run at: https://your-app-name.onrender.com