from movies_data import movies

def movies_by_category(category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]


if __name__ == "__main__":
    category_input = input("Enter a movie category: ").strip()
    filtered_movies = movies_by_category(category_input)

    if filtered_movies:
        print(f"Movies in the '{category_input}' category:")
        for movie in filtered_movies:
            print(f"- {movie['name']} (IMDB: {movie['imdb']})")
    else:
        print(f"No movies found in the '{category_input}' category.")
