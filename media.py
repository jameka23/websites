#making the class movie
#associated with the website we're making

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,
                 trailer_youtube):
        #self refers to the movie itself ie ToyStory ...
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        