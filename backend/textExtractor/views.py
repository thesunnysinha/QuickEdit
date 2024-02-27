import urllib.parse
import io
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image
import pytesseract
import PyPDF2

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def textExtractor(request):
    if request.method == 'POST' and request.FILES['image']:
        # Get the uploaded image from the request
        uploaded_image = request.FILES['image']

        # Get the filename and encode it correctly
        filename = urllib.parse.quote(uploaded_image.name)

        # Save the image to a temporary location
        fs = FileSystemStorage()
        image_path = fs.save(filename, uploaded_image)

        # Open the image using PIL
        with fs.open(image_path) as image_file:
            image = Image.open(image_file)

            # Perform OCR to extract text from the image
            extracted_text = pytesseract.image_to_string(image)

        # Delete the temporary original image file
        fs.delete(image_path)

        # Return JSON response with the extracted text
        return JsonResponse({
            'extracted_text': extracted_text,
        })

    return render(request, 'textExtractor.html')

def pdfTextExtractor(request):
    if request.method == 'POST' and request.FILES['pdf']:
        # Get the uploaded PDF file from the request
        uploaded_pdf = request.FILES['pdf']

        # Get the filename and encode it correctly
        filename = urllib.parse.quote(uploaded_pdf.name)

        # Save the PDF to a temporary location
        fs = FileSystemStorage()
        pdf_path = fs.save(filename, uploaded_pdf)

        # Open the PDF file and read its contents
        with fs.open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize a variable to store the extracted text
            extracted_text = ""

            # Loop through all the pages of the PDF and extract text
            for page in pdf_reader.pages:
                extracted_text += page.extract_text()

        # Delete the temporary original PDF file
        fs.delete(pdf_path)

        # Return JSON response with the extracted text
        return JsonResponse({
            'extracted_text': extracted_text,
        })

    return render(request, 'pdfTextExtractor.html')
