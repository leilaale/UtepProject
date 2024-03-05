import pandas as pd
import keyBertExtraction as kb

def addToDB(file):
    #db._append({'ID' : files_InSystem+1, 'Name': f'{file.filename}', 'File': file, 'Keywords': kb.keywordExtraction(file)})

    data  = {'ID' : files_InSystem+1, 'Name': 'file', 'File': file, 'Keywords': kb.keywordExtraction(file)}
    db = pd.concat([db, pd.DataFrame([data])], ignore_index=True)

    print(db)

    #data = {'ID' : db.proposals.estimated_document_count()+1, 'Name': f'{proposal.filename}', 'File': proposal, 'Keywords': kb.keywordExtraction(proposal)}
        #df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
files_InSystem = 0

#fileSearch = 'myproject/final_prop_pkg_ahsan__20150430.pdf'
#kb.keywordExtraction(fileSearch)


db = pd.DataFrame(columns = ['ID', 'Name', 'File', 'Keywords'])
addToDB("myproject/final_prop_pkg_ahsan__20150430.pdf")




