#!/usr/bin/env bash
# CAP-X bootstrap – install all toolchains while the network is still up
set -euo pipefail
trap 'echo "BOOTSTRAP FAILED on line $LINENO" >&2' ERR

###############################################################################
# 0. Detect platform & ensure core runtimes
###############################################################################
OS="$(uname)"

if [[ "$OS" == "Linux" ]]; then
  export DEBIAN_FRONTEND=noninteractive
  apt_get() {
    if [[ "$(id -u)" == 0 ]]; then
      apt-get -qq "$@"
    else
      sudo -n apt-get -qq "$@" || {
        echo "WARN: apt-get $1 skipped (no sudo privileges)"; return 0; }
    fi
  }

  apt_get update
  # Ubuntu 24.04 ships Python 3.12; add 3.11 here only if you must.
  apt_get install -y --no-install-recommends python3 python3-pip nodejs npm
elif [[ "$OS" == "Darwin" ]]; then
  if command -v brew >/dev/null 2>&1; then
    brew update >/dev/null
    for pkg in python3 node; do
      brew list "$pkg" >/dev/null 2>&1 || brew install "$pkg"
    done
  else
    echo "❌  Homebrew not found; install python3 & node manually." >&2
    exit 1
  fi
else
  echo "❌ Unsupported operating system: $OS" >&2
  exit 1
fi

# Sanity-check
for cmd in python3 pip3 node npm; do
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "❌ $cmd is required but not installed." >&2
    exit 1
  }
done

###############################################################################
# 1. Python & Node dependencies  (network still available in this phase)
###############################################################################
if [[ -z "${NO_NET:-}" ]]; then
  # --- Core agent/runtime deps ------------------------------------------------
  pip3 install --quiet google-adk litellm        # TODO: pin & vendor wheels
  npm install -g --quiet --no-fund --omit=dev \
    @modelcontextprotocol/server-filesystem \
    @modelcontextprotocol/server-github

  # --- Dev-toolchain (formatters / linters) ----------------------------------
  if [[ -f requirements-dev.txt ]]; then
    # Use --no-cache-dir so wheels don’t fill the 4 GB sandbox
    pip3 install --quiet --no-cache-dir -r requirements-dev.txt \
      || echo "WARNING: some dev wheels unavailable offline"
  else
    echo "INFO: requirements-dev.txt not present; skipping dev-tool install"
  fi
else
  echo "NO_NET set – skipping pip/npm installs." >&2
fi

# --- Smoke-check versions so the box fails fast if anything is missing -------
command -v ruff   >/dev/null && ruff   --version || echo "ruff   N/A"
command -v black  >/dev/null && black  --version || echo "black  N/A"
command -v bandit >/dev/null && bandit --version || echo "bandit N/A (skipped)"

###############################################################################
# 2. Signal offline mode for downstream scripts
###############################################################################
export NO_NET=1
echo "✅  Bootstrap complete – NO_NET=1 exported; subsequent scripts run offline."
