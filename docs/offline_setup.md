# Offline Setup Guide

This repository can run without internet access. To prepare an environment:

1. Download all required Python wheels or tarballs ahead of time and store them in a `vendor/` directory.
2. Before running `scripts/bootstrap.sh`, export `NO_NET=1` to skip any online installs.
3. When packages are vendored, install them with:
   ```bash
   pip install --no-index --find-links=vendor/ -r requirements.txt
   ```

See the main README for additional tips.
