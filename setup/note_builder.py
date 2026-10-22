#!/usr/bin/env python3
"""
md_to_ipynb.py — Convert a Markdown file into a Jupyter notebook.

Self-bootstrapping: installs `nbformat` automatically if it is missing.

Usage:
    python md_to_ipynb.py                      # lemmatization-nlp.md -> lemmatization-nlp.ipynb
    python md_to_ipynb.py input.md             # input.md -> input.ipynb
    python md_to_ipynb.py input.md output.ipynb
"""

import importlib
import re
import subprocess
import sys
from pathlib import Path


# --------------------------------------------------------------- bootstrap
def ensure_nbformat():
    """Import nbformat, installing it via pip on first use if necessary."""
    try:
        return importlib.import_module("nbformat")
    except ImportError:
        print("[setup] nbformat not found — installing ...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet", "nbformat"]
        )
        # Force Python to see the freshly-installed package
        importlib.invalidate_caches()
        return importlib.import_module("nbformat")


# --------------------------------------------------------------- parser
def parse_markdown(md_text: str):
    """Split Markdown text into ordered ('md'|'code', content) pairs."""
    # Strip an outer ````markdown ... ```` wrapper if the file was saved that way
    md_text = re.sub(
        r"^````markdown\n(.*)\n````\s*$", r"\1", md_text, flags=re.DOTALL
    )

    fence = re.compile(r"```(?:python3?|py)\s*\n(.*?)```", re.DOTALL)

    last = 0
    for match in fence.finditer(md_text):
        chunk = md_text[last:match.start()].rstrip()
        if chunk:
            yield "md", chunk
        yield "code", match.group(1).rstrip() + "\n"
        last = match.end()

    tail = md_text[last:].rstrip()
    if tail:
        yield "md", tail


# --------------------------------------------------------------- convert
def convert(nbf, md_path: Path, ipynb_path: Path) -> int:
    """Build the notebook using nbformat and write it. Returns cell count."""
    cells = []
    for kind, content in parse_markdown(md_path.read_text(encoding="utf-8")):
        if kind == "md":
            cells.append(nbf.v4.new_markdown_cell(content))
        else:
            cells.append(nbf.v4.new_code_cell(content))

    nb = nbf.v4.new_notebook()
    nb["cells"] = cells
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "version": sys.version.split()[0]},
    }
    nbf.write(nb, str(ipynb_path))
    return len(cells)


# --------------------------------------------------------------- main
def main() -> None:
    args = sys.argv[1:]
    md_path = Path(args[0]) if args else Path("week6.md")
    ipynb_path = Path(args[1]) if len(args) > 1 else md_path.with_suffix(".ipynb")

    if not md_path.exists():
        sys.exit(
            f"Error: '{md_path}' not found.\n"
            f"Run this script from the folder that contains it, "
            f"or pass the correct path."
        )

    nbf = ensure_nbformat()
    count = convert(nbf, md_path, ipynb_path)
    print(f"[ok] {md_path} -> {ipynb_path}  ({count} cells)")


if __name__ == "__main__":
    main()