from rake_nltk import Rake
from PyPDF2 import PdfReader

#reader = PdfReader("static/files/example.pdf")
# page = reader.pages[2]
# print(page.extract_text())

reader = PdfReader("myproject/final_prop_pkg_ahsan__20150430.pdf")

num_pages = len(reader.pages)


count = 0
text = ""

while count < num_pages:
    pageObj = reader.pages[count]
    count += 1
    text += pageObj.extract_text()
    
    
r = Rake(min_length=2, max_length=3, include_repeated_phrases=False)

r.extract_keywords_from_text(text)

keywords_rake = r.get_ranked_phrases()

print(keywords_rake)