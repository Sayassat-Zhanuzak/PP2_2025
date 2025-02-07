from movies_data import movies

def high_rated_movies():
    return [movie for movie in movies if movie["imdb"] > 5.5]

if __name__ == "__main__":
    print("Movies with IMDB score above 5.5:")
    for movie in high_rated_movies():
        print(f"- {movie['name']} (IMDB: {movie['imdb']})")
