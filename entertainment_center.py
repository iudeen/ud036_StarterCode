import media
import fresh_tomatoes
#Initializing Objects of class Movie
moana = media.Movie("Moana", "An island girl goes on a voyage to save her island.","https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg", "https://www.youtube.com/watch?v=LKFuXETZUsI" )

spiderman_homecoming = media.Movie("Spiderman Homecoming", "Just another Spiderman Movie", "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg", "https://www.youtube.com/watch?v=U0D3AOldjMU")

school_of_rock = media.Movie("School Of Rock", "Story", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "Story of a Rat", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Some story in Paris", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "Games excite me, but I am hungry", "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [moana, spiderman_homecoming, school_of_rock, ratatouille, midnight_in_paris, hunger_games] #list of Movies
fresh_tomatoes.open_movies_page(movies) #open the HTML page by calling the class
