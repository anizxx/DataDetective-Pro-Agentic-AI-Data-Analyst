# DataDetective Pro

DataDetective Pro is an agentic AI data analyst platform built with FastAPI and React. It uploads CSV or Excel files, profiles data quality, runs safe DuckDB analytics, answers natural-language questions with a deterministic fallback mode, searches uploaded business documents, and generates exportable HTML reports.

## Main Features

- CSV, XLSX, and XLS dataset upload with file validation.
- Automated profiling for data types, missing values, duplicates, statistics, outliers, and quality score.
- Cleaning suggestions without mutating the original dataset.
- SELECT-only DuckDB analytics with blocked dangerous SQL keywords.
- Agent workflow: Supervisor, Data Profiler, Analyst, Visualization, and Validation agents.
- AI Analyst fallback mode when no LLM API key is configured.
- Document upload for TXT, PDF, and DOCX with keyword-search RAG fallback.
- Responsive SaaS dashboard with dark/light mode, charts, report generation, and settings.

## Architecture

The backend exposes REST APIs from `backend/app/main.py`. Uploaded datasets are stored under `data/uploads`, metadata is stored in `backend/storage`, DuckDB runs in memory for safe analytical queries, and reports are saved in `reports`. The frontend is a Vite React dashboard that calls the API through `frontend/src/services/api.js`.

## Technology Stack

Backend: Python 3.11+, FastAPI, Pandas, NumPy, DuckDB, Pydantic, OpenPyXL, PyMuPDF, python-docx, scikit-learn, pytest.

Frontend: React, Vite, Tailwind CSS, React Router, Axios, Recharts, Lucide React.

Storage: SQLite metadata, DuckDB analytics, local file storage, keyword RAG fallback.

## Folder Structure

```text
backend/app/api              API route modules
backend/app/services         Upload, profiling, SQL, RAG, chart, insight, report services
backend/app/agents           Agent workflow stages
backend/app/utils            Readers, validators, safe SQL, logging helpers
backend/tests                Pytest test suite
frontend/src/components      Reusable React UI
frontend/src/pages           Dashboard pages
data/sample_sales.csv        Fictional sample dataset
documents/sample_business_document.txt
reports                      Generated reports
_backup_before_codex_changes Original workspace files preserved before changes
```

The original `hello.py`, root `sales.csv`, and misplaced `backend/tools` files were copied into `_backup_before_codex_changes`. The legacy profiler path remains as a compatibility wrapper.

## Windows Setup

```powershell
cd "C:\Users\KIIT0001\Desktop\DataDetective pro"
cd backend
python -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\venv\Scripts\python.exe -m pytest
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
```

In a second PowerShell terminal:

```powershell
cd "C:\Users\KIIT0001\Desktop\DataDetective pro\frontend"
npm install
npm run dev
```

Open `http://127.0.0.1:5173`. The API runs at `http://127.0.0.1:8000`.

## Environment Variables

Create `backend/.env` from `backend/.env.example`.

```text
APP_NAME=DataDetective Pro
DEBUG=true
DATABASE_URL=sqlite:///./datadetective.db
OPENAI_API_KEY=
OPENAI_MODEL=
EMBEDDING_MODEL=
MAX_UPLOAD_SIZE_MB=20
FRONTEND_URL=http://localhost:5173
```

If `OPENAI_API_KEY` is blank, the app still works in fallback mode and the Settings page shows that the AI provider is not configured.

## API Endpoints

- `GET /api/health`
- `POST /api/upload/dataset`
- `GET /api/analysis/profile/{dataset_id}`
- `GET /api/analysis/cleaning-suggestions/{dataset_id}`
- `POST /api/analysis/sql-query`
- `POST /api/chat/query`
- `POST /api/documents/upload`
- `POST /api/documents/query`
- `POST /api/reports/generate/{dataset_id}`
- `GET /reports/{filename}`

## Sample Questions

- What is the total sales?
- What is the total profit?
- Which region generated the highest sales?
- Which category is most profitable?
- Show monthly sales trends.
- What is the average order value?
- Which products have negative profit?
- Are there missing values?
- Are there duplicate rows?
- Create a chart of sales by region.
- Give me three business insights.

## Testing

```powershell
cd backend
.\venv\Scripts\python.exe -m pytest
```

Tests cover health, CSV/XLSX upload, invalid files, profiling, missing values, duplicates, safe SQL, dangerous SQL rejection, and fallback AI query mode.

## Screenshots

Add screenshots of the dashboard, upload flow, AI analyst, document RAG, and reports after running the app locally.

## Future Improvements

- Add real OpenAI-compatible LLM calls with function-style tool routing.
- Add ChromaDB or FAISS semantic embeddings for document retrieval.
- Add authenticated users and dataset sharing.
- Add PDF report rendering.
- Add background jobs for very large files.

## Resume-Ready Description

Built DataDetective Pro, a full-stack agentic AI analytics platform with FastAPI, React, DuckDB, and Pandas that enables business users to upload datasets, profile data quality, ask natural-language questions, generate charts, search documents, and export reports with secure fallback behavior when no LLM key is configured.

## Interview Explanation

Explain it as a production-minded analytics workflow: the backend validates uploads, stores metadata, profiles data with Pandas, runs only safe SELECT queries in DuckDB, routes questions through distinct agent stages, validates outputs, and returns chart-ready JSON to a polished React dashboard. The key security decision is that user input never becomes executable Python or shell commands.

## Strong Resume Bullets

- Built a full-stack AI data analyst SaaS with FastAPI, React, DuckDB, Pandas, and Recharts, supporting dataset upload, profiling, safe SQL analytics, document Q&A, and report generation.
- Designed a deterministic agent workflow with Supervisor, Profiling, Analyst, Visualization, and Validation stages, including fallback analysis when external LLM credentials are unavailable.
- Implemented security-focused file validation, safe SQL keyword blocking, structured Pydantic responses, pytest coverage, and responsive dashboard UX with dark/light mode.

## Known Limitations

- LLM and semantic vector search are represented by safe fallback workflows unless provider credentials are added.
- Reports are generated as HTML files rather than PDF.
- Local storage is designed for development and portfolio demos, not multi-user production scale.
