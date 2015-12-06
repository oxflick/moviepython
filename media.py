import webbrowser

#Creating a class Movie
class Movie():
    """This class provides a way to store movie related information"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, 
                 trailer_youtube, movie_actors):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = movie_actors

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
