#!/usr/bin/env bash
# Launch the local GitHub MCP on port 8788 (uses \$GITHUB_PERSONAL_ACCESS_TOKEN)

set -euo pipefail
: "${GITHUB_PERSONAL_ACCESS_TOKEN:?Need this env var}"
npx --yes --quiet @modelcontextprotocol/server-github 8788
