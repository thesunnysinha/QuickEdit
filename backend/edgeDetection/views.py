from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageFilter
import io
import urllib.parse

def detect_edges(image):
    # Apply edge detection using Canny method
    edge_image = image.filter(ImageFilter.FIND_EDGES)

    if edge_image.mode == 'RGBA':
        edge_image = edge_image.convert('RGB')

    return edge_image

def edgeDetection(request):
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

            # Apply edge detection to the image
            edge_image = detect_edges(image)

            # Save the edge-detected image with a new filename
            edge_filename = f"edge_detected_{filename}"
            edge_io = io.BytesIO()
            edge_image.save(edge_io, format='JPEG')
            edge_image_path = fs.save(edge_filename, edge_io)

        # Generate URLs for the original and edge-detected images
        original_image_url = fs.url(image_path)
        edge_image_url = fs.url(edge_image_path)

        # Delete the temporary original image file
        # fs.delete(image_path)

        # Return JSON response with the URLs of the original and edge-detected images
        return JsonResponse({
            'original_image': original_image_url,
            'edged_image': edge_image_url,
        })

    return render(request, 'edgeDetection.html')
