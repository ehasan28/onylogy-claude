#!/bin/zsh
# usage: src/render.sh <docx> — converts to PDF next to it and prints page count
set -e
DOCX="$1"; DIR=$(dirname "$DOCX")
pkill -f soffice >/dev/null 2>&1 || true
/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir "$DIR" "$DOCX" >/dev/null 2>&1
PDF="${DOCX%.docx}.pdf"
pdfinfo "$PDF" | grep Pages
