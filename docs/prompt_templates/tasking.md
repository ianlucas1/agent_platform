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

**Extending the template**  
* `cat >` blocks → add new files.  
* `git rm` / `git mv` → delete or rename files.  
* Run tests/lints before the commit as extra shell commands.  
* Always leave `echo DONE` last so Codex shows the Push menu.
```

### Roadmap variant

Start with:

```
python scripts/parse_roadmap.py --format json > /tmp/tasks.json
```
