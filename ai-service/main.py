from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from analyzer.repository_scanner import scan_repository


app = FastAPI(
    title="DevLens AI Service",
    description="AI and code intelligence service for DevLens AI",
    version="0.1.0",
)


class RepositoryScanRequest(BaseModel):
    repository_path: str


class RepositoryScanResponse(BaseModel):
    repository_path: str
    file_count: int
    files: list[dict]


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "devlens-ai-service",
    }


@app.post(
    "/repositories/scan",
    response_model=RepositoryScanResponse,
)
def scan_repository_endpoint(
    request: RepositoryScanRequest,
):
    repository_path = Path(request.repository_path)

    if not repository_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Repository path does not exist",
        )

    if not repository_path.is_dir():
        raise HTTPException(
            status_code=400,
            detail="Repository path must be a directory",
        )

    try:
        files = scan_repository(
            str(repository_path)
        )

        return RepositoryScanResponse(
            repository_path=str(repository_path),
            file_count=len(files),
            files=files,
        )

    except (FileNotFoundError, ValueError) as exception:
        raise HTTPException(
            status_code=400,
            detail=str(exception),
        )