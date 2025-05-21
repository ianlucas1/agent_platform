"""
Minimal Filesystem MCP server for FS17.
Provides health check and read-only file fetch.
"""

from pathlib import Path
from fastapi import FastAPI, HTTPException
import uvicorn

ROOT = Path(__file__).resolve().parents[1]  # repo root
app = FastAPI(title="Filesystem MCP", docs_url=None, redoc_url=None)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/file")
def read_file(path: str):
    fp = (ROOT / path).resolve()
    if not fp.is_file() or not str(fp).startswith(str(ROOT)):
        raise HTTPException(404, "not found")
    return {"content": fp.read_text()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8787)
