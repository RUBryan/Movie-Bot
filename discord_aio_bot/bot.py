import requests
import json

class MovieAPI:
    def __init__(self,base_url="https://api.themoviedb.org/3"):
        self.base_url = base_url
        self.api_key = "NONE"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def request_recommedation(self):
        url = f"{self.base_url}/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
        response = requests.get(url, headers=self.headers)

        return response.text

    def send_recommedation():
        try:
            movie = MovieAPI()
            response_text = movie.request_recommedation()
            movie_list =json.loads(response_text)
            image = "https://image.tmdb.org/t/p/w500"+ movie_list["results"][0]["poster_path"]
            name = movie_list["results"][0]["original_title"]
            overview = movie_list["results"][0]["overview"]
            release = movie_list["results"][0]["release_date"]
            popularity = movie_list["results"][0]["popularity"]
            my_information = {'name': name, 'overview': overview, 'release date': release,'rating': popularity, 'image': image} 
            return my_information
        except Exception as e:
            # Handle exceptions if any
            print(f"Error in send_message: {e}")



