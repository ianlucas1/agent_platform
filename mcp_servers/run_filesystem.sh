#!/usr/bin/env bash
# Launch the local Filesystem MCP on port 8787

set -euo pipefail
npx --yes --quiet @modelcontextprotocol/server-filesystem /workspace 8787
