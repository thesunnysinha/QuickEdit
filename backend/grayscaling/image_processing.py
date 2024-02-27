from PIL import Image

def grayscale(image_path):
    try:
        image = Image.open(image_path)
        grayscale_image = image.convert("L")  # Convert to grayscale
        return grayscale_image
    except Exception as e:
        print("Error:", e)
        return None
