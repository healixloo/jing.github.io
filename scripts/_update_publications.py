#!/usr/bin/env python3
# coding: utf-8

"""
Update publications for Jekyll academic site from Google Scholar.

Usage:
    python update_publications.py

Requirements:
    pip install scholarly pandas

This script:
1. Fetches publications from your Google Scholar profile.
2. Converts them into Markdown files for Jekyll (_publications/).
3. Each file is named YYYY-MM-DD-[slug].md with proper YAML front matter.
"""

import os
import re
import pandas as pd
from scholarly import scholarly

# --- Config ---
SCHOLAR_ID = "1W_3YjAAAAAJ"   # your Google Scholar ID
OUTPUT_DIR = "../_publications"  # relative to script location

# --- Escape special characters for YAML ---
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}
def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in str(text))

# --- Slugify titles for filenames ---
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def main():
    print("Fetching publications from Google Scholar...")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []
    for pub in author['publications']:
        bib = pub['bib']
        title = bib.get('title', 'Untitled')
        year = bib.get('pub_year', '1900')
        venue = bib.get('venue', '')
        authors = bib.get('author', '')
        citation = f"{authors} ({year}). {title}. {venue}"

        pub_date = f"{year}-01-01"
        url_slug = slugify(title)

        md_filename = f"{pub_date}-{url_slug}.md"
        html_filename = f"{pub_date}-{url_slug}"

        # --- YAML front matter ---
        md = f"---\ntitle: \"{html_escape(title)}\"\n"
        md += "collection: publications"
        md += f"\npermalink: /publication/{html_filename}"
        md += f"\ndate: {pub_date}"
        md += f"\nvenue: '{html_escape(venue)}'"
        md += f"\ncitation: '{html_escape(citation)}'"
        md += "\n---\n"

        # --- Body ---
        md += f"\nRecommended citation: {citation}\n"

        pubs.append((md_filename, md))

    # --- Write files ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for fname, content in pubs:
        path = os.path.join(OUTPUT_DIR, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote {path}")

    print("Done! Publications updated.")

if __name__ == "__main__":
    main()

