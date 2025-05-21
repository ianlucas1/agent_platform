# Local MCP Servers

| Server | Port | Purpose | Start script |
|--------|------|---------|--------------|
| Filesystem | **8787** | Read/write repo files via MCP tool. | `mcp_servers/run_filesystem.sh` |
| GitHub     | **8788** | Commit, branch, PR operations via MCP tool. | `mcp_servers/run_github.sh` |

## Usage

```bash
# one\u2011time (from repo root)
./mcp_servers/run_filesystem.sh &
./mcp_servers/run_github.sh &
```

Both scripts rely on packages installed in **bootstrap.sh**:

```bash
npm install -g @modelcontextprotocol/server-filesystem @modelcontextprotocol/server-github
```

Set `GITHUB_PERSONAL_ACCESS_TOKEN` in Codex secrets before starting the GitHub server.
