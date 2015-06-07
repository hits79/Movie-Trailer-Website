# importing webbrowser, so we can open the broswer and show trailers
import webbrowser


class Movie():

    """holds movie title, stroyline, image, and trailer link"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
         
         #movie title
         self.title = movie_title
         #summary of the movie's story
         self.storyline = movie_storyline
         #image url of the movie poster
         self.poster_image_url = poster_image
         #movie trailer on youtube
         self.trailer_youtube_url = trailer_youtube

    # method to show trailers of videos
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
