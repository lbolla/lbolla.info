---
title: Digital Garden
date: 2026-03-28
tags:
- obsidian
- pkm
---
[lbolla.info](https://lbolla.info) is now based on  [Obsidian's Digital Garden](https://github.com/oleeskild/obsidian-digital-garden). Previously, my notes were written in [orgmode](https://orgmode.org/) as `.org` files. Here are the most important steps I followed to convert them.
## From org to md
I used  [pandoc](https://pandoc.org/) to convert from `org` to `md`, something like:
```
pandoc --from=org --to=markdown file.org -o file.md -s ...
```
The conversion is not perfect and required some cleanup to remove spurious "block" elements in the output.
## Obsidian
I created a new [Obsidian](https;//obsidian.md) vault in the directory containing the `.md` files.
I then installed the [Obsidian's Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) plugin and configured to publish the notes to [Netlify]({{< relref "blog/Netlify.md" >}}).

I further cleaned up my notes by asking [Gemini](https://gemini.google.com) to tag the notes according to their content, e.g. {{< tag "python" >}} or {{< tag "programming" >}}.

The notes sources are hosted on Github: https://github.com/lbolla/digitalgarden
## Workflow
The writing workflow is now pretty simple.
- I create a new note in the Obsidian vault
- When ready to publish it, I tag it with `dg-publish`
- I invoke the "Digital Garden > Publish" command in Obsidian, which pushes the changes to Github.
- [Netlify]({{< relref "blog/Netlify.md" >}}) triggers a deployment of the notes, which are published in a few seconds
## Next steps
Write more! There is a much lower barrier of entry to write more now.
- Keep a reading log
- Keep track of what I learn about e.g. AI
- Maybe keep a gym journal
- Ultimately, create a [zettlekasten](https://en.wikipedia.org/wiki/Zettelkasten) of notes and build a [knowledge graph](https://en.wikipedia.org/wiki/Knowledge_graph)