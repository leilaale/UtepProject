from PyPDF2 import PdfReader
import os

'''
TODO: Add description, handle exceptions
'''
def get_pdf_data(pdf):
    if not pdf: return

    with open(pdf, 'rb') as file:
        pdf_data = file.read()

    return pdf_data
    

# reader = PdfReader("static/files/example.pdf")
# page = reader.pages[2]
# print(page.extract_text())