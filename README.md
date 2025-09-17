
# TL;DR

# SE-CV Assignment - Sharayu Rasal

**Live:** [https://sharayu1418.pythonanywhere.com/](https://sharayu1418.pythonanywhere.com/)
**Repo:** [https://github.com/Sharayu1418/SE-CV\_Assignment-Sharayu-Rasal](https://github.com/Sharayu1418/SE-CV_Assignment-Sharayu-Rasal)

**What:** Django app that renders my CV from **`data/cv_data.json`** using **`cv/templates/cv.html`**. 
No CV text is hard-coded. 
The template uses variables/loops.

Data (JSON)
Logic (`cv/views.py`)
Presentation (template). 
Projects support optional `url` links.

**Run locally**

```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1   |  macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

**Files to see**

* `data/cv_data.json` – all content
* `cv/views.py` – loads JSON → context
* `cv/templates/cv.html` – renders sections
* `cvsite/urls.py` & `cv/urls.py` – route `/`

# SE-CV Assignment - Sharayu Rasal

**Live URL:** [https://sharayu1418.pythonanywhere.com/](https://sharayu1418.pythonanywhere.com/)
**GitHub Repo:** [https://github.com/Sharayu1418/SE-CV\_Assignment-Sharayu-Rasal](https://github.com/Sharayu1418/SE-CV_Assignment-Sharayu-Rasal)

A minimal Django app that renders my CV from a **JSON file** using a **Django template** (no CV text hard-coded in HTML). The view loads `data/cv_data.json` and passes it to `cv/templates/cv.html`, which uses variables and loops to render sections (Education, Experience, Projects, Skills, Awards).

## Why this design 
  * *Data* → `data/cv_data.json`
  * *Logic* → `cv/views.py` (loads JSON, passes context)
  * *Presentation* → `cv/templates/cv.html` (Jinja/Django templating)
* **No hard-coding:** All resume content is outside the HTML; only template variables/loops are used.
* **Extensible:** Add fields in JSON → template renders them automatically.

## Tech stack
* Python **3.12**
* Django **5.2.6** (see `requirements.txt`)
* JSON data source
* Inline CSS for a clean layout
* 
## Data flow

1. `cv/views.py` reads `data/cv_data.json` (UTF-8).
2. The parsed dict is passed to `cv.html` as context (keys: `profile`, `education`, `experience`, `projects`, `skills`, `awards`).
3. `cv.html` renders with loops/conditionals (e.g., `{% for edu in education %}`).

## Local setup

### Windows (PowerShell)

```powershell
cd C:\Users\HP\Desktop\django-cv-Sharayu-Rasal
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate  # optional, silences warnings
python manage.py runserver
# open http://127.0.0.1:8000/
```

### macOS/Linux

```bash
cd SE-CV_Assignment-Sharayu-Rasal
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate  # optional
python manage.py runserver
```

## Deployment (PythonAnywhere)

Deployed at **[https://sharayu1418.pythonanywhere.com/](https://sharayu1418.pythonanywhere.com/)**

Steps used:

1. **Consoles → Bash**

   ```bash
   git clone https://github.com/Sharayu1418/SE-CV_Assignment-Sharayu-Rasal.git
   cd SE-CV_Assignment-Sharayu-Rasal
   python3.12 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Web → Add a new web app → Manual → Python 3.12**
3. **Virtualenv**: `/home/sharayu1418/SE-CV_Assignment-Sharayu-Rasal/.venv`
4. **WSGI config**:

   ```python
   import os, sys
   project_path = os.path.expanduser('~/SE-CV_Assignment-Sharayu-Rasal')
   if project_path not in sys.path:
       sys.path.insert(0, project_path)
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cvsite.settings')
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
5. In `cvsite/settings.py`:

   ```python
   ALLOWED_HOSTS = ["127.0.0.1", "localhost", "sharayu1418.pythonanywhere.com"]
   ```
6. **Reload** from the Web tab.


## Extras I implemented

## Troubleshooting

* **DisallowedHost**: ensure your domain is in `ALLOWED_HOSTS`.
* **TemplateDoesNotExist (`cv.html`)**: file must be at `cv/templates/cv.html`.
* **JSONDecodeError**: fix commas/quotes in `data/cv_data.json`.
* **500 error on PythonAnywhere**: check **Error log** in the Web tab; confirm WSGI `project_path` and virtualenv path.


## License

MIT (see `LICENSE`).
