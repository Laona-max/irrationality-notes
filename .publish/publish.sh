#!/bin/sh
set -eu
notes_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
quartz_dir=$(dirname -- "$notes_dir")/quartz
message=${1:-Update reading notes}
python3 "$notes_dir/.publish/sync.py"
(cd "$quartz_dir" && node quartz/bootstrap-cli.mjs build)
for repo in "$notes_dir" "$quartz_dir"; do
  test "$(git -C "$repo" branch --show-current)" = main || { echo "Expected main in $repo"; exit 1; }
  git -C "$repo" remote get-url origin >/dev/null
  git -C "$repo" ls-remote origin HEAD >/dev/null
done
for repo in "$notes_dir" "$quartz_dir"; do
  git -C "$repo" add -A
  if ! git -C "$repo" diff --cached --quiet; then
    git -C "$repo" commit -m "$message"
  fi
  git -C "$repo" push -u origin main
done
