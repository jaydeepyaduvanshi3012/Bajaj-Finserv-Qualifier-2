from fastapi import FastAPI, UploadFile, File
from parser import parse_lab_tests
import io
from PIL import Image

app = FastAPI()

@app.post("/upload")
async def upload_lab_report(file: UploadFile = File(...)):
    # Read the image data from the uploaded file
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    # Process the image to extract lab test data
    extracted_data = parse_lab_tests(image)

    return {"extracted_data": extracted_data}

