import webbrowser
class Movie():
    """ The class Movies has the following attributes
    1. Movie Title
    2. Story Line
    3. Poster Image
    4. YouTube trailer Link """

    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
