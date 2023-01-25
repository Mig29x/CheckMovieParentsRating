import requests
from bs4 import BeautifulSoup

def get_rt_rating(movie_name):
    url = f'https://www.rottentomatoes.com/m/{movie_name.lower().replace(" ","_")}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rt_rating = soup.find('score-board', {'class': 'scoreboard'})['audiencescore']
    except:
        rt_rating = "No rating available."
    return rt_rating
print(get_rt_rating("Back to the Future"))
