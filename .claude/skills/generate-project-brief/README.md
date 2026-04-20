Generates a Project Brief for the current project. The brief documents essential project information — product overview, team, tech stack, key links — so any Oak's Lab team member can quickly get up to speed. The generated brief is saved to `docs/project-brief.md` in the repo and published to Outline for the full team.

## How to use

1. Download the existing Project Brief page from Confluence as a DOC file (e.g. https://oakslab.atlassian.net/wiki/spaces/OL/pages/3501261364/OpenLoop+1+Intake+A4).
2. Upload it to GDrive, open it in Google Docs, and export it as a Markdown file. Save it to `docs/project-brief-tmp.md`.
3. Run the skill:
```
/generate-project-brief generate the Project Brief for this project based on all the MD files you see in the project structure (mainly in the docs folder). For links take links from @docs/project-brief-tmp.md
```