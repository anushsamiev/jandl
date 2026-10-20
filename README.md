# J&L Bail Bonds — website

Static marketing site for J&L Bail Bonds, 400 Texas St Suite 570, Shreveport, LA 71101.
No framework, no build dependencies beyond Python 3. Hosts anywhere that serves static files.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Home: hero, trust strip, 3-step process, cost table, services, jails, reviews, about teaser, call-to-action |
| `how-bail-works.html` | Long-form explainer with a live premium estimator (12% rule), checklist, timing, after-release |
| `services.html` | Bond types (misdemeanor, felony, DWI, domestic, drug, probation holds), warrant walk-throughs, payment options |
| `jails.html` | Facilities served with addresses and phone numbers |
| `about.html` | Story, four promises, directions to the office |
| `faq.html` | Accordion FAQ grouped by cost, timing, co-signing, after release |
| `contact.html` | Phone-first contact, embedded Google Map, non-urgent message form |
| `thanks.html`, `privacy.html`, `404.html` | Supporting pages |

## Editing

- Page content lives in `src/pages/*.html` (body only, with a small JSON header for title and description).
- Shared header, footer, and `<head>` live in `src/partials/`.
- Styles: `src/assets/css/site.css`. Script: `src/assets/js/site.js`.
- Site-wide values (phone number, domain) are set once at the top of `build.py`.
- Run `python3 build.py` to regenerate the pages at the repo root. GitHub Pages serves them from `main` with the folder set to `/ (root)`.

## Before launch (placeholders to replace)

1. **Phone number.** `build.py` uses `(318) 555-0199`. Replace `phone` and `tel` with the real number.
2. **Domain and indexing.** Set `site_url` in `build.py` and change `robots` to `index, follow`. The draft preview is set to noindex.
3. **Photos.** Drop real photos into `src/assets/img/` using the names in `src/assets/img/README.md`. Until then each slot shows a designed navy panel, so the site never looks broken.
4. **Reviews.** Paste two or three real Google reviews into the reviews section of `src/pages/index.html` (marked with a TODO comment). Never invent reviews.
5. **About copy.** Replace the "How we work" section in `src/pages/about.html` with the owners' real story (names, years in business).
6. **Bossier addresses.** `src/pages/jails.html` has TODO comments where the Bossier Parish and Bossier City jail addresses and phone numbers go. Confirm with the Bossier Sheriff's Office and Bossier City Police.
7. **Contact form.** Works out of the box on Netlify (Netlify Forms). On another host, point the form `action` at a Formspree or Basin endpoint.
8. **Verify these claims with the client:** payment plans offered, cards accepted, electronic signing, parishes served beyond Caddo and Bossier, "steps from the Caddo Parish Courthouse" (the courthouse is at 501 Texas St).

## Facts baked in (with sources)

- Louisiana bail premium: 12% of the bond or $120 minimum, La. R.S. 22:1443.
- Caddo Correctional Center: 1101 Forum Dr, Shreveport, LA 71107, (318) 677-5254 (Caddo Sheriff's Office site).
- Shreveport City Jail: 755 Hope St, Shreveport, LA 71101, jail desk (318) 673-7130 (City of Shreveport site).

## Hosting

Any static host. Netlify or Cloudflare Pages: publish directory `/` (repo root), no build command needed .
Add a custom 404 by pointing the host at `404.html`.
