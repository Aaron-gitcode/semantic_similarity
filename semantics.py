import spacy

nlp = spacy.load("en_core_web_md")

## Similarity with spaCy
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Working with vectors
tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Interesting how there is a higher similarity between monkey-banana compared to cat-banana and the model has recognised that monkeys are more associated with bananas than cats
more_tokens = nlp("tea coffee china colombia")
for token1 in more_tokens:
    for token2 in more_tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare = "Why is my cat on the car"
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana",
]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# As the 'en_core_web_sm' model has no word vectors loaded, the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements.
# The recognition of the similarity between complaints, recipes and complaint-recipes are all lower and less informative
