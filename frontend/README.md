# Frontend

React/Next.js UI: image upload, chat input, map with mask overlay.

## Setup
```bash
npm install
npm run dev
```
Runs at http://localhost:3000, expects the backend at http://localhost:8000 (see `backend/app/main.py`).

## Mapbox token
Sign up free at https://mapbox.com, grab an access token, and put it in `.env.local`:
```
NEXT_PUBLIC_MAPBOX_TOKEN=your_token_here
```
(Leaflet is a free/no-token alternative if you'd rather skip this step — swap `react-map-gl` for `react-leaflet` in package.json.)

## Suggested first component
`pages/index.js` (or `app/page.js` if using the App Router):
- File upload input for the satellite image
- Text input for the question
- POST to `http://localhost:8000/query` with `FormData`
- Render the returned `answer` text + overlay `mask`/`bounding_boxes` on the image
