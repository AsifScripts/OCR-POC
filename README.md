# Text2Image_OCR

## Project Overview
This Django-based project is designed to test and compare multiple OCR libraries for extracting text from images embedded in PDF documents. The goal is to evaluate the accuracy and structure of the output from each OCR engine.

## Data Storage
- All PDF images for testing should be placed in the `data/` folder inside the project directory: `Text2Image_OCR/data/`
- The results of OCR processing will also be stored in organized subfolders within `data/` (e.g., `data/results/`).

## Workflow
1. Add your PDF images to the `data/` folder.
2. Run the provided script/app to process all PDFs using the supported OCR libraries.
3. Compare the raw text output from each OCR engine.

## Supported OCR Libraries
- Tesseract (pytesseract)
- PaddleOCR
- EasyOCR
- Surya OCR
- pdf2image (for PDF to image conversion)
- Additional libraries can be added as needed

## Next Steps
- Add your PDF images to the `data/` folder.
- Follow instructions in the script/app to run OCR and view results.

## Collaboration
- The project is structured for easy collaboration via GitHub branches.
- Please commit changes to your respective branch and follow standard pull request workflows.

---
For any questions or setup issues, please contact the project maintainer.