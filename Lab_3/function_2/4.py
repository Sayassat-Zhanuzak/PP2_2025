from movies_data import movies

def average_imdb_by_movies(movie_names):
    filtered_movies = [movie for movie in movies if movie["name"].lower() in movie_names]
    
    if not filtered_movies:
        return "None of the entered movies were found."
    
    total_score = sum(movie["imdb"] for movie in filtered_movies)
    return total_score / len(filtered_movies)

if __name__ == "__main__":
    user_input = input("Enter movie names separated by commas: ").strip().split(",")
    movie_names = [name.strip().lower() for name in user_input]
    
    print(f"Average IMDB score: {average_imdb_by_movies(movie_names)}")
