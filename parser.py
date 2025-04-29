import pytesseract
from PIL import Image

def parse_lab_tests(image: Image):
    # Use Tesseract to extract text from the image
    text = pytesseract.image_to_string(image)

    # Example parsing logic - you should customize this based on the format of your reports
    # For instance, extracting test names and values from the text
    parsed_data = {}
    lines = text.split("\n")
    for line in lines:
        if "Test" in line:
            test_name = line.split(":")[0].strip()
            test_value = line.split(":")[1].strip() if ":" in line else "Not found"
            parsed_data[test_name] = test_value

    return parsed_data

