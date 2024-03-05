import pandas as pd
from keybert import KeyBERT
from PyPDF2 import PdfReader

# SOURCE: https://stackoverflow.com/questions/74360815/keywords-extracted-from-text-using-keybert-and-lambda-function-appear-to-be-simi

def keywordExtraction(file):
    
    data = {'Text': [extractText(file)]}


    memo_ = pd.DataFrame(data)  # Create dataframe
    kw_model = KeyBERT(model="all-mpnet-base-v2")  # Instantiate KeyBERT model
    n_keywords = 50  # Specify number of keywords to extract
    ngram = 2  # Specify ngram of keywords

    # Apply KeyBERT model extraction function along 'Text' axis of pandas dataframe

    memo_keywords_df = memo_['Text'].apply(lambda x:
                                        kw_model.extract_keywords(x,
                                                                    keyphrase_ngram_range=(1, 1),
                                                                    stop_words='english',
                                                                    highlight=False,
                                                                    top_n=n_keywords))

    memo_keywords_df = memo_keywords_df + memo_['Text'].apply(lambda x:
                                        kw_model.extract_keywords(x,
                                                                    keyphrase_ngram_range=(1, ngram),
                                                                    stop_words='english',
                                                                    highlight=False,
                                                                    top_n=n_keywords))
    # Display results
    keywords = []
    
    for i, memo_keywords in enumerate(memo_keywords_df):
        #print("-"*40 + "\nmemo_ #{}: top {} keywords (ngram range 1-{})".format(i, n_keywords, ngram))
        #print('HERE')
        #print(memo_keywords)
        for keyword in memo_keywords:
            #print(keyword[0])
            if keyword not in keywords:
                keywords.append(keyword[0])

    return keywords



def extractText(file):
    reader = PdfReader(file)
    num_pages = len(reader.pages)

    count = 0
    text = ""

    while count < num_pages:
        pageObj = reader.pages[count]
        count += 1
        text += pageObj.extract_text()
        
    return text

