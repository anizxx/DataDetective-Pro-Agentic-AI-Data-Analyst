from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .api import analysis_routes, chat_routes, document_routes, report_routes, upload_routes
from .config import get_settings
from .database import init_db
from .schemas import HealthResponse

settings = get_settings()

app = FastAPI(title=settings.app_name, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal server error", "error": str(exc)})


@app.get("/api/health", response_model=HealthResponse)
def health():
    return {"status": "ok", "service": "DataDetective Pro"}


app.include_router(upload_routes.router)
app.include_router(analysis_routes.router)
app.include_router(chat_routes.router)
app.include_router(document_routes.router)
app.include_router(report_routes.router)
