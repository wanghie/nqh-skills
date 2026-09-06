#!/usr/bin/env bash
# nqh-video-shorts - full chain: transcribe -> cut -> reframe -> zoom -> captions
# Usage: pipeline.sh INPUT.mp4 [--audience vi|en|auto] [--outdir DIR]
#                    [--skip cut,reframe,zoom,captions] [--mode balanced]
#                    [--aspect 9:16] [--density 0.12] [--dry-run]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
IN=""; AUD="auto"; OUTDIR=""; SKIP=""; MODE="balanced"; ASPECT="9:16"; DENSITY="0.12"; DRY=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --audience) AUD="$2"; shift 2;;
    --outdir)   OUTDIR="$2"; shift 2;;
    --skip)     SKIP="$2"; shift 2;;
    --mode)     MODE="$2"; shift 2;;
    --aspect)   ASPECT="$2"; shift 2;;
    --density)  DENSITY="$2"; shift 2;;
    --dry-run)  DRY="1"; shift;;
    -*) echo "unknown flag $1" >&2; exit 1;;
    *)  IN="$1"; shift;;
  esac
done
[[ -n "$IN" ]] || { echo "usage: pipeline.sh INPUT.mp4 [--audience vi|en|auto]" >&2; exit 1; }
[[ -f "$IN" ]] || { echo "no such file: $IN" >&2; exit 1; }

skipped() { [[ ",$SKIP," == *",$1,"* ]]; }
BASE="$(basename "${IN%.*}")"
OUTDIR="${OUTDIR:-$(dirname "$IN")/sf-out}"
mkdir -p "$OUTDIR"
S="$ROOT/skills"; CUR="$IN"
step() { printf '\n[%s] %s\n' "$1" "$2" >&2; }

step 1/5 "transcribe"
TR="$OUTDIR/$BASE.transcript.json"
[[ -f "$TR" ]] || python3 "$S/nqh-video-transcribe/scripts/transcribe.py" "$IN" --audience "$AUD" -o "$TR" >/dev/null
AUD="$(python3 -c "import json,sys;print(json.load(open(sys.argv[1],encoding='utf-8'))['audience'])" "$TR")"
echo "  audience = $AUD" >&2

if ! skipped cut; then
  step 2/5 "cut silence + fillers"
  python3 "$S/nqh-video-cut-silence/scripts/cut.py" "$CUR" -t "$TR" --mode "$MODE" \
      -o "$OUTDIR/$BASE.cut.mp4" ${DRY:+--dry-run} >/dev/null
  if [[ -z "$DRY" ]]; then
    python3 "$ROOT/lib/remap.py" "$TR" "$OUTDIR/$BASE.cut.edl.json" \
        -o "$OUTDIR/$BASE.cut.transcript.json" >/dev/null
    CUR="$OUTDIR/$BASE.cut.mp4"; TR="$OUTDIR/$BASE.cut.transcript.json"
  fi
fi

if ! skipped reframe; then
  step 3/5 "reframe -> $ASPECT"
  python3 "$S/nqh-video-reframe/scripts/reframe.py" "$CUR" --aspect "$ASPECT" --mode face \
      -o "$OUTDIR/$BASE.vertical.mp4" ${DRY:+--dry-run} >/dev/null
  [[ -z "$DRY" ]] && CUR="$OUTDIR/$BASE.vertical.mp4"
fi

if ! skipped zoom; then
  step 4/5 "punch zoom"
  python3 "$S/nqh-video-punch-zoom/scripts/zoom.py" "$CUR" -t "$TR" --density "$DENSITY" \
      -o "$OUTDIR/$BASE.zoom.mp4" ${DRY:+--dry-run} >/dev/null
  [[ -z "$DRY" ]] && CUR="$OUTDIR/$BASE.zoom.mp4"
fi

if ! skipped captions; then
  step 5/5 "burn captions"
  python3 "$S/nqh-video-captions/scripts/captions.py" "$CUR" -t "$TR" --style bold \
      -o "$OUTDIR/$BASE.final.mp4" ${DRY:+--ass-only} >/dev/null
  [[ -z "$DRY" ]] && CUR="$OUTDIR/$BASE.final.mp4"
fi

printf '\ndone -> %s\n' "$CUR"
