# Models

This folder holds model weights. **Nothing here is committed to git** (see `.gitignore`) — weights are large and belong on Hugging Face Hub or a shared cloud drive, not in the repo.

## What to download

**Vision-Language Model (pick one to start with):**
- GeoChat: https://huggingface.co/MBZUAI/geochat-7B
- Qwen2.5-VL: https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- LLaVA-NeXT: https://huggingface.co/llava-hf/llava-v1.6-mistral-7b-hf

Start with the smallest/quantized variant available so it fits on a free Colab/Kaggle GPU.

**Segmentation (SAM 2):**
- Official repo + weights: https://github.com/facebookresearch/sam2
- Use the smallest checkpoint (`sam2_hiera_tiny` or similar) for fast iteration; swap to a larger one later if accuracy needs it.

## Folder layout (once populated)
```
models/
├── vlm/           # base or fine-tuned VLM checkpoint
├── sam2/          # SAM 2 weights
└── checkpoints/   # your fine-tuned LoRA adapters, if any
```

## Loading in code
Prefer loading straight from Hugging Face Hub (`from_pretrained("org/model-name")`) during development rather than manually downloading — it's simpler and the team stays in sync on versions.
