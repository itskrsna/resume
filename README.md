# Resume & Cover Letters

LaTeX resume (AltaCV) and cover letters, built automatically by GitHub Actions and
published to GitHub Pages. **Everything can be done in the browser. No local setup is needed.**

## Hosted site

Landing page with view/download buttons for every PDF: **https://itskrsna.github.io/resume/**

It is generated from `site/index.html` (edit it in the browser like any other file) and
deployed to the `gh-pages` branch together with the PDFs.

## Published PDFs

Replace the path if the Pages URL differs: Settings > Pages shows the actual address.

| File | Link |
| --- | --- |
| Resume (cloud profile, default) | https://itskrsna.github.io/resume/krishnakishore.pdf |
| Cover letter (cloud template) | https://itskrsna.github.io/resume/cover-letter-cloud.pdf |

The **AI profile** (`krishnakishore-ai.pdf`, `cover-letter-ai.pdf`, includes the freelance role and
GenAI content) is built on every run but **not published**. Download it from the run's
**pdfs** artifact in the Actions tab when you need it.

## Where things live

| Path | What it is |
| --- | --- |
| `resume/krishnakishore.tex` | Main resume (public cloud profile by default). AI-only text is wrapped in `\ifshowai ... \fi`. |
| `resume/roles/ai.tex`, `resume/roles/cloud.tex` | Per-role tagline and skill tags. |
| `resume/krishnakishore-ai.tex` | Tiny wrapper that builds the private AI variant. |
| `resume/cover-letter-ai.tex`, `resume/cover-letter-cloud.tex` | Cover letter text per role. |
| `resume/letter-common.tex` | Shared letter layout (header, date, sign-off). |
| `site/index.html` | Landing page published at the site root. |
| `.github/workflows/main.yml` | Build and deploy pipeline. |

## Edit and save in the browser

1. Open the file on github.com, for example `resume/krishnakishore.tex`.
2. Click the **pencil icon** (Edit this file), or press `.` anywhere in the repo to open the
   web editor (github.dev, a VS Code-like editor).
3. Make your change.
4. **Save:**
   - On the file page: click **Commit changes...**, write a short message, choose
     **Commit directly to the `main` branch**, and click **Commit changes**.
   - In github.dev: open the Source Control tab (left sidebar), type a message, click
     **Commit & Push**.
5. Open the **Actions** tab. A "Build LaTeX" run starts (about 2 to 3 minutes). A green tick
   means the PDFs were rebuilt and published. Refresh the PDF link after a minute or two.

Tip: to try a change safely first, choose **Create a new branch and start a pull request**
at step 4. The build runs on the pull request without publishing. Merge it when it is green.

### LaTeX gotchas when editing

- Escape special characters: write `\&`, `\%`, `\$`, `\#`, `\_`.
- Don't end a line with a single `\`. Use `\\` for a line break, or leave a blank line.
- One `\item` per bullet inside `\begin{itemize} ... \end{itemize}`.
- The resume is meant to fit 2 pages and each letter 1 page. The build prints a warning
  if they run over.

## Common edits

- **Add or change a job bullet:** edit `resume/krishnakishore.tex`, under the right `\cvevent{...}` block.
- **Change tagline or skills for a role:** edit `resume/roles/ai.tex` or `resume/roles/cloud.tex`.
- **Add a new role profile (for example "data"):**
  1. Copy `resume/roles/cloud.tex` to `resume/roles/data.tex` and edit the tagline and tags.
  2. Copy `resume/krishnakishore-ai.tex` to `resume/krishnakishore-data.tex` and change `ai` to `data`.
     In the new role file, also define `\newif\ifshowai`, a `\showaitrue` or `\showaifalse` line, and `\roleacgtitle` (copy them from `roles/cloud.tex`).
  3. In `.github/workflows/main.yml`, add `krishnakishore-data.tex` to `root_file`, and
     add `krishnakishore-data` to the `for f in ...` validation list and the `upload-artifact` paths.

## Tailored cover letter for one job (not published)

1. **Actions** tab > **Build LaTeX** > **Run workflow**.
2. Fill in **company**, **position**, and the **template** (`ai` or `cloud`).
3. When the run finishes, open it and download the **tailored-cover-letter** artifact (a zip
   containing `cover-letter-custom.pdf`). Nothing is pushed to the public site.

## How the pipeline behaves

- **Push to `main`** (changes under `resume/`): compile all four PDFs, validate, publish to
  the `gh-pages` branch.
- **Pull request:** compile and validate only. Nothing is published.
- **Compile error:** the run fails and nothing is published, so the live PDFs are never replaced by a broken build.
  Open the failed run and look for the first line starting with `!` or containing `.tex:NN:`.
- **Re-running:** use **Run workflow** (or push a new commit). "Re-run jobs" on an old run
  rebuilds the *old* commit.
- Unchanged PDFs are skipped, so no empty deploy commit is made.
