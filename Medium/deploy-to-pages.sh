#!/bin/bash

# Replace with your actual file/article names
ARTICLE_MD="Article_Name.md"
ARTICLE_SLUG="article-name"  # lowercase/kebab-case URL-safe folder name

# Create the target folder inside docs/
mkdir -p "Medium-Posts/$ARTICLE_SLUG"

# Convert to HTML and place in docs/{slug}/index.html
pandoc "$ARTICLE_MD" -o "Medium-Posts/$ARTICLE_SLUG/article-name.md"

# Stage, commit and push
git add "docs/$ARTICLE_SLUG/article-name.md"
git commit -m "Add $ARTICLE_SLUG as md post"
git push origin main
