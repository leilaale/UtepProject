from PyPDF2 import PdfReader
import pandas as pd 
import numpy as np
import textract
import re
#reader = PdfReader("static/files/example.pdf")
# page = reader.pages[2]
# print(page.extract_text())

reader = PdfReader("myproject\Resume-Leila-Martinez.pdf")

num_pages = len(reader.pages)


count = 0
text = ""

while count < num_pages:
    pageObj = reader.pages[count]
    count += 1
    text += pageObj.extract_text()
    
    
if text != "":
    text = text
else: 
    text = textract.process('http://bit.ly/epo_keyword_extraction_document', method='tesseract', language='eng')
    
text = text.encode('ascii','ignore').lower()
text = text.decode()
keywords = re.findall(r'[a-zA-Z]\w+',text)

df = pd.DataFrame(list(set(keywords)),columns=['keywords'])

def weightage(word,text,number_of_documents=1):
    word_list = re.findall(word,text)
    number_of_times_word_appeared =len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf 


    
df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])

df = df.sort_values('tf_idf',ascending=True)
df.to_csv('Keywords.csv')

df.head(25)     


# SOURCE: https://towardsdatascience.com/how-to-extract-keywords-from-pdfs-and-arrange-in-order-of-their-weights-using-python-841556083341