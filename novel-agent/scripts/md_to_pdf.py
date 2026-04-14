#!/usr/bin/env python3
"""Convert Chinese novel markdown to readable PDF."""

import re
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

# Font paths for macOS
FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/PingFang.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]


def register_chinese_font():
    """Register a Chinese font. TTC files need special handling."""
    try:
        # Try Hiragino Sans GB (common on macOS)
        pdfmetrics.registerFont(TTFont("ChineseFont", "/System/Library/Fonts/Hiragino Sans GB.ttc"))
        return "ChineseFont"
    except Exception:
        pass
    try:
        # Fallback: PingFang from Supplemental
        pdfmetrics.registerFont(TTFont("ChineseFont", "/System/Library/Fonts/Supplemental/PingFang.ttc"))
        return "ChineseFont"
    except Exception:
        pass
    # Last resort: Helvetica (will show boxes for Chinese)
    return "Helvetica"


def parse_markdown(content: str) -> list:
    """Parse markdown into blocks for PDF."""
    blocks = []
    lines = content.split("\n")
    i = 0
    metadata_skipped = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip only the first metadata block (--- ... ---) at top
        if stripped == "---":
            if not metadata_skipped:
                i += 1
                while i < len(lines) and lines[i].strip() != "---":
                    i += 1
                i += 1
                metadata_skipped = True
                continue
            else:
                i += 1  # Skip standalone --- dividers
                continue

        # H1 - Title
        if line.startswith("# ") and not line.startswith("## "):
            title = line[2:].strip()
            blocks.append(("h1", title))
            i += 1
            continue

        # H2 - Chapter
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip()))
            i += 1
            continue

        # Empty line
        if not stripped:
            blocks.append(("spacer", None))
            i += 1
            continue

        # Regular paragraph - collect until empty line
        para_lines = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip():
            para_lines.append(lines[i].strip())
            i += 1
        blocks.append(("para", " ".join(para_lines)))

    return blocks


def main():
    base = Path(__file__).parent.parent
    src = base / "out" / "novel_final_zh.md"
    dst = base / "out" / "novel_final_zh.pdf"

    if not src.exists():
        print(f"Error: {src} not found")
        sys.exit(1)

    content = src.read_text(encoding="utf-8")
    font_name = register_chinese_font()

    # Page setup: A4, readable margins for long-form reading
    doc = SimpleDocTemplate(
        str(dst),
        pagesize=A4,
        leftMargin=2.2 * cm,
        rightMargin=2.2 * cm,
        topMargin=2.2 * cm,
        bottomMargin=2.2 * cm,
    )

    styles = getSampleStyleSheet()
    body_style = ParagraphStyle(
        name="ChineseBody",
        fontName=font_name,
        fontSize=12,
        leading=20,
        spaceAfter=10,
        alignment=0,  # LEFT
        wordWrap="CJK",
    )
    h1_style = ParagraphStyle(
        name="ChineseH1",
        fontName=font_name,
        fontSize=22,
        leading=28,
        spaceAfter=12,
        spaceBefore=20,
        alignment=1,  # CENTER
    )
    h2_style = ParagraphStyle(
        name="ChineseH2",
        fontName=font_name,
        fontSize=16,
        leading=22,
        spaceAfter=12,
        spaceBefore=24,
        alignment=0,
    )

    story = []
    in_body = False
    skip_meta = True

    for block_type, text in parse_markdown(content):
        if block_type == "spacer":
            if in_body:
                story.append(Spacer(1, 6))
            continue

        if block_type == "h1":
            # Skip first title block (we'll add custom cover)
            if "UCL" in text or "海归" in text:
                if not story:
                    story.append(Paragraph(text, h1_style))
                    story.append(Spacer(1, 12))
                continue
            story.append(Paragraph(text, h1_style))
            in_body = True
            continue

        if block_type == "h2":
            if skip_meta and ("目录" in text or "字数" in text):
                continue
            skip_meta = False
            # Page break before new chapter (except first)
            if re.search(r"第[一二三四五六七八九十]+章", text) and len(story) > 3:
                story.append(PageBreak())
            if story and not isinstance(story[-1], PageBreak):
                story.append(Spacer(1, 6))
            story.append(Paragraph(text, h2_style))
            in_body = True
            continue

        if block_type == "para":
            # Skip metadata lines
            if skip_meta and ("字数" in text or "章节" in text or "完成" in text):
                continue
            skip_meta = False
            # Escape XML for reportlab
            text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            story.append(Paragraph(text, body_style))
            in_body = True

    doc.build(story)
    print(f"✓ PDF created: {dst}")
    print(f"  File size: {dst.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
