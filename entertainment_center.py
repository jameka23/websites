import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)


avatar = media.Movie("Avatar", "A marine on an alien planet.",
                     "http://ecx.images-amazon.com/images/I/41kTVLeW1CL.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

black_panther = media.Movie("Black Panther",
                            "The story of T'Challa returing home to be king.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

black_panther.show_trailer()
