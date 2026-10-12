#!/usr/bin/env python3
"""Package only the draft and the dependencies needed for offline recompilation."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
out = root / "build/electronics-skeleton-source.zip"
files = [root / name for name in (
    "main.tex", "planning.tex", "references.bib", "verse.sty", "Makefile",
    "README.md", "research/template_manifest.json", "research/verse_manifest.json",
    "research/verse/README", "research/verse/verse.dtx", "research/verse/verse.ins",
)]
for folder in ("Definitions", "sections", "tools"):
    files.extend(p for p in (root / folder).rglob("*") if p.is_file()
                 and "__pycache__" not in p.parts)
with ZipFile(out, "w", ZIP_DEFLATED) as archive:
    for p in sorted(files):
        archive.write(p, Path("electronics-skeleton") / p.relative_to(root))
    archive.write(root / "build/main.pdf", "electronics-skeleton/main.pdf")
    archive.write(root / "build/skeleton_verification.json",
                  "electronics-skeleton/skeleton_verification.json")
assert out.stat().st_size < 120_000_000, "Archive exceeds the submission file budget"
print(f"Created {out} ({out.stat().st_size:,} bytes). Explicit planning placeholders remain.")
