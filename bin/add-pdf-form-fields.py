#!/usr/bin/env python3
"""Overlay AcroForm text fields on the contract PDF's underscore blanks."""

import sys
from pathlib import Path

import fitz

FIELDS = [
    ("cliente_nombre", "Nombre del Cliente"),
    ("cliente_domicilio", "Domicilio del Cliente"),
    ("prestador_firma", "Firma del Prestador"),
    ("prestador_fecha", "Fecha del Prestador"),
    ("cliente_firma", "Firma del Cliente"),
    ("cliente_nombre_sig", "Nombre del Cliente (firma)"),
    ("cliente_fecha", "Fecha del Cliente"),
]

ACCENT = (0.78, 0.64, 0.97)
FILL = (0.97, 0.94, 1.0)


def main(pdf_path: Path) -> None:
    doc = fitz.open(pdf_path)

    hits = []
    for page_idx, page in enumerate(doc):
        for rect in page.search_for("______"):
            hits.append((page_idx, rect))

    if len(hits) != len(FIELDS):
        print(
            f"Expected {len(FIELDS)} blanks, found {len(hits)}. "
            "Check that contrato.md still has the underscore placeholders.",
            file=sys.stderr,
        )
        sys.exit(1)

    for (page_idx, rect), (name, tooltip) in zip(hits, FIELDS):
        page = doc[page_idx]
        page.draw_rect(rect, color=FILL, fill=(1, 1, 1), width=0, overlay=True)

        widget = fitz.Widget()
        widget.rect = fitz.Rect(rect.x0, rect.y0 - 1, rect.x1, rect.y1 + 2)
        widget.field_type = fitz.PDF_WIDGET_TYPE_TEXT
        widget.field_name = name
        widget.field_label = tooltip
        widget.text_font = "Helv"
        widget.text_fontsize = 11
        widget.border_color = ACCENT
        widget.border_width = 0.6
        widget.fill_color = FILL
        page.add_widget(widget)

    tmp = pdf_path.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    tmp.replace(pdf_path)
    print(f"Added {len(FIELDS)} fillable fields to {pdf_path}")


if __name__ == "__main__":
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("downloads/Contrato-Hermes-Agent.pdf")
    main(pdf)
