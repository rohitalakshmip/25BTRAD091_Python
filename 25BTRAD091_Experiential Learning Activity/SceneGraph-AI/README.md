# SceneGraph AI

## Full-Stack Production Intelligence Platform

**Python Programming Experiential Learning · Five-member team · AI & Data Engineering**

SceneGraph AI is a working, full-stack, multi-user web application for screenplay production planning. It converts Fountain screenplays into structured records, analyzes scene relationships, checks annotated continuity, builds single-crew filming schedules, and measures scheduling results.

The application has a custom cinematic HTML/CSS/JavaScript frontend. **It does not use Streamlit.**

## Architecture

```text
GitHub Pages (static docs/ files)          Render Web Service (FastAPI/Python)
+----------------------------------+       +----------------------------------+
| index.html / styles.css          | HTTPS | Authentication + private API     |
| app.js / config.js               | ----> | Fountain parser + normalization  |
| Auth, graph, timeline, metrics,  | Bearer| Graph, continuity, scheduler     |
| and exports                      | token | Baseline, benchmarks, PDF        |
+----------------------------------+       +----------------+-----------------+
                                                          |
                                               Private SQL connection
                                                          |
                                       Managed PostgreSQL (e.g., Supabase)
                                       Users, sessions, projects, scenes,
                                       locations, cast, annotations, audit
```

For local development, FastAPI serves the same frontend and stores records in an SQLite file. For a hosted deployment, set `DATABASE_URL` to a managed **PostgreSQL** database so records persist across backend restarts. The frontend never receives the database password or connection string.

## Features

### Accounts and project data

- Email/password sign-up, sign-in, and sign-out.
- Password hashing with PBKDF2-SHA256 and revocable, expiring sessions.
- Per-account project isolation.
- SQLAlchemy storage for users, projects, locations, actors, scene/cast relationships, annotations, scheduling settings, schedule results, and audit events.
- Create and switch between projects, edit records, and delete projects with confirmation.
- Each new account receives a sample 12-scene production.

### Screenplay and continuity

- Import UTF-8 `.fountain` or `.txt` screenplays, parse them, and validate the resulting structure.
- Edit cast, scene metadata, and durations.
- Explore an interactive, source-linked scene knowledge graph.
- Check manually annotated prop continuity in **story order**.

### Scheduling and analytics

- Generate feasible single-crew schedules using actor and location constraints and 30-minute time slots.
- Optimize schedules with priority-aware SciPy MILP. Google OR-Tools CP-SAT is optional and must be installed separately.
- Use a transparent fallback when an optimizer is unavailable.
- Change actor or location availability and replan.
- Review metrics and solver status; stale schedule output is invalidated.
- Run synthetic benchmark experiments with fixed seeds and the same hard constraints for greedy and optimized methods.

### Exports and tests

- Export authenticated JSON, CSV, and PDF files based on the current persisted project data.
- Integration tests cover login, data isolation, import, graph, scheduling, replanning, storage, and exports.
- A GitHub Actions workflow runs tests.

> **Technical limitations:** The parser is rule-based, and continuity warnings require human annotations. The application does not claim general story understanding or unsupported machine-learning prediction accuracy. A scheduled scene is a production-planning estimate, not a safety guarantee.

## Run locally

### Windows

1. Install Python 3.11 or later.
2. Open the `SceneGraph-AI` folder in VS Code and open **Terminal → New Terminal**.
3. Create a virtual environment and install the dependencies:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

4. Start the application:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
   ```

5. Visit **http://127.0.0.1:8000/**. Select **Create an account**, register with your email address and a strong password, then sign in.
6. Open **Production planner → Generate optimized schedule**. You can also block an actor on a scheduled day and replan.

The local database is saved in `scenegraph.db` and is not tracked by Git.

### macOS and Linux

From the `SceneGraph-AI` folder, run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### Troubleshooting

If your browser says **“site can't be reached”**, check that:

- The terminal is still running the application.
- You are in the `SceneGraph-AI` project folder.
- The application is using port `8000`.
- Dependencies were installed in the same Python environment used to start the application.

The address `http://127.0.0.1:8000` is available only on the same computer.

## Publish a public website

> **GitHub Pages alone cannot run Python or a database.** It hosts the static frontend; Render (or another Python hosting service) runs FastAPI, and PostgreSQL stores the data. See [DEPLOY_GITHUB_PAGES.md](documentation/DEPLOY_GITHUB_PAGES.md) for detailed setup instructions.

### Deployment steps

1. Push the complete project, including hidden `.github/` files and `docs/`, to a GitHub repository. Do not commit `.env`, `scenegraph.db`, or passwords.
2. Create a persistent managed PostgreSQL database. The Supabase **Session Pooler** works with IPv4-only hosting. Copy its connection URI and keep it private.
3. Deploy a **Python Web Service** on Render using the repository. Set `DATABASE_URL` privately and set `CORS_ORIGINS=https://YOUR_USERNAME.github.io`. Use this start command:

   ```text
   uvicorn app:app --host 0.0.0.0 --port $PORT
   ```

4. Check that `https://YOUR-API.onrender.com/api/health` reports `ok: true`.
5. Edit `docs/config.js` and set `window.SCENEGRAPH_API_BASE = "https://YOUR-API.onrender.com";`. This must be an HTTPS URL, not a secret.
6. In the GitHub repository, open **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/docs`, then save. Visit the generated GitHub Pages URL and register an account.
7. Test the website from a second browser. Friends can use the same public link; each account's productions are saved separately in the managed database.

**Deployment status:** The application can run locally. This project does not provide a public backend, DNS name, or online database. Deploy these using your own accounts, URLs, and credentials.

## Repository layout

```text
SceneGraph-AI/
├── app.py                       FastAPI routes, authentication, and API downloads
├── models.py                    SQLAlchemy schema for SQLite/PostgreSQL
├── project_service.py           Owner-scoped CRUD and application orchestration
├── core/                        Parser, graph, continuity, scheduling, and metrics
├── docs/                        GitHub Pages website (HTML, CSS, JS, and config)
├── data/                        Sample screenplay and continuity fixtures
├── tests/                       Automated tests and optional browser smoke script
├── documentation/               Deployment, architecture, algorithms, and team work
├── .github/workflows/tests.yml  GitHub Actions test workflow
├── requirements.txt             Python runtime dependencies
├── requirements-dev.txt         Runtime and test dependencies
├── render.yaml                  Render web-service blueprint
└── .env.example                 Example environment variables (not secrets)
```

## Verify the backend

Install the development dependencies and run the test suite:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

FastAPI's interactive REST API reference is available at `http://127.0.0.1:8000/docs`. The application frontend is at `/`. The repository's `docs/` folder contains the files used by GitHub Pages.

## Five-member role ownership

| Member | Role | Working source |
|---|---|---|
| 1 | Data engineering and Fountain parser | `core/parser.py`, `core/normalizer.py`, `models.py` |
| 2 | Graph modeling and continuity analysis | `core/graph_engine.py`, `core/continuity.py` |
| 3 | Scheduling and optimization | `core/scheduler.py`, `core/constraints.py`, `core/baseline.py` |
| 4 | Analytics and reproducibility | `core/analytics.py`, `core/experiments.py`, `core/synthetic_data.py` |
| 5 | UI, API, integration, and deployment | `docs/`, `app.py`, `project_service.py`, `tests/` |

Every student should understand the full workflow and submit the complete repository link and files to GitHub/GCR as required by their faculty. List the actual team members in the submission report; the code does not include fabricated authorship or contribution history.

## Known limitations before public use

This is a deployable educational application, **not an audited enterprise SaaS service**. Broader public use requires a configured managed PostgreSQL service, HTTPS (provided by the hosting service), backups, migrations for future schema changes, stronger distributed rate limiting, password recovery and email verification, and production monitoring.

Some hosts' temporary free databases have expiry or data-retention limits. The development package does not include an online database, credentials, or an invented live URL. Keep secrets in hosting environment variables.

## References

- [Fountain syntax](https://fountain.io/syntax/)
- [GitHub Pages documentation](https://docs.github.com/en/pages)
- [Render FastAPI deployment](https://render.com/docs/deploy-fastapi)
- [Supabase PostgreSQL connections](https://supabase.com/docs/guides/database/connecting-to-postgres)
