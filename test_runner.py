import os
import requests

# URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/upload"

# Directory where your images are stored
image_directory = "/home/jaydeepyaduvanshi/bajaj 2/lab_reports_samples"

# Loop through all image files in the directory
for image_filename in os.listdir(image_directory):
    # Check for image files (you can add other image formats if needed)
    if image_filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_path = os.path.join(image_directory, image_filename)
        
        # Open the image file in binary mode and send it to the FastAPI endpoint
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file})
        
        # Print the server's response (should be JSON containing parsed data)
        print(f"Response for {image_filename}:")
        print(response.json())



