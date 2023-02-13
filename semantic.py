import spacy

nlp=spacy.load('en_core_web_md')


# #SIMILARITY

# word1 = nlp("cat")
# word2 = nlp("monkey")
# word3 = nlp("banana")

# print(word1.similarity(word2))
# print(word3.similarity(word2))
# print(word3.similarity(word1))


#WORKING WITH VECTORS

# tokens = nlp ('cat apple monkey banana')
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))

#The lowest correlations are those with cat (~0.20), except for the comparison between cat and monkey. 
#The highest correlation is that for the two fruits (0.66), followed by the two animals (0.59), and the association between monkey and banana (0.40)

tokens_own = nlp ('tea coffee book mug')
for token1 in tokens_own:
    for token2 in tokens_own:
        print(token1.text, token2.text, token1.similarity(token2))

#The lowest correlations are between tea and book (0.10), followed by mug and book (0.12) or book and coffee (0.13)
#The highest correlations are between tea and coffee (0.80) since they are both hot drinks, this is followed by the association between mug and coffe or tea (~0.46).

# #WORKING WITH SENTENCES 

# sentence_to_compare = "Why is my cat on the car"
# sentences = ["where did my dog go",
# "Hello, there is my car",
# "I\'ve lost my car in my car",
# "I\'d like my boat back",
# "I will name my dog Diana"]
# model_sentence = nlp(sentence_to_compare)
# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", similarity)

