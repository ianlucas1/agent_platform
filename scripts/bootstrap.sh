#!/usr/bin/env bash
# agent_platform bootstrap – install all toolchains while the network is still up
set -euo pipefail
trap 'echo "BOOTSTRAP FAILED on line $LINENO" >&2' ERR

export DEBIAN_FRONTEND=noninteractive  # silence apt prompts

###############################################################################
# 0. Detect platform & ensure core runtimes
###############################################################################
OS="$(uname)"

if [[ "$OS" == "Linux" ]]; then
  # Ubuntu GitHub runners are non-root; use sudo fallback for apt
  apt_get() {
    if [[ "$(id -u)" == 0 ]]; then
      apt-get -qq "$@"
    else
      sudo -n apt-get -qq "$@" || {
        echo "WARN: apt-get $1 skipped (no sudo privileges)"; return 0; }
    fi
  }

  apt_get update
  apt_get install -y --no-install-recommends python3 python3-pip nodejs npm

elif [[ "$OS" == "Darwin" ]]; then
  if command -v brew >/dev/null 2>&1; then
    brew update >/dev/null
    for pkg in python3 node; do
      brew list "$pkg" >/dev/null 2>&1 || brew install "$pkg"
    done
    # Required for pip to work under Homebrew Python (PEP 668)
    export PIP_BREAK_SYSTEM_PACKAGES=1
  else
    echo "⚠️  Homebrew not found. Ensure python3, pip3, node, and npm are installed." >&2
    exit 1
  fi
else
  echo "❌ Unsupported operating system: $OS" >&2
  exit 1
fi

# Sanity check to fail fast if core tools are missing
for cmd in python3 pip3 node npm; do
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "❌ $cmd is required but not installed." >&2
    exit 1
  }
done

###############################################################################
# 1. Python & Node dependencies (network still available in this phase)
###############################################################################

# --- Core Python deps from requirements.txt ---
if [[ -f requirements.txt ]]; then
  pip3 install --quiet --no-cache-dir -r requirements.txt || \
    echo "WARNING: requirements.txt install failed"
fi

# --- Dev-toolchain (linters, formatters) ---
if [[ -f requirements-dev.txt ]]; then
  pip3 install --quiet --no-cache-dir -r requirements-dev.txt || \
    echo "WARNING: some dev wheels unavailable offline"
else
  echo "INFO: requirements-dev.txt not present; skipping dev-tool install"
fi

# --- MCP Node tools (version pinning TODO) ---
npm install -g --quiet --no-fund --omit=dev \
  @modelcontextprotocol/server-filesystem \
  @modelcontextprotocol/server-github

# --- Smoke-check versions ---
command -v ruff   >/dev/null && ruff   --version || echo "ruff   N/A"
command -v black  >/dev/null && black  --version || echo "black  N/A"
command -v bandit >/dev/null && bandit --version || echo "bandit N/A (security scan skipped)"

# --- Runtime version printout for CI debugging ---
python3 --version || echo "python3 N/A"
pip3 --version || echo "pip3 N/A"
node --version || echo "node N/A"
npm --version || echo "npm N/A"

###############################################################################
# 2. Signal offline mode for downstream scripts
###############################################################################
export NO_NET=1
echo "✅  Bootstrap complete – NO_NET=1 exported; subsequent scripts run offline."
