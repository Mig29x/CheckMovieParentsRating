#todo conexion con RT
import imdb
import requests
from bs4 import BeautifulSoup

def get_rt_rating(movie_name):
    print("RT Rating of "+movie_name["long imdb title"])
    url = f'https://www.rottentomatoes.com/m/{movie_name["long imdb title"].replace(" ","_")}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        rt_rating = soup.find('score-board', {'class': 'scoreboard'})['audiencescore']
    except:
        rt_rating = "No rating available."
    return rt_rating
ia = imdb.IMDb()

def search_movie(title):
    movies = ia.search_movie(title)
    for i, movie in enumerate(movies):
        print(f"{i+1}. {movie}")
    return movies

def show_parents_guide(movie_id):
    print("guide:")
    movie = ia.get_movie(movie_id)
    parents_guide = movie.get("certificates")
    if parents_guide:
        for value in parents_guide:
            print(value)
    else:
        print("No parents guide available.")

while True:
    title = input("Enter movie title (at least 4 characters): ")
    if len(title) < 4:
        print("Title must be at least 4 characters.")
        continue
    movies = search_movie(title)
    if not movies:
        print("No movies found.")
        continue
    choice = input("Select a movie by number: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(movies):
            movie_id = movies[choice-1].movieID
            selected_movie = movies[choice-1]
            show_parents_guide(movie_id)
            print(get_rt_rating(selected_movie)) 
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

