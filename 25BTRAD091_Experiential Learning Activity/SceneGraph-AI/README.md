# SceneGraph AI

**A production-planning workspace for screenplay teams.**

SceneGraph AI turns Fountain screenplays into structured scene data, maps relationships between scenes, helps teams review continuity, and builds filming schedules. It includes a browser-based frontend and a Python API.

## Contents

- [Features](#features)
- [Technology](#technology)
- [Run locally](#run-locally)
- [Configuration](#configuration)
- [Tests](#tests)
- [Deployment](#deployment)
- [Project structure](#project-structure)
- [Scope and limitations](#scope-and-limitations)

## Features

- Import Fountain (`.fountain`) or UTF-8 text scripts and review structured scenes.
- Manage production projects, scene details, cast, locations, and availability.
- Explore scene relationships in an interactive graph.
- Review continuity warnings based on manually recorded annotations.
- Create and revise single-crew schedules using cast and location constraints.
- Track shoot progress and view production metrics.
- Export project data in supported formats.
- Keep project data in a local SQLite database or configure PostgreSQL for a hosted deployment.

## Technology

- **Backend:** Python, FastAPI, SQLAlchemy
- **Frontend:** HTML, CSS, and JavaScript in `docs/`
- **Data and algorithms:** SQLite/PostgreSQL, NetworkX, NumPy, and SciPy
- **Tests:** pytest
- **Hosting template:** Render (`render.yaml`)

## Run locally

### Windows: quick start

Open PowerShell or Command Prompt in the `SceneGraph-AI` project folder and run:

```powershell
.\run_windows.bat
```

The launcher creates a `.venv` if needed, checks for FastAPI and Uvicorn, installs runtime dependencies if they are missing, starts the app, and opens the local page. Keep the terminal open while using the app; press **Ctrl+C** to stop it.

> The convenience launcher binds to `0.0.0.0`, so other devices on your local network may be able to reach it. For localhost-only access, use the manual commands below.

### Windows: localhost-only

Requires Python 3.11 or newer and the Python launcher (`py`):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### macOS and Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Once the server is running:

- App: <http://127.0.0.1:8000/>
- API health: <http://127.0.0.1:8000/api/health>
- Interactive API docs: <http://127.0.0.1:8000/docs>

The local database is created as `scenegraph.db` when `DATABASE_URL` is not set. This file is ignored by Git and stays on your computer.

## Configuration

The app reads configuration from environment variables provided to the Python process or hosting service. The repository does not automatically load a `.env` file.

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | SQLAlchemy database connection. Defaults to local SQLite; use PostgreSQL for a hosted deployment. |
| `CORS_ORIGINS` | Allowed browser origins when the frontend and API are hosted separately. |
| Firebase, Google, email, and Twilio variables | Optional authentication and messaging integrations; see `.env.example` for the supported variable names. |

Keep passwords, database connection strings, and provider secrets out of Git. The Firebase web configuration in `docs/config.js` is client-side and visible to users; never put private credentials there.

## Tests

Install the development dependencies and run the test suite from the project folder:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

GitHub Actions runs the tests on pushes and pull requests.

## Deployment

GitHub Pages can serve the static frontend, but it cannot run the Python API or host the database. A public deployment needs:

1. A Python web service, such as Render, to run FastAPI.
2. A persistent PostgreSQL database for hosted data.
3. The frontend configured to call the deployed API.

This repository includes a Render blueprint in `render.yaml`. Set `DATABASE_URL` and, where needed, `CORS_ORIGINS` as private service environment variables. For the complete setup and verification steps, see [the deployment guide](documentation/DEPLOY_GITHUB_PAGES.md).

## Project structure

```text
SceneGraph-AI/
├── app.py                 FastAPI application and API routes
├── models.py              SQLAlchemy data models and database setup
├── project_service.py     Project and production data operations
├── core/                  Parsing, graph, continuity, scheduling, and analytics
├── data/                  Sample screenplay and parser/continuity fixtures
├── docs/                  Static web frontend
├── tests/                 Automated tests
├── documentation/         Architecture and deployment guides
├── .github/workflows/     Continuous integration
├── requirements.txt       Runtime dependencies
└── requirements-dev.txt   Runtime and test dependencies
```

## Scope and limitations

The screenplay parser is rule-based, not a general story-understanding model. Continuity checks depend on annotations entered by the production team. Generated schedules are planning aids; review them against real production requirements before use.
