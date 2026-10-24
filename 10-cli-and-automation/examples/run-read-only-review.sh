#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: run-read-only-review.sh PROMPT_FILE OUTPUT_DIR" >&2
  exit 2
fi

prompt_file=$1
output_dir=$2
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
schema_file="$script_dir/review-schema.json"
events_file="$output_dir/events.jsonl"
final_file="$output_dir/final.json"

if [[ ! -f "$prompt_file" ]]; then
  echo "prompt file not found: $prompt_file" >&2
  exit 2
fi

command -v codex >/dev/null || {
  echo "codex is required" >&2
  exit 127
}

command -v jq >/dev/null || {
  echo "jq is required" >&2
  exit 127
}

mkdir -p -- "$output_dir"

if ! codex exec \
  --ephemeral \
  --sandbox read-only \
  -c 'approval_policy="never"' \
  --output-schema "$schema_file" \
  --output-last-message "$final_file" \
  --json \
  - < "$prompt_file" > "$events_file"; then
  echo "codex exec failed; inspect standard error and $events_file" >&2
  exit 1
fi

if [[ ! -s "$final_file" ]]; then
  echo "codex exec completed without a final response" >&2
  exit 1
fi

jq -e . "$final_file" >/dev/null
echo "events: $events_file"
echo "final:  $final_file"
