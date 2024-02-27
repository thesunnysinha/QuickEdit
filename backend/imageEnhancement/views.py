from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageFilter, ImageEnhance
import io
import urllib.parse
from django.shortcuts import render

def enhance_image(image):
    # Apply GaussianBlur to smoothen the image
    smoothed_image = image.filter(ImageFilter.GaussianBlur(radius=2))

    # Apply unsharp mask to enhance edges and details
    enhanced_image = smoothed_image.filter(ImageFilter.UnsharpMask(radius=2, percent=150))

    # Convert the image to RGB mode (remove alpha channel if present)
    if enhanced_image.mode == 'RGBA':
        enhanced_image = enhanced_image.convert('RGB')

    # Apply additional enhancement (brightness and contrast)
    enhanced_image = ImageEnhance.Brightness(enhanced_image).enhance(1.2)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(1.2)

    return enhanced_image

def imageEnhancement(request):
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

            # Apply enhancements to the image
            enhanced_image = enhance_image(image)

            # Save the enhanced image with a new filename
            enhanced_filename = f"enhanced_{filename}"
            enhanced_io = io.BytesIO()
            enhanced_image.save(enhanced_io, format='JPEG')
            enhanced_image_path = fs.save(enhanced_filename, enhanced_io)

        # Generate URLs for the original and enhanced images
        original_image_url = fs.url(image_path)
        enhanced_image_url = fs.url(enhanced_image_path)

        # Delete the temporary original image file
        # fs.delete(image_path)

        # Return JSON response with the URLs of the original and enhanced images
        return JsonResponse({
            'original_image': original_image_url,
            'enhanced_image': enhanced_image_url,
        })

    return render(request, 'imageEnhancement.html')
