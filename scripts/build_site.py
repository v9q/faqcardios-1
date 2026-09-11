#!/usr/bin/env python3
"""Injects site/data.json into site/index.template.html to produce site/index.html."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site" / "data.json"
TEMPLATE = ROOT / "site" / "index.template.html"
OUT = ROOT / "site" / "index.html"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    template = TEMPLATE.read_text(encoding="utf-8")
    # Safe for embedding inside a <script type="application/json"> block.
    payload = json.dumps(data, ensure_ascii=False).replace("</script", "<\\/script")
    out = template.replace("__DATA__", payload)
    OUT.write_text(out, encoding="utf-8")
    print(f"Wrote {OUT} ({len(out)} bytes)")


if __name__ == "__main__":
    main()
