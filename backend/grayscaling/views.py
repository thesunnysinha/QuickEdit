from django.shortcuts import render
import os
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from PIL import Image
import io

def grayscale_conversion(request):
    if request.method == 'POST' and request.FILES['image']:
        # Get the uploaded image from the request
        uploaded_image = request.FILES['image']

        # Save the image to a temporary location
        fs = FileSystemStorage()
        image_path = fs.save(uploaded_image.name, uploaded_image)

        # Open the image using PIL
        image = Image.open(fs.open(image_path))

        # Convert the image to grayscale
        grayscale_image = image.convert('L')

        # Save the grayscale image with a new filename
        grayscale_filename = f"grayscale_{uploaded_image.name}"
        grayscale_io = io.BytesIO()
        grayscale_image.save(grayscale_io, format='JPEG')
        grayscale_image_path = fs.save(grayscale_filename, grayscale_io)

        # Delete the temporary original image file
        # fs.delete(image_path)

        # Return JSON response with the URLs of the original and grayscale images
        return JsonResponse({
            'original_image': fs.url(image_path),
            'grayscale_image': fs.url(grayscale_image_path),
        })

    return render(request, 'grayscaling.html')


