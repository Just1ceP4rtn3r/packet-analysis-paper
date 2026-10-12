#!/usr/bin/env python3
"""Check the actual planning PDF against its declared physical page allocation."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "build/main.pdf"
info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
assert pages == 22, f"Expected 22 physical pages, got {pages}"
assert "A4" in info, "Expected A4 page size"

expected = {
    1: ["Abstract", "22-page structural draft"],
    2: ["1. Introduction"],
    4: ["2. Related Work", "2.1. Traffic Representations"],
    5: ["3. Methodology", "3.1. Problem Formulation",
        "3.1.1. Target Flows", "3.1.2. Decision Paths"],
    6: ["3.2. System Overview"],
    7: ["3.3. Message-Level Operational Semantics"],
    8: ["3.4. Cross-Flow Behavioral Semantics"],
    9: ["3.5. Dual-Path Candidate Selection", "3.5.2. Cross-Flow Discovery"],
    10: ["3.6. Typed Decisions", "3.7. Implementation"],
    11: ["4. Experiments", "4.1. Experimental Setup"],
    12: ["4.1.3. Metrics and Measurement Protocol"],
    13: ["4.2. End-to-End Detection"],
    14: ["4.3. Semantic Representation Ablations"],
    15: ["4.4. Decision-Path Ablations"],
    16: ["4.5. Jev Comparison"],
    17: ["4.6. Budget Sensitivity", "4.6.2. Traceable Cross-Flow Evidence"],
    18: ["5. Discussion", "6. Conclusions"],
    19: ["Author Contributions", "Data Availability", "Conflicts of Interest"],
    20: ["Appendix A.", "Reproducibility Details", "Table A1"],
    21: ["References"],
    22: ["Reserved continuation"],
}
for page, snippets in expected.items():
    text = subprocess.check_output(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(PDF), "-"],
        text=True,
    )
    text = re.sub(r"\s+", " ", text)
    for snippet in snippets:
        assert snippet in text, f"Page {page}: missing {snippet!r}"

log = (ROOT / "build/main.log").read_text()
bad = [line for line in log.splitlines() if any(s in line for s in (
    "undefined", "Overfull", "LaTeX Error", "Package paper-plan Error",
    "multiply defined", "Rerun to get cross-references right",
))]
assert not bad, "Build issues:\n" + "\n".join(bad)
main = (ROOT / "main.tex").read_text()
abstract = re.search(r"\\abstract\{(.*?)\}\s*\\keyword", main, re.S)[1]
abstract_words = len(abstract.split())
assert abstract_words <= 200, f"Abstract placeholder has {abstract_words} words"
keywords = re.search(r"\\keyword\{([^}]+)\}", main)[1].split(";")
assert 3 <= len(keywords) <= 10
assert "electronics,article,submit,moreauthors,pdftex" in main

manifest = json.loads((ROOT / "research/template_manifest.json").read_text())
for name, expected_hash in manifest["definitions"].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected_hash, f"Official template file modified: {name}"
intro_hash = hashlib.sha256((ROOT / "sections/introduction.tex").read_bytes()).hexdigest()
report = {
    "status": "passed",
    "artifact": "structural draft with explicit placeholders; not a completed submission",
    "physical_pages": pages,
    "page_size": "A4",
    "section_page_checks": expected,
    "abstract_placeholder_words": abstract_words,
    "keyword_count": len(keywords),
    "introduction_sha256": intro_hash,
    "official_template_hashes_unchanged": True,
    "undefined_references_or_layout_overflows": False,
}
(ROOT / "build/skeleton_verification.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n"
)
print(f"PASS: {pages} A4 pages; section starts, citations, template hashes, "
      f"abstract ({abstract_words} words), and {len(keywords)} keywords verified.")
