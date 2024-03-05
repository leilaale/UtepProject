import wordSimilarity
import scapy

words = ['cyber', 'aerospace', 'additive manufacturing',
         'cybersecurity', 'environmental Science', 'materials science and engineering',
         'biomedical science', 'transportation', 'hispanic health disparities', 'real estate', 
         'hispanic student success']

strengthWords = {}

def addToStrengthWords():
    
    for w in words:
        wordVec = wordVector(w)
        strengthWords['w'] = wordVec

    print(strengthWords)