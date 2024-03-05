import sample
import keyBertExtraction as kb
import pickle


fileUpload = "myproject/final_prop_pkg_ahsan__20150430.pdf"

keywords_dict = {}
file_dict = {}


key_list = kb.keywordExtraction(fileUpload)

for word in key_list:
    
    if word not in keywords_dict:   
        newKey = sample.Keyword(word, fileUpload)
        keywords_dict[word] = newKey
    else: 
        keywords_dict[word].searchFiles('Test')
               #keywords[word].appearances += 1
               #keywords[word].listOfFiles.append(proposal)
        
    
print("HERE")
print(keywords_dict.keys())



        
file = sample.File('Test', "hello", key_list)
file_dict[file.filename] = file

print("FILES")
print(file_dict.keys())


savedKeywords = open('Keywords_Dictionary', 'wb')
pickle.dump(keywords_dict, savedKeywords)

savedFiles = open('Files_Dictionary', 'wb')
pickle.dump(file_dict, savedFiles)




