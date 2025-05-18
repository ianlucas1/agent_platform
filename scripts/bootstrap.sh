#!/usr/bin/env bash
set -euo pipefail

OS="$(uname)"

if [[ "$OS" == "Linux" ]]; then
    echo "Linux detected – assuming python3/pip & node/npm already present; skipping apt-get."
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

echo "Bootstrap completed successfully."
