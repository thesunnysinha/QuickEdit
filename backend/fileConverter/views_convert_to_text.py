def docx_to_text(docx_path):
    return docx2txt.process(docx_path)

def pdf_to_text(pdf_path):
    text = textract.process(pdf_path, method='pdfminer')
    return text.decode()









