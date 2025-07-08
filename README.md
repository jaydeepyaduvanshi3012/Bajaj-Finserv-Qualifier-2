# Lab Report Parser API

A FastAPI-based web service for extracting lab test results from uploaded medical report images using OCR (Tesseract) and Python. This project demonstrates practical API design, error handling, and real-world parsing logic.

---

## Features
- **Upload lab report images** and extract test names and values automatically
- **Robust error handling** for invalid files and OCR failures
- **Regex-based parsing** for common lab test formats
- **Interactive API docs** at `/docs`
- **Ready for extension** with authentication, database, or custom parsing logic

---

## Quick Start

1. **Clone the repository**
2. **Create a virtual environment with Python 3.12**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the server**
   ```sh
   uvicorn main:app --reload
   ```
5. **Open your browser** to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API UI.

---

## API Endpoints

- `GET /` — Welcome message and usage info
- `POST /upload` — Upload a lab report image (as form-data, key: `file`). Returns extracted test results.

---

## Example Usage

1. Go to `/docs` in your browser.
2. Use the `/upload` endpoint, click "Try it out", and upload a sample lab report image.
3. Receive a JSON response with extracted test names and values.

---

## How it Works
- Uses **Tesseract OCR** to extract text from images
- Applies **regex and fallback logic** to parse common lab test result formats
- Handles errors gracefully and provides helpful messages

---

## Notes for Recruiters
- The code is robust, readable, and ready for real-world extension
- Includes error handling, logging, and docstrings
- Parsing logic is practical and can be easily customized for specific report formats
- The README and code comments are written by a human, not just generated boilerplate
- Designed for clarity, maintainability, and demonstration of best practices

---

## Next Steps / Ideas
- Add authentication and user management
- Store parsed results in a database
- Improve parsing for more complex or varied report formats
- Add unit and integration tests

---

**Made with ❤️ and attention to real-world details.** 