
class Word:
    def __init__(self, w, fileName):
        self.word = w
        self.appearances = 0
        self.listOfFiles = [fileName] #file.name
            
        
    def searchFiles(self, file):
            
        if file.filename not in self.listOfFiles:
            self.listOfFiles.append(file.filename)
            self.appearances +=1
        else:
            print('FILE EXIST') 