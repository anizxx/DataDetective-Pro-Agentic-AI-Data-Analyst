from typing import Any, Literal
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    service: str


class DatasetMetadata(BaseModel):
    dataset_id: str
    filename: str
    row_count: int
    column_count: int
    columns: list[str]
    preview: list[dict[str, Any]]
    detected_file_type: str


class ProfileResponse(BaseModel):
    dataset_id: str
    row_count: int
    column_count: int
    column_names: list[str]
    data_types: dict[str, str]
    missing_values: dict[str, int]
    missing_percentage: dict[str, float]
    duplicate_row_count: int
    unique_values: dict[str, int]
    numeric_columns: list[str]
    categorical_columns: list[str]
    datetime_columns: list[str]
    basic_statistics: dict[str, dict[str, float | int | None]]
    possible_outliers: dict[str, int]
    data_quality_score: float


class SQLQueryRequest(BaseModel):
    dataset_id: str
    sql_query: str = Field(min_length=1, max_length=5000)


class SQLQueryResponse(BaseModel):
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int


class ChatRequest(BaseModel):
    dataset_id: str
    user_question: str = Field(min_length=1, max_length=2000)
    history: list[dict[str, str]] = []


class ChartConfig(BaseModel):
    type: Literal["bar", "line", "pie", "area", "scatter", "histogram", "kpi", "table"]
    title: str
    x: str | None = None
    y: str | None = None
    data: list[dict[str, Any]] = []


class ChatResponse(BaseModel):
    mode: str
    answer: str
    analysis_plan: list[str]
    sql: str | None = None
    table: list[dict[str, Any]] = []
    chart: ChartConfig
    assumptions: list[str]
    validation: dict[str, Any]


class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    chunk_count: int
    mode: str


class DocumentQueryRequest(BaseModel):
    document_id: str
    question: str = Field(min_length=1, max_length=2000)


class DocumentQueryResponse(BaseModel):
    answer: str
    sources: list[dict[str, Any]]
    mode: str


class ReportResponse(BaseModel):
    report_id: str
    filename: str
    download_url: str
