class Movie():
    """ This class provides  a way to store movie related information

    Atributes:
        title (str) : The name of the Movie.
        storyline (str): All the information about the movie.
        running_time (str): The duration of the movie.
        genre (str): The type of movie.
        poster_image (str): Represent the poster image of the movie.
        trailer_youtube (str): The youtube video of the movie.
        director (str):  The movie was directed by.
        release_date (str): The date of the release. Format (YYYY-MM-dd).
        actors (str): The actor and actreeses of the movie.

    """
    def __init__(self, title, storyline, running_time, genre, poster_image, trailer_youtube, director, release_date, actors):
        self.title = title
        self.storyline = storyline
        self.running_time =  running_time
        self.genre = genre
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.release_date = release_date
        self.actors = actors
        
    