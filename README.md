# Favored by the Father Ministries — Website

Modern, fast, static website for [Favored by the Father Ministries](https://favoredbythefather.com) and Rev. Dr. Barbara A. F. Brehon. A complete redesign of the original Squarespace site: multi-page structure, premium typography, elevated purple/butterfly brand identity, responsive layout, SEO metadata, and accessibility built in.

## Pages

| Page | Purpose |
|---|---|
| `/` | Home — ministry overview, what we do, featured book, retreat, podcast |
| `/about` | Dr. Brehon's bio, foundation / purpose / motto / mission, partner ministries |
| `/books` | All three book series + anthology contributions (Amazon links) |
| `/podcast` | UNBOXED on Purpose podcast, music (Here, in the Becoming), guest appearances |
| `/mentoring` | Brookside virtual mentoring, Haven for Ravens, Community of Prayer Circle |
| `/events` | 2026 events, Mini Masterclass Series, Chat & Chew, Fall Spiritual Retreat, past events |
| `/testimonials` | Testimonies + share-your-journey CTA |
| `/contact` | Email, Calendly booking, prayer requests, app downloads, giving, socials |

## Tech

- **Pure static HTML/CSS/JS** — no framework. Fast, cheap, zero maintenance.
- `build.py` + `pages_*.py` — a tiny Python generator that assembles the shared header/footer around each page's content and writes the finished site into `public/`. Edit a `pages_*.py` file and run `python3 build.py` to regenerate. Vercel runs this automatically on every deploy (`buildCommand: python3 build.py`, output directory `public`).
- `vercel.json` — clean URLs, security headers, cache headers, and redirects from the old Squarespace URL structure (`/home`, `/testimonial`, etc.).
- Fonts: Cormorant Garamond, Outfit, Great Vibes (Google Fonts).

## Deploying

Deployed on [Vercel](https://vercel.com). Any push to `main` redeploys automatically once the repo is connected to a Vercel project. To point the real domain: add `favoredbythefather.com` in Vercel → Project → Settings → Domains, then update DNS at the registrar.

## ⚠️ Image assets

Images are currently hot-linked from the existing Squarespace CDN (`images.squarespace-cdn.com`). **Before cancelling the Squarespace subscription**, download the images referenced in the pages and move them into an `/assets` folder in this repo (then update the `src` URLs, or re-run the generator after editing the `IMG` map in `build.py`).

## Forms

By design there is no form backend: contact, testimonials, and prayer actions use email (`barbara@favoredbythefather.com`), Calendly, and the existing prayer-wall service. If real forms are wanted later, Formspree or a Vercel serverless function + Resend are easy drop-ins.
