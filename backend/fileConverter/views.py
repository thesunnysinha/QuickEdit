import urllib.parse
import io
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import os
import PyPDF2
from docx import Document
import docx2txt
import textract
from PIL import Image
from pdf2image import convert_from_path
from fileConverter.views_convert_to_docx import *
from fileConverter.views_convert_to_jpeg import *
from fileConverter.views_convert_to_jpg import *
from fileConverter.views_convert_to_pdf import *
from fileConverter.views_convert_to_text import *

def fileConverter(request):
    if request.method == 'POST' and request.FILES['file']:
        # Get the uploaded file from the request
        uploaded_file = request.FILES['file']

        # Get the filename and encode it correctly
        filename = urllib.parse.quote(uploaded_file.name)

        # Save the file to a temporary location
        fs = FileSystemStorage()
        file_path = fs.save(filename, uploaded_file)

        # Get the selected format for conversion
        selected_format = request.POST.get('format')

        # Perform file conversion based on the selected format
        converted_file_path = None
        if selected_format == 'pdf':
            # Perform PDF conversion (e.g., from DOCX to PDF)
            if filename.endswith('.docx'):
                docx_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_path = docx_to_pdf(docx_path)
            elif filename.endswith('.txt'):
                text_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_path = text_to_pdf(text_path)
            elif filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_path = image_to_pdf(image_path)
        elif selected_format == 'docx':
            # Perform DOCX conversion (e.g., from PDF to DOCX)
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_path = pdf_to_docx(pdf_path)
        elif selected_format == 'text':
            # Perform text conversion (e.g., from PDF to text)
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_path = pdf_to_text(pdf_path)
        
        elif selected_format == 'jpg':
            # Perform JPG conversion
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_paths = pdf_to_jpg(pdf_path)
            
            elif filename.endswith('.docx'):
                docx_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_paths = docx_to_jpg(docx_path)

            elif filename.endswith('.txt'):
                txt_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_paths = txt_to_jpg(txt_path)
            elif filename.endswith('.png'):
                png_path = os.path.join(settings.MEDIA_ROOT, file_path)
                converted_file_paths = png_to_jpg(png_path)

        # Delete the temporary original file
        fs.delete(file_path)

        if converted_file_path:
            # Get the filename of the converted file
            converted_filename = os.path.basename(converted_file_path)

            # Create the download link for the converted file
            download_link = fs.url(converted_filename)

            # Return JSON response with the download link
            return JsonResponse({
                'download_link': download_link,
            })

    return render(request, 'fileConverter.html')



