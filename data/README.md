# Data

Sample satellite imagery and QA datasets go here. **Not committed to git** — too large.

## Free imagery sources
- Copernicus Open Access Hub (Sentinel-2 optical + SAR): https://dataspace.copernicus.eu
- USGS Earth Explorer (Landsat): https://earthexplorer.usgs.gov
- NASA Worldview (quick visual samples, no account needed): https://worldview.earthdata.nasa.gov

## QA / training datasets
- RSVQA: https://rsvqa.sylvainlobry.com
- GeoChat instruction dataset: https://huggingface.co/datasets/MBZUAI/GeoChat_Instruct

## Suggested layout
```
data/
├── raw/          # untouched downloaded imagery
├── processed/    # tiled / NDVI-NDWI processed outputs
└── samples/      # 3-5 small images kept for quick demo/testing (keep these tiny)
```

## Tip for the demo
Pick 2-3 known-good sample images ahead of time (e.g. one with an obvious flood, one with visible ships) and test your exact demo queries against them repeatedly — don't rely on a random image working live.
