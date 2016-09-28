import webbrowser


class Movie():
    """
    The Movie class is used to store your favorite movies.
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
    	"""
        The initializer of Movie class
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    	"""
        Play the movie trailer in your browser
        """
        webbrowser.open(self.trailer_youtube_url)
