#!/usr/bin/env python3
"""Copy the authoring repository into its sibling Quartz publishing repository."""
from pathlib import Path
import json
import shutil

source = Path(__file__).resolve().parents[1]
destination = source.parent / 'quartz' / 'content'
if not (destination.parent / 'quartz.config.ts').is_file():
    raise SystemExit('Expected the sibling Quartz repository.')
if (destination / '.git').exists():
    raise SystemExit('Refusing to replace content containing a Git repository.')
staging = destination.with_name('content-sync-staging')
if staging.exists():
    raise SystemExit(f'Remove the previous unfinished staging directory first: {staging}')
staging.mkdir()
count = 0
try:
    for item in source.rglob('*'):
        relative = item.relative_to(source)
        if any(part.startswith('.') or part in ('node_modules', '_book', '__pycache__') for part in relative.parts):
            continue
        if item.is_symlink() or not item.is_file():
            continue
        target = staging / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
        if item.suffix == '.md':
            body = item.read_text()
            if not body.startswith('---\n'):
                title = next((line[2:].strip() for line in body.splitlines() if line.startswith('# ')), item.stem)
                # Add page metadata to the publishing copy only; preserve the entire source body.
                target.write_text('---\ntitle: ' + json.dumps(title, ensure_ascii=False) + '\n---\n' + body)
        count += 1
    if destination.exists():
        shutil.rmtree(destination)
    staging.rename(destination)
except BaseException:
    if staging.exists():
        shutil.rmtree(staging)
    raise
print(f'Synced {count} files from notes to quartz/content.')
