# Image search API — examples

Google Images results for a query — thumbnail, source page and host.

**Live page, full schema & pricing → [quanticdata.io/collectors/image-scraper-api/](https://quanticdata.io/collectors/image-scraper-api/)**

Searches the Google Images vertical and delivers each result with its title, thumbnail URL, the page hosting it and that page's host. Served by the HTTP tier (no browser), so it stays cheap at dataset volume. Full-size image URLs are returned only when Google exposes them.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/search_images/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "proxy server diagram", "country": "us", "max_results": 20}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — What to search, e.g. "proxy server diagram".
- `country` (string) — ISO 3166-1 alpha-2 code — proxy exit geo and Google locale (gl). Omit for the default pool.
- `lang` (string) — Interface language (hl), e.g. en, it, de.
- `max_results` (integer) — How many images to deliver at most (1–100). You pay only for delivered images.

## Output — one row per image

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `title` | string | Image title as shown. |
| `thumbnail` | string | Thumbnail URL (always present in the grid). |
| `image` | string | Full-size image URL when Google exposes it. |
| `source` | string | Host of the page showing the image. |
| `source_url` | string | URL of the page showing the image. |

## Pricing

**$0.0003 per delivered image** ($0.3 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 6,666 images — no card required.

## Links

- This collector: https://quanticdata.io/collectors/image-scraper-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
