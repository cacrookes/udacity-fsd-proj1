import json
import urllib2
import config

# API Key to use the TMDB API. API is used to grab movie information
#TMDB_API_KEY = "334c17cc23f7a85354e73197ffa16617"

class Movie():
    """ Movie defines the attributes of a movie such as title, poster image,
        link to a trailer, as well as other interesting data
    """
    def __init__(self, movie_id, trailer_youtube):
        # consume movie info from themoviedb.org
        response = urllib2.urlopen('https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+config.TMDB_API_KEY+'&append_to_response=credits')
        movie_data = json.load(response)

        # parse the data we want and assign them to the object
        self.title = movie_data['title']
        self.poster_image_url = 'https://image.tmdb.org/t/p/w185/' + movie_data['poster_path']
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_data['release_date']
        self.runtime = movie_data['runtime'] # returns runtime in minutes

        # construct cast list
        self.cast_list = []
        for cast_member in movie_data['credits']['cast']:
            # encode to ascii and ignore errors. Unicode names with accents causes errors when formatting for html
            self.cast_list.append([cast_member['name'].encode('ascii', 'ignore'), cast_member['character'].encode('ascii', 'ignore')])
