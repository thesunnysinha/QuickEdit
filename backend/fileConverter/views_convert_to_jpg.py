def pdf_to_jpg(input_path):
    # Conversion logic for PDF to JPG
    images = convert_from_path(input_path, dpi=300)
    jpg_image_paths = []

    for i, image in enumerate(images):
        jpg_image_path = input_path.replace('.pdf', f'_{i+1}.jpg')
        image.save(jpg_image_path, 'JPEG')
        jpg_image_paths.append(jpg_image_path)

    return jpg_image_paths

def docx_to_jpg(input_path):
    # Conversion logic for DOCX to JPG
    doc = Document(input_path)
    images = []

    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            img_path = doc.part.rels[rel].target_ref
            image = Image.open(img_path)
            images.append(image)

    jpg_image_paths = []
    for i, image in enumerate(images):
        jpg_image_path = input_path.replace('.docx', f'_{i+1}.jpg')
        image = image.convert("RGB")
        image.save(jpg_image_path, "JPEG")
        jpg_image_paths.append(jpg_image_path)

    return jpg_image_paths

def txt_to_jpg(input_path):
    # Conversion logic for TXT to JPG
    with open(input_path, 'r') as txt_file:
        content = txt_file.read()

    # You can customize the image size and font as needed
    image_width, image_height = 800, 600
    font_size = 24

    # Create a white background image
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype('arial.ttf', font_size)

    # Add the text to the image
    draw.text((20, 20), content, fill='black', font=font)

    jpg_image_path = input_path.replace('.txt', '.jpg')
    image.save(jpg_image_path, 'JPEG')

    return jpg_image_path

def png_to_jpg(input_path):
    # Conversion logic for PNG to JPG
    image = Image.open(input_path)

    # Convert the image to RGB mode (remove transparency if present)
    image = image.convert('RGB')

    jpg_image_path = input_path.replace('.png', '.jpg')
    image.save(jpg_image_path, 'JPEG')

    return jpg_image_path
