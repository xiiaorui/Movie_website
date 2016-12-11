import media
import fresh_tomatoes

toystory = media.Movie("Toy Story", "Toys play like human", "http://vignette4.wikia.nocookie.net/pixar/images/a/af/Toy_Story_Logo.png/revision/latest?cb=20150728184703",
                       "https://www.youtube.com/watch?v=SgoiKLFBA3Q")


spiderman = media.Movie("SpiderMan", "Man--Men--Spiderman", "https://i.ytimg.com/vi/3R2uvJqWeVg/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=xrzXIaTt99U")
"""
print(toystory.storyline)
print(toystory.title)
toystory.show_trailer()
spiderman.show_trailer()
"""

movie = [toystory, spiderman]
fresh_tomatoes.open_movies_page(movie)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__moudle__)
