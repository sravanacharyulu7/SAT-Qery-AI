# SatQuery AI
**SIH26167** — A conversational Vision-Language Assistant for satellite & geospatial imagery.

Upload a satellite image, ask a question in plain English ("Highlight flooded areas near the river", "Count the cargo ships in the bay"), and get back a text answer + a visual overlay (bounding box / segmentation mask) showing exactly what the model found.

## Architecture

```
[User Query] ──> [Geospatial Router]
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 [Tiled Multi-Scale VLM]       [Band Processing & Geo-RAG]
 (Handles high-res imagery)    (NIR/SAR + historical context)
        │                               │
        └───────────────┬───────────────┘
                        ▼
      [Grounding & SAM 2 Mask Engine]
   (Prevents hallucination via pixel-confirmed overlays)
```

See [`docs/architecture.md`](docs/architecture.md) for the full breakdown.

## Repo Structure

```
satquery-ai/
├── backend/        FastAPI service: router, VLM inference, SAM 2, Geo-RAG
│   └── app/         Application code
├── frontend/        React/Next.js UI with Mapbox/Leaflet overlay
├── models/          Pretrained + fine-tuned model weights (gitignored)
├── data/            Sample satellite imagery & datasets (gitignored)
├── notebooks/       Colab/Kaggle notebooks for experiments & fine-tuning
└── docs/            Architecture notes, API spec, demo script
```

## Team & Roles

| Role | Owns | Name |
|---|---|---|
| ML/CV Engineer | VLM fine-tuning, PyTorch pipeline | _TBD_ |
| Computer Vision Engineer | SAM 2, tiling, band processing (NDVI/NDWI) | _TBD_ |
| Backend Developer | FastAPI, router, vector DB (Qdrant) | _TBD_ |
| Frontend Developer | React/Next.js, Mapbox/Leaflet UI | _TBD_ |
| GIS/Domain Lead | Dataset selection, sanity-checking outputs | _TBD_ |
| Pitch/Demo Lead | Deck, demo script, judging Q&A prep | _TBD_ |

> Fill in names, then delete this note. One person can hold two roles on a small team — just make sure every row has an owner.

## Getting Started

### 1. Clone & branch
```bash
git clone <your-repo-url>
cd satquery-ai
git checkout -b feature/<your-name>-<short-task>
```

### 2. Backend setup
```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend setup
```bash
cd frontend
npm install
npm run dev
```

### 4. Models & data
See [`models/README.md`](models/README.md) and [`data/README.md`](data/README.md) — these folders are gitignored on purpose, don't commit large weights or imagery.

## Tech Stack

| Layer | Technology |
|---|---|
| VLM | Qwen2.5-VL / LLaVA-NeXT / GeoChat |
| Segmentation | SAM 2 / Lang-SAM |
| Geospatial processing | GDAL, Rasterio, TorchGeo, OpenCV |
| Vector DB | Qdrant / PostGIS + pgvector |
| Backend | FastAPI, PyTorch, Ray/Triton |
| Frontend | React/Next.js, Mapbox GL JS / Leaflet |

## License
TBD — add before public submission.
