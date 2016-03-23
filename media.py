import re               # Imports Regex Library
import urllib2          # URL library for requesting movie API
import json             # Json processing library


class Movie():
    """This class gathers and stores information about a given movie

    Attributes:
    title (str): The title of the movie, should be spelled correctly to work
    trailer_youtube_url (str): Link to the movie trailer
    storyline (str): Quick storyline about movie from OMDB
    poster_image_url (str): Image of movie from OMDB
    genre (str): Genre of movie from OMDB
    year_released (str): Movie Release Year from OMDB
    runtime (str): Movie runtime taken from OBDB
    actors (str): Major actors in movie taken from OMDB

    """

    # Object initializer
    def __init__(self, title, trailer_youtube_url):

        self.title = title
        self.storyline = "none"                 # temporarily set to none
        self.poster_image_url = "none"          # temporarily set to none
        self.trailer_youtube_url = trailer_youtube_url

        self.build_movie_api_url()
        self.get_movie_data()

    # Method sets up API call url to get movie data from OMDB
    def build_movie_api_url(self):
        self.scrubbed_title = self.title.strip()    # Removes whitespace
        self.scrubbed_title = self.title.replace(" ", "+")
        self.api_url = "http://www.omdbapi.com/?t=MOVIETITLE&plot=short&r=json"
        # places the newly formatted movie title in the URL
        self.api_url = self.api_url.replace("MOVIETITLE", self.scrubbed_title)

    # this method actually gets the data from the URL and stores it
    def get_movie_data(self):
        self.response = urllib2.urlopen(self.api_url)  # Gets data from url
        self.htmlstr = self.response.read()  # stores the data in htlpstr
        self.decoded_json = json.loads(self.htmlstr)  # loads data to JSON obj

        # Get the required data and store it in the object for easy access
        self.storyline = self.decoded_json["Plot"]
        self.poster_image_url = self.decoded_json["Poster"]
        self.year_released = self.decoded_json["Year"]
        self.runtime = self.decoded_json["Runtime"]
        self.genre = self.decoded_json["Genre"]
        self.actors = self.decoded_json["Actors"]
