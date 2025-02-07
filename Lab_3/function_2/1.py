from movies_data import movies

def is_highly_rated(movie):
    """Returns True if the movie's IMDB rating is above 5.5"""
    return movie["imdb"] > 5.5

def find_movie(movie_name):
    """Searches for a movie by name in the movies list"""
    for movie in movies:
        if movie["name"].lower() == movie_name.lower():
            return movie
    return None

def check_movie():
    """Gets user input and checks if the movie has an IMDB score above 5.5"""
    movie_name = input("Enter the movie name: ").strip()
    movie = find_movie(movie_name)

    if movie:
        if is_highly_rated(movie):
            print(f"{movie_name} has an IMDB score above 5.5")
        else:
            print(f"{movie_name} has an IMDB score below 5.5")
    else:
        print("Movie not found in the database.")

if __name__ == "__main__":
    check_movie()
