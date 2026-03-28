"""Convert docx/RCA-Laravel-MySQL-Production.md to .docx."""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt


def add_paragraph_with_inline_bold(doc: Document, text: str) -> None:
    """Add a paragraph; **segments** become bold."""
    p = doc.add_paragraph()
    parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            run = p.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            run = p.add_run(part[1:-1])
            run.font.name = "Consolas"
        else:
            p.add_run(part)


def md_to_docx(md_path: Path, out_path: Path) -> None:
    doc = Document()
    style = doc.styles["Normal"]
    style.font.size = Pt(11)

    lines = md_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("|") and "---" in stripped:
            i += 1
            continue

        if stripped.startswith("# "):
            h = doc.add_heading(stripped[2:].strip(), level=0)
            h.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            i += 1
            continue

        if stripped.startswith("## "):
            doc.add_heading(stripped[3:].strip(), level=1)
            i += 1
            continue

        if stripped.startswith("### "):
            doc.add_heading(stripped[4:].strip(), level=2)
            i += 1
            continue

        if stripped.startswith("|") and stripped.count("|") >= 2:
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            rows_parsed: list[list[str]] = []
            for tl in table_lines:
                cells = [c.strip() for c in tl.strip("|").split("|")]
                if len(cells) < 2:
                    continue
                if re.match(r"^[-:\s|]+$", tl.replace(" ", "")):
                    continue
                rows_parsed.append(cells)
            if rows_parsed:
                table = doc.add_table(rows=len(rows_parsed), cols=len(rows_parsed[0]))
                table.style = "Table Grid"
                for r_i, row_cells in enumerate(rows_parsed):
                    for c_i, cell_text in enumerate(row_cells):
                        table.rows[r_i].cells[c_i].text = cell_text
            continue

        if stripped.startswith("- "):
            doc.add_paragraph(stripped[2:], style="List Bullet")
            i += 1
            continue

        if stripped.startswith("- [ ]"):
            doc.add_paragraph(stripped, style="List Bullet")
            i += 1
            continue

        if stripped.startswith("_") and stripped.endswith("_") and len(stripped) > 2:
            p = doc.add_paragraph()
            run = p.add_run(stripped.strip("_"))
            run.italic = True
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        add_paragraph_with_inline_bold(doc, line.rstrip())
        i += 1

    doc.save(out_path)


def main() -> None:
    base = Path(__file__).resolve().parent
    md_path = base / "RCA-Laravel-MySQL-Production.md"
    out_path = base / "RCA-Laravel-MySQL-Production.docx"
    if not md_path.is_file():
        raise SystemExit(f"Missing source: {md_path}")
    md_to_docx(md_path, out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
