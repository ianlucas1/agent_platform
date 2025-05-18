#!/usr/bin/env bash
set -euo pipefail

OS="$(uname)"

if [[ "$OS" == "Linux" ]]; then
    # Ensure python3, pip3, node, npm exist or can be installed
    for pkg in python3 pip3 node npm; do
        if ! command -v "$pkg" >/dev/null 2>&1; then
            if command -v apt-get >/dev/null && [[ "$(id -u)" == 0 ]]; then
                apt-get update -y && apt-get install -y python3 python3-pip nodejs npm
                break
            else
                echo "$pkg missing and no root privileges; see docs/offline_setup.md" >&2
                exit 1
            fi
        fi
    done
elif [[ "$OS" == "Darwin" ]]; then
    if command -v brew >/dev/null 2>&1; then
        brew update
        # Install python3 and node via brew if not installed
        for pkg in python3 node; do
            if ! brew list "$pkg" >/dev/null 2>&1; then
                brew install "$pkg"
            fi
        done
    else
        echo "Homebrew not found. Ensure python3, pip3, node, and npm are installed." >&2
    fi
else
    echo "Unsupported operating system: $OS" >&2
    exit 1
fi

# Verify commands exist
for cmd in python3 pip3 node npm; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "$cmd is required but was not installed." >&2
        exit 1
    fi
done

# Install Python dependencies and MCP servers
if [[ -n "${NO_NET:-}" ]]; then
    echo "NO_NET set – skipping pip/npm installs." >&2
else
    pip3 install --no-cache-dir -r requirements.txt
    pip3 install --no-cache-dir -r requirements-dev.txt
    npm install -g @modelcontextprotocol/server-filesystem @modelcontextprotocol/server-github
fi

echo "Bootstrap completed successfully."
