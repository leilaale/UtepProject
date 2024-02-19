from PyPDF2 import PdfReader
from pymongo import MongoClient
import os
from urllib.parse import quote_plus

client = MongoClient('mongodb+srv://angel:angel123@cluster0.hi3uuvt.mongodb.net/?retryWrites=true&w=majority')
db = client['proposal_db']
collection = db['proposal_collection']

with open('static/files/example.pdf', 'rb') as file:
    pdf_data = file.read()

inserted_id = collection.insert_one({'pdf': pdf_data}).inserted_id
print(f"PDF uploaded to MongoDB with ID: {inserted_id}")

reader = PdfReader("static/files/example.pdf")
page = reader.pages[2]
print(page.extract_text())