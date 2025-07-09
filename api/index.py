from fastapi import FastAPI, UploadFile, File, HTTPException
from parser import parse_lab_tests
import io
from PIL import Image
import logging
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Lab Report Parser API! Use the /upload endpoint to extract lab test data from an image. Visit /docs for API documentation."}

@app.post("/upload")
async def upload_lab_report(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        logging.error(f"Failed to read or open image: {e}")
        raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")

    extracted_data = parse_lab_tests(image)

    if 'error' in extracted_data:
        logging.error(f"OCR error: {extracted_data['error']}")
        raise HTTPException(status_code=500, detail=extracted_data['error'])

    return JSONResponse(content={"extracted_data": extracted_data})

handler = Mangum(app) 