import pytesseract
from PIL import Image
from typing import Dict, Any
import re

def parse_lab_tests(image: Image.Image) -> Dict[str, Any]:
    """
    Extracts lab test names and values from a lab report image using OCR.
    Attempts to handle common lab report formats and provides basic error handling.
    Args:
        image (PIL.Image.Image): The image of the lab report.
    Returns:
        dict: A dictionary mapping test names to their values.
    """
    try:
        # Use Tesseract to extract text from the image
        text = pytesseract.image_to_string(image)
    except Exception as e:
        return {"error": f"OCR failed: {str(e)}"}

    parsed_data = {}
    # Example regex for common lab test lines: "Hemoglobin: 13.5 g/dL"
    pattern = re.compile(r"([A-Za-z0-9\s\-]+):\s*([\d\.]+\s*[a-zA-Z\/%]*)")
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = pattern.match(line)
        if match:
            test_name = match.group(1).strip()
            test_value = match.group(2).strip()
            parsed_data[test_name] = test_value
        else:
            # Try to handle lines without colon, e.g., "WBC 5.2 x10^3/uL"
            tokens = line.split()
            if len(tokens) >= 2 and re.match(r"^[\d\.]+", tokens[1]):
                test_name = tokens[0]
                test_value = ' '.join(tokens[1:])
                parsed_data[test_name] = test_value
    if not parsed_data:
        parsed_data["note"] = "No recognizable lab test data found. Please check the image quality or format."
    return parsed_data

