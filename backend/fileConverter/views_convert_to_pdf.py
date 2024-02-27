def docx_to_pdf(docx_path):
    pdf_path = docx_path.replace('.docx', '.pdf')
    doc = Document(docx_path)
    doc.save(pdf_path)
    return pdf_path

def text_to_pdf(text_path):
    pdf_path = text_path.replace('.txt', '.pdf')
    with open(text_path, 'r', encoding='utf-8') as txt_file:
        text = txt_file.read()
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(PyPDF2.PageObject.createTextPage(text))
    with open(pdf_path, 'wb') as pdf_file:
        pdf_writer.write(pdf_file)
    return pdf_path

def image_to_pdf(image_path):
    pdf_path = image_path.replace('.jpg', '.pdf').replace('.png', '.pdf')
    image = Image.open(image_path)
    pdf_path = image_path.replace('.jpg', '.pdf').replace('.png', '.pdf')
    image.save(pdf_path, "PDF", resolution=100.0, save_all=True)
    return pdf_path
