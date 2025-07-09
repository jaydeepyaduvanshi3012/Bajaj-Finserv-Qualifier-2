from fastapi import FastAPI, UploadFile, File, HTTPException
from parser import parse_lab_tests
import io
from PIL import Image
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

# The FastAPI app has been moved to api/index.py for Vercel deployment.
# Please use that file as the entry point for the API.

if __name__ == "__main__":
    print("The FastAPI app is now located in api/index.py for Vercel deployment. Run and deploy from there.")

@app.get("/")
def read_root():
    """
    Root endpoint providing a welcome message and API usage info.
    """
    return {"message": "Welcome to the Lab Report Parser API! Use the /upload endpoint to extract lab test data from an image. Visit /docs for API documentation."}

@app.post("/upload")
async def upload_lab_report(file: UploadFile = File(...)):
    """
    Endpoint to upload a lab report image and extract lab test data.
    Accepts image files and returns parsed test results.
    """
    try:
        # Read the image data from the uploaded file
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        logging.error(f"Failed to read or open image: {e}")
        raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")

    # Process the image to extract lab test data
    extracted_data = parse_lab_tests(image)

    if 'error' in extracted_data:
        logging.error(f"OCR error: {extracted_data['error']}")
        raise HTTPException(status_code=500, detail=extracted_data['error'])

    return {"extracted_data": extracted_data}

