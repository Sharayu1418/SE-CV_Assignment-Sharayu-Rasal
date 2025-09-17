

# SE-CV Assignment — Sharayu Rasal

**Live (GitHub Pages):** [https://sharayu1418.github.io/SE-CV\_Assignment-Sharayu-Rasal/](https://sharayu1418.github.io/SE-CV_Assignment-Sharayu-Rasal/)
**Live (PythonAnywhere):** [https://sharayu1418.pythonanywhere.com/](https://sharayu1418.pythonanywhere.com/)
**Repo:** [https://github.com/Sharayu1418/SE-CV\_Assignment-Sharayu-Rasal](https://github.com/Sharayu1418/SE-CV_Assignment-Sharayu-Rasal)


Django app that renders my CV from a JSON file using a Django template. No resume text is hard-coded into the HTML. The view loads `data/cv_data.json` and passes it to `cv/templates/cv.html`, which uses variables/loops to build the page (Education, Experience, Projects, Skills, Awards).

**Structure (separation of concerns)**

* **Data:** `data/cv_data.json`
* **Logic:** `cv/views.py` (reads JSON, builds context)
* **Presentation:** `cv/templates/cv.html` (templating with loops/conditionals)

> I also committed a static snapshot as `index.html` at the repo root so you can see the CV directly on GitHub/Pages without running a server.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
# http://127.0.0.1:8000/
```

## Files worth a quick look

* `data/cv_data.json` — all content lives here
* `cv/views.py` — loads JSON → passes context to the template
* `cv/templates/cv.html` — renders sections with loops/conditions
* `cvsite/urls.py` and `cv/urls.py` — route `/` to the CV view
* `index.html` — static snapshot of the rendered CV (for graders)

* Clean separation of data/logic/presentation.
* Easy to extend: update the JSON → the page updates (e.g., projects support optional `url`/`code` links).
* Avoids hard-coding resume text inside HTML or Python.

## Deployment (PythonAnywhere)

* Web app: **Manual** (Python 3.12)
* Virtualenv: `/home/sharayu1418/SE-CV_Assignment-Sharayu-Rasal/.venv`
* WSGI sets `DJANGO_SETTINGS_MODULE=cvsite.settings` and adds the project path to `sys.path`.
* `ALLOWED_HOSTS` includes `sharayu1418.pythonanywhere.com`.

## Note about viewing on GitHub

When you click `index.html` inside the repo, GitHub shows the **source** (not a live render). To see it rendered, use **GitHub Pages**:
`https://sharayu1418.github.io/SE-CV_Assignment-Sharayu-Rasal/`
(or the Django demo on **PythonAnywhere** linked at the top).

## Troubleshooting (quick)

* **DisallowedHost** → add your domain to `ALLOWED_HOSTS`.
* **TemplateDoesNotExist (cv.html)** → ensure the file is at `cv/templates/cv.html`.
* **JSONDecodeError** → fix commas/quotes in `data/cv_data.json`.

License: MIT (see `LICENSE`).

