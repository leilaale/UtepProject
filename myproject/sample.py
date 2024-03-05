import keyBertExtraction as kb


class File: 
    
    def __init__(self, fileN, f, kList ):
        self.filename = fileN
        self.file = f
        self.keywordList = kList
    
class Keyword:
            
    def __init__(self, w, file):
        self.word = w
        self.appearances = 0
        self.listOfFiles = [file.name] #file.name
        
    
    def searchFiles(self, File):
        
        if File.name not in self.listOfFiles:
            self.listOfFiles.append(File.name)
            self.appearances +=1
        else:
            print('FILE EXIST') 