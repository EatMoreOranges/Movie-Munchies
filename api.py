import requests
# from requests.exceptions import HTTPError
from dotenv import load_dotenv
load_dotenv()
import os 

class MovieApi:

    def __init__(self,movie_id=None):
        self.movie_id = movie_id

    def get_top_rated_movies(self,page=1):
        url = 'https://api.themoviedb.org/3/movie/top_rated?api_key='+ os.environ.get('MOVIE_API_KEY') + '&page=' + page
        response = requests.get(url)
        return response

    def get_movie_images(self, movie_id):
        url = 'https://api.themoviedb.org/3/movie/'+ movie_id +'/images?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response
    
    def get_popular_movies(self):
        url = 'https://api.themoviedb.org/3/movie/popular?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response
    
    def get_movie_genre_list(self):
        url = 'https://api.themoviedb.org/3/genre/movie/list?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response
    
    def get_movie_recommendations(self, movie_id):
        url = 'https://api.themoviedb.org/3/movie/'+ movie_id +'/recommendations?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response

    def get_movie_translations(self,movie_id):
        url = 'https://api.themoviedb.org/3/movie/'+ movie_id +'/translations?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response
    
    def get_upcoming_movies(self):
        url = 'https://api.themoviedb.org/3/movie/upcoming?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response
    
    def get_movies_out_now(self):
        url = 'https://api.themoviedb.org/3/movie/now_playing?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response
    
    def discover_other_movies(self,lang='en-US', region='', with_genres='?,?', without_genres='?,?'):
        url = 'https://api.themoviedb.org/3/movie/now_playing?api_key='+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response 
    def get_languages(self):
        url = 'https://api.themoviedb.org/3/movie/configuration/languages'+ os.environ.get('MOVIE_API_KEY')
        response = requests.get(url)
        return response


# def main():
#     movie_session = MovieApi()
#     genre_list = movie_session.get_movie_genre_list()
#     out_movies = movie_session.get_movies_out_now()
#     # print(out_movies.json())


# if __name__ == "__main__":
#     main()