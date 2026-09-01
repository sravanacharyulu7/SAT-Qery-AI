# Architecture

## Pipeline

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

## Component notes

**Geospatial Router** — decides whether a query needs the VLM path, the Geo-RAG/temporal path, or both (e.g. "how much forest was lost between 2022-2024" needs Geo-RAG; "count the ships in this image" needs only the VLM path).

**Tiled Multi-Scale VLM** — satellite images can be 10,000×10,000+ px. We split into overlapping tiles, run inference per tile, and merge results, so small objects (cars, boats) don't vanish from downsampling.

**Band Processing & Geo-RAG** — non-RGB data (NIR, SAR, thermal) gets converted to false-color composites or indices (NDVI, NDWI) before reaching the VLM. Geo-RAG stores historical imagery + metadata in a vector DB for change-detection queries.

**Grounding & SAM 2 Mask Engine** — the anti-hallucination layer. The VLM isn't allowed to claim an object exists unless SAM 2 confirms a pixel-level mask for it. This is what turns "the model said so" into "the model can show you exactly where."

## Key technical risks (track these explicitly)
| Risk | Mitigation |
|---|---|
| Small objects lost at scale | Dynamic tiling + sliding window |
| Non-RGB channel mismatch | Rasterio preprocessing → FCC/NDVI before VLM input |
| Hallucination on dense scenes | Grounding-driven verification against SAM 2 output |
| GPU memory limits (VLM + SAM 2 together) | Use quantized/smaller checkpoints during dev; batch carefully |
