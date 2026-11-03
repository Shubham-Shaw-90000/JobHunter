Career_Growth_System/
│
├── .github/                  # CI/CD workflows (linting, tests)
│   └── workflows/
├── docs/                     # Specifications & Phase architecture documents
│   └── implementation/
├── backend/                  # FastAPI Application
│   ├── .venv/                # (Ignored by Git) Local Python virtualenv
│   ├── alembic/              # Database migration scripts
│   ├── app/
│   │   ├── core/             # Config, security, database session setup
│   │   ├── modules/          # Domain-first business features:
│   │   │   ├── candidate/    # Profile, education, skills, progress
│   │   │   ├── jobs/         # Pipelines, discovery ingestion, review queue
│   │   │   ├── resumes/      # Master resume, tailoring, DOCX/PDF generation
│   │   │   ├── applications/ # Status tracker, event history
│   │   │   └── ai_engine/    # Orchestrator (Gemini/Groq/Ollama router)
│   │   └── main.py           # FastAPI entrypoint, router mounting, middleware
│   ├── tests/                # Pytest unit and integration test suite
│   ├── alembic.ini           # Migration configuration
│   ├── requirements.txt      # (or pyproject.toml) Python dependencies
│   └── .env.example          # Backend environment template
│
├── frontend/                 # React + TypeScript + Vite Application
│   ├── src/
│   │   ├── components/       # Reusable UI components (buttons, tables, modals)
│   │   ├── features/         # Domain-first UI slices (jobs, candidate, resumes)
│   │   ├── lib/              # API client, utilities
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   └── tsconfig.json
│
├── docker-compose.yml        # Local services (PostgreSQL, local storage)
├── .gitignore                # Root Git ignore rules
└── README.md                 # Project orientation