# Profile Setup and Maintenance

How to publish this profile on GitHub and keep it healthy.

## What is in this folder

| File | Purpose |
|---|---|
| `README.md` | The profile page itself. GitHub shows it at the top of `github.com/mrfaizan-dev`. |
| `assets/profile-banner.svg` | Hero banner with a built-in typing animation and a neural-network graphic. |
| `assets/profile-footer.svg` | Matching footer with a slow flowing line. |
| `assets/ai-architecture.svg` | Five-layer map of the tools you work with, used in the AI and LLM Ecosystem section. |
| `tools/generate_assets.py` | Optional. Regenerates the three SVGs if you want to change the typing phrases. Safe to delete. |
| `PROFILE_SETUP.md` | This guide. You can leave it out of the published repo. |

## 1. Publish the profile

GitHub shows a repository's README on your profile when the repository is **public** and named **exactly the same as your username**.

1. Go to <https://github.com/new>.
2. Repository name: `mrfaizan-dev`. GitHub will show a note that this is a special repository.
3. Choose **Public**. Leave "Add a README file" **unchecked**, then create the repository.
4. Upload the files, using either method.

**Option A: command line**

```bash
git clone https://github.com/mrfaizan-dev/mrfaizan-dev.git
cd mrfaizan-dev
# copy README.md, assets/ and (optionally) tools/ into this folder
git add README.md assets tools
git commit -m "Add profile README"
git push origin main
```

**Option B: browser**

Open the new repository, choose **Add file → Upload files**, and drag in `README.md` and the `assets` folder (keep the folder structure). Commit to `main`.

5. Open <https://github.com/mrfaizan-dev> and hard-refresh (Ctrl+Shift+R). GitHub caches images, so allow a minute if the banner is slow to appear.

## 2. Set up the rest of your profile

These live in **Settings → Public profile**, not in the README.

- **Name:** `Mr Faizan`
- **Pronouns:** `he/him`
- **Bio** (limit 160 characters; this one is 107):
  `Python Backend & Applied AI Developer | Agentic AI, LLM Applications, RAG, Web Automation & Data Extraction`
- **Public email:** choose `pakmrfaizan@gmail.com` if you want it shown in the sidebar. It already appears in the README.
- **Pinned repositories:** on your profile choose **Customize your pins** and pin `Natural-Scraping-AI` and `Enterprise-RAG-AI`.

## 3. Strengthen the two featured repositories

Visitors who click through from the profile land on these repositories, so they matter as much as the profile does.

- **Enterprise-RAG-AI has an empty README** (it contains only the title). The profile describes it from the source code, but the repository itself should explain what it does. The Natural-Scraping-AI README is a good template to follow: overview, architecture, quick start, API endpoints and configuration (`GEMINI_API_KEY`, `COHERE_API_KEY`, `GROQ_API_KEY` or `GROQ_API_KEYS`, `REDIS_URL`).
- **Add a one-line description and topics** in each repository's "About" panel (the gear icon beside it). Suggested topics:
  - Natural-Scraping-AI: `web-scraping`, `playwright`, `seleniumbase`, `fastapi`, `celery`, `redis`, `nextjs`, `python`
  - Enterprise-RAG-AI: `rag`, `llamaindex`, `hybrid-search`, `chromadb`, `fastapi`, `celery`, `document-intelligence`, `python`
- **Check for secrets.** Neither repository should contain real API keys. Keep them in `.env` files that are listed in `.gitignore`.

## 4. Keep the profile accurate

The README only claims things that can be checked in your code or that you supplied directly. When you add to it, keep to that rule.

**Adding a project.** Copy one of the project cards in `README.md` (each is a single `<table>`), then change the title, link, bullets and badges. Describe only what the code does.

**Adding a skill.** Add a badge line inside the matching category block in the "Technical Arsenal" section. Badge URLs follow this pattern:

```text
https://img.shields.io/badge/<Label>-<HexBackground>?style=flat-square&logo=<simple-icons-slug>&logoColor=<HexLogo>
```

Spaces become `_` and a literal `-` becomes `--`. Logos come from [Simple Icons](https://simpleicons.org/). If a tool has no logo there (Playwright, LlamaIndex and Groq are examples), leave the `logo=` part out and the badge is simply text.

**Changing the typing phrases.** Edit `PHRASES` at the top of `tools/generate_assets.py` (33 characters per phrase at most), then run:

```bash
python tools/generate_assets.py
```

This rewrites the three SVGs in `assets/`. Commit them as usual.

**Changing the static text** (the headline or the small tagline in the banner) is a plain find-and-replace inside the SVG, but regenerating with the script keeps everything aligned.

## 5. Brand reference

| Role | Colour |
|---|---|
| Background | `#0B1020` |
| Secondary | `#111827` |
| Electric blue | `#3B82F6` |
| Cyan | `#22D3EE` |
| Violet | `#8B5CF6` |
| Light text | `#E5E7EB` |
| Muted text | `#94A3B8` |

Badge fills use darker tints of the same hues (`#1E3A8A`, `#155E75`, `#4C1D95`) so they stay readable on both GitHub's light and dark themes.

## 6. How it is built, and what can fail

- **SVGs are self-contained.** No JavaScript, no external fonts or images. The typing line is a native SVG (SMIL) animation, so no third-party typing service is involved. If a viewer does not play SVG animation, the banner shows the first phrase fully typed.
- **Badges** come from Shields.io. If the service is down, each badge falls back to its alt text, which still names the technology.
- **The Languages card** comes from the public `github-readme-stats` service, which is occasionally rate-limited. If it fails, only the alt text and the "browse the repositories directly" link show. You can delete that whole section from the README without affecting anything else.
- **Images not showing at all?** Check that the repository is public, the branch is `main`, and the folder is named `assets` in lowercase (paths are case-sensitive).

## 7. Deliberately left out

- **Contribution snake / GitHub Actions workflow.** It would add a third-party action and a scheduled job for little benefit while the account is new.
- **Contribution streak and total-commit cards.** Raw counts would highlight how new the account is. The Languages card shows what you work in without that.
- **LinkedIn, X, Discord and portfolio links.** None were supplied. When you have them, add them next to the email badge in the Contact section.
- **Visitor counters.**

If your activity grows and you would like a stats card later, this block can go beside the Languages card:

```html
<img src="https://github-readme-stats.vercel.app/api?username=mrfaizan-dev&show_icons=true&hide_border=true&bg_color=0B1020&title_color=22D3EE&icon_color=8B5CF6&text_color=E5E7EB&ring_color=3B82F6" alt="GitHub stats for mrfaizan-dev" width="49%">
```
