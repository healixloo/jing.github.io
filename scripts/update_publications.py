#!/usr/bin/env python3
# coding: utf-8

"""
Update publications.md from Google Scholar.

Usage:
    python update_publications.py

Requirements:
    pip install scholarly

This script:
1. Fetches publications from your Google Scholar profile.
2. Writes them into publications.md with a compact layout.
"""

import os
import re
from scholarly import scholarly

# --- Config ---
SCHOLAR_ID = "1W_3YjAAAAAJ"   # your Google Scholar ID
OUTPUT_FILE = "publications.md"

def html_escape(text):
    """Escape HTML special characters for Markdown/HTML output."""
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return "".join(html_escape_table.get(c, c) for c in str(text))

def main():
    print("Fetching publications from Google Scholar...")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []
    for pub in author['publications']:
        bib = pub['bib']
        title = bib.get('title', 'Untitled')
        year = bib.get('pub_year', '')
        venue = bib.get('venue', '')
        authors = bib.get('author', '')

        # Build a compact entry
        entry = f"<p style='font-size:90%; margin-bottom:8px;'>"
        entry += f"<b>{html_escape(title)}</b><br>"
        entry += f"{html_escape(authors)} ({year}). "
        if venue:
            entry += f"<i>{html_escape(venue)}</i>"
        entry += "</p>"

        pubs.append(entry)

    # --- Write publications.md ---
    header = """---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">
    You can also find my articles on my
    <a href="{{ site.author.googlescholar }}">Google Scholar</a>.
  </div>
{% endif %}

"""
    body = "\n".join(pubs)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(header + body)

    print(f"Updated {OUTPUT_FILE} with {len(pubs)} publications.")

if __name__ == "__main__":
    main()
