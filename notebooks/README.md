# Notebooks

Colab/Kaggle notebooks for experiments that don't belong in the main backend yet:
- Initial VLM inference tests
- LoRA fine-tuning runs
- SAM 2 mask quality checks
- Tiling/NDVI script prototyping before porting into `backend/app/preprocessing.py`

## Convention
Name notebooks `NN_short-description.ipynb` (e.g. `01_vlm_baseline_test.ipynb`, `02_sam2_mask_test.ipynb`) so the team can tell execution order at a glance.

## Getting a free GPU
- **Google Colab**: colab.research.google.com → Runtime → Change runtime type → GPU (T4 free tier)
- **Kaggle**: kaggle.com/code → New Notebook → Settings → Accelerator → GPU T4 x2 (free, ~30 hrs/week)

Kaggle's free tier tends to give more consistent GPU access during busy periods than Colab's free tier.
