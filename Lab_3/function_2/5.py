from movies_data import movies

def average_imdb_by_category(category):
    filtered_movies = [movie for movie in movies if movie["category"].lower() == category.lower()]
    
    if not filtered_movies:
        return f"No movies found in category '{category}'"
    
    total_score = sum(movie["imdb"] for movie in filtered_movies)
    return total_score / len(filtered_movies)

if __name__ == "__main__":
    category_name = input("Enter a movie category: ")
    print(f"Average IMDB score for '{category_name}' movies: {average_imdb_by_category(category_name)}")
