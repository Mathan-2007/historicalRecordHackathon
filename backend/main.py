from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import shutil
import uuid

from ocr import extract_text
from models import llama_process, deepseek_process, qwen_process
from consensus import consensus_output

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    path = f"temp_{file_id}.png"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # STEP 1: OCR
    raw_text = extract_text(path)

    # STEP 2: AI Models
    llama = llama_process(raw_text)
    deepseek = deepseek_process(raw_text)
    qwen = qwen_process(raw_text)

    # STEP 3: Consensus
    final = consensus_output([llama, deepseek, qwen])

    return {
        "ocr_text": raw_text,
        "llama": llama,
        "deepseek": deepseek,
        "qwen": qwen,
        "final_output": final
    }
