import transformers
import strengthWords

# Load the BERT model
model = transformers.BertModel.from_pretrained('bert-base-uncased')


# Tokenize and encode the texts
text1 = "This is the first text."
text2 = "This is the second text."
encoding1 = model.encoder(text1)
encoding2 = model.encoder(text2)


# Calculate the cosine similarity between the embeddings
similarity = numpy.dot(encoding1, encoding2) / (numpy.linalg.norm(encoding1) * numpy.linalg.norm(encoding2))

print(similarity)



# method to run strength words vectors
def wordVector(word):
    wordV = model.encoder(word)
    return wordV
