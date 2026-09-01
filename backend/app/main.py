"""
SatQuery AI — Backend entrypoint.

Run with:
    uvicorn app.main:app --reload

This is a placeholder skeleton. Fill in:
  - app/router.py     -> decides which pipeline(s) a query needs
  - app/vlm.py        -> loads & runs the Vision-Language Model
  - app/segmentation.py -> loads & runs SAM 2 / Lang-SAM
  - app/preprocessing.py -> tiling, NDVI/NDWI, band handling
"""
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SatQuery AI", version="0.1.0")

# Allow the local frontend dev server to call this API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query")
async def query_satellite_image(
    image: UploadFile = File(...),
    question: str = Form(...),
):
    """
    Main endpoint: image + natural language question -> text answer + mask.

    TODO:
      1. Preprocess the uploaded image (preprocessing.py)
      2. Route the query (router.py)
      3. Run VLM inference (vlm.py)
      4. Run SAM 2 grounding on VLM output (segmentation.py)
      5. Return combined result
    """
    # Placeholder response so the frontend has something to render against
    # while the real pipeline is being built.
    return {
        "answer": f"(stub) Received question: '{question}' for image '{image.filename}'",
        "mask": None,
        "bounding_boxes": [],
    }
