import fresh_tomatoes
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

#black_panther.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "A fake substitute at a prep school gets his class to perform rock music",
                             "http://www.impawards.com/2003/posters/school_of_rock.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A story about a mouse that helps a chef make a dish.",
                          "http://www.impawards.com/2007/posters/ratatouille_ver3.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

forrest_gump = media.Movie("Forrest Gump",
                           "Life for a slow-witted man from Greenbow,AL",
                           "http://www.moviepostersusa.com/media/catalog/product/cache/1/image/512x512/9df78eab33525d08d6e5fb8d27136e95/p/2/p286_1.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")

aladdin = media.Movie("Aladdin",
                      "A story of a street boy falling in love with a princess",
                      "http://www.impawards.com/1992/posters/med_aladdin_ver3.jpg",
                      "https://www.youtube.com/watch?v=qUfd5JDkcwE")

movies = [toy_story, avatar, school_of_rock, ratatouille, forrest_gump,
          aladdin]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__) #prints out the documentation 
