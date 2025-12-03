import os
from django.shortcuts import render
from django.conf import settings
from pdf2image import convert_from_path
import pytesseract
import easyocr
from paddleocr import PaddleOCR

# Add Surya OCR import if available
# import suryaocr

def ocr_test(request):
    data_dir = settings.MEDIA_ROOT
    pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith('.pdf')]
    results = {}
    for pdf_file in pdf_files:
        pdf_path = os.path.join(data_dir, pdf_file)
        images = convert_from_path(pdf_path)
        page_results = []
        for img in images:
            img_path = os.path.join(data_dir, 'temp_page.png')
            img.save(img_path)
            ocr_outputs = {}
            # Tesseract
            ocr_outputs['Tesseract'] = pytesseract.image_to_string(img)
            # EasyOCR
            reader = easyocr.Reader(['en'])
            ocr_outputs['EasyOCR'] = ' '.join([text for _, text, _ in reader.readtext(img_path)])
            # PaddleOCR
            paddle_ocr = PaddleOCR(use_angle_cls=True, lang='en')
            paddle_result = paddle_ocr.ocr(img_path, cls=True)
            paddle_text = ' '.join([line[1][0] for line in paddle_result[0]])
            ocr_outputs['PaddleOCR'] = paddle_text
            # Surya OCR (if available)
            # ocr_outputs['SuryaOCR'] = suryaocr.ocr(img_path)
            page_results.append(ocr_outputs)
            os.remove(img_path)
        results[pdf_file] = page_results
    return render(request, 'ocr_app/ocr_results.html', {'results': results})
