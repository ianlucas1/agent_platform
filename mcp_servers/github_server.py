"""
Minimal GitHub MCP server for FS18.
Health check plus stub handlers for commit, branch, PR.
"""

from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="GitHub MCP", docs_url=None, redoc_url=None)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/commit")
def commit():
    raise HTTPException(501, "commit not implemented")


@app.post("/branch")
def branch():
    raise HTTPException(501, "branch not implemented")


@app.post("/pr")
def pull_request():
    raise HTTPException(501, "pull-request not implemented")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8788)
