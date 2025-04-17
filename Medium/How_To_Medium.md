

#######

## make `.md` format as follows:

```
---
title: "Article Name"
author: "Claudia G. Petersen"
date: "2025-MM-DD"
---

# Provocative But Open Ended Article Name

## Witty, Catchy Subtitle

Content starts here...

*Bold* _italic_ 

`code block`

DO NOT:

### Big [wont publish]

--- [doesn't separator line/may not publish cos thinks is metadata]

*_BoldItalic_* [doesn't]

```

#######


## When done:

#######

- to preview, copy title of `.md` to a temp `.txt` as `Article_Name`
- use to paste into the following and run `pandoc Article_Name.md -o Article_Name.html`
- and article will appear as `Article_Name.html` in same folder

### if satisfied can then upload `.md` to:
`https://whisprer.github.io/Medium-Posts`

### 1. by:
- creating repo named `article-name` [note lc and kebab case]
- committing
- it will appear online at:
`https://whisprer.github.io/Medium-Posts/article-name`


#######

### 2. Bonus: One-Click Debug Fix

- ensure git is installed

Run this in your project root:
```
mkdir -p docs/article-name
pandoc Article_Name.md -o Medium-Posts/article-name.md
git add Medium-Posts/article-name.md
git commit -m "Add article-name as md post"
git push origin main
```

### 3. or fill in and run:
`C:\Users\user\documents\writings\Medium\deploy-to-pages.sh`

either route;
- Then wait ~30s,
- goto github.com/name/
- goto settings for Medium-Posts repo and select 'page' from left menu
- ensure is set to main; root; saved.
- goto:

`https://whisprer.github.io/Medium-Posts/article-name`

will be visble _publicly_ so remove after uploading to Medium!
[this means the repo must be public]


#######

- goto G-Petey and get him to do a DALL-E pic for the main pic
- make any other pics needed/generate with DALL-E/wiki commons/etc.
- add 'em to folder so you know where they are ready


#######

then goto Medium → Profile Pic → Stories → “Import a Story”

- do any final necessary formatting/add pics etc.
- preview and check
- publish
- add tags [hint: type word, look for big number - pick it]
- done

Check its ok - you can still edit to your hearts desire for as long as you like if its still up there!


#######

Here's a tidy lil’ cleanup script for your local repo that will:

- Delete a given .md file
- Commit the change with a nice lil message
- Push the update to GitHub to remove it from the public GitHub Pages site
- You can run this on any .md you’ve already deployed and imported to Medium.

medium_cleanup.py (Python CLI Script)
```
Python [Copy/Edit]

import os
import subprocess
import sys

def delete_markdown_file(filename):
    if not filename.endswith(".md"):
        print("🚫 Please provide a markdown file ending in .md")
        return

    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return

    try:
        # Delete the file
        os.remove(filename)
        print(f"🗑️ Deleted {filename}")

        # Stage the deletion
        subprocess.run(["git", "rm", filename], check=True)
        print("📦 Staged the file for removal.")

        # Commit the change
        commit_msg = f"Remove published Medium article: {filename}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print("✅ Committed changes.")

        # Push to GitHub
        subprocess.run(["git", "push"], check=True)
        print("🚀 Pushed to GitHub.")

    except subprocess.CalledProcessError as e:
        print(f"❗ Git error: {e}")
    except Exception as e:
        print(f"💥 Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python medium_cleanup.py <filename.md>")
    else:
        delete_markdown_file(sys.argv[1])
```

How to use it:
Save that script as medium_cleanup.py inside your local repo (same folder as your .md files).

Open a terminal and navigate to your repo folder:
```
bash [Copy/Edit]
cd path/to/your/medium-posts
```

Run it like this:
```
bash [Copy/Edit]
python medium_cleanup.py vibe-coding.md
```

That’s it — the script will handle deletion, git staging, commit, and push!


#######

