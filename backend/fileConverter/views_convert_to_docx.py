def pdf_to_docx(pdf_path):
    docx_path = pdf_path.replace('.pdf', '.docx')
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    doc = Document()
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extract_text()
        doc.add_paragraph(text)
    doc.save(docx_path)
    return docx_path
