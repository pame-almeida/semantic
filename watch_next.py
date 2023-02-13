import spacy  

nlp = spacy.load('en_core_web_md') 


def movies(movie_description):
    
    #Open text file with movie descriptions
    with open ("movies.txt") as f:
        data=f.readlines()

    #Compare the similarities between the description provided and those in the text
    for token in movie_description:
        coef={}
        token = nlp(token)
        for token_ in data:
            token_ = nlp(token_)
            coef[token_]= token.similarity(token_)

    coef=sorted(coef.items(), key=lambda item:item[1])
    most_similar=list(coef[-1])
    
    print(f"Based on the movie description provided, with a similarity of {round(most_similar[1]*100)}% we recommend:\n{most_similar[0]}")
            

movie_description=["Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."]

movies(movie_description)


