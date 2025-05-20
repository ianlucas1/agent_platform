# Implementation / Tasking Prompt Template

```
git checkout -b codex/<feature-branch>

## Patch blocks
apply_patch <file> <<'PATCH'
...
PATCH

## Commit
git add …
git commit -m "<type>: <summary> (<task id>)"

echo DONE   # clean exit; human will Push ▾ / Create PR
```

### Roadmap variant
Start with:

```
python scripts/parse_roadmap.py --format json > /tmp/tasks.json
```
