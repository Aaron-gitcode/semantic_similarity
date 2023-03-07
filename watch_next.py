# Function that compares current movie description with descriptions of other movies and informs user of the most similar movie in collection.
# Use spaCy package and its language model 'en_core_web_md to find compare and find most similar movie description
def watch_next(current_movie_descript):

    import spacy

    nlp = spacy.load("en_core_web_md")

    compare_movie = nlp(current_movie_descript)

    movie_descript = {} # Initialise dictionary to store movie title as key and the movie description as value
    with open("movies.txt", "r") as movies_file:
        for line in movies_file:
            movie = line.split(" ")
            title = movie[0:2]
            del movie[0:2]
            temp_descript = " ".join(movie)
            descript = temp_descript.strip(":\n")
            movie_descript[" ".join(title)] = descript

    recommended_movie = ("", 0.0)  # Initialise tuple to store the movie title with the greatest similarity index
    for k, v in movie_descript.items():
        similarity = nlp(v).similarity(compare_movie)
        if similarity > recommended_movie[1]:  
            recommended_movie = (k, similarity)

    print(f"\nIf you liked Planet Hulk, you might also like {recommended_movie[0]}")

current_movie_descript = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
watch_next(current_movie_descript)
