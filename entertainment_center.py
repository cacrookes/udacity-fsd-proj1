import fresh_tomatoes
import media

""" *********************************************** 
     Define movies to be listed on the website 
    *********************************************** 
"""
john_wick = media.Movie("245891", "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
inception = media.Movie("27205", "https://www.youtube.com/watch?v=66TuSJo4dZM")
fight_club = media.Movie("550", "https://www.youtube.com/watch?v=SUXWAEX2jlg")
kill_bill = media.Movie("24", "https://www.youtube.com/watch?v=7kSuas6mRpk")
inglorious_bastards = media.Movie("16869", "https://www.youtube.com/watch?v=6AtLlVNsuAc")
batman_begins = media.Movie("272", "https://www.youtube.com/watch?v=dYYRjVof6TU")
dark_knight = media.Movie("155", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
terminator_2 = media.Movie("280", "https://www.youtube.com/watch?v=eajuMYNYtuY")
guardians_galaxy = media.Movie("118340", "https://www.youtube.com/watch?v=d96cjJhvlMA")
captain_america_2 = media.Movie("100402", "https://www.youtube.com/watch?v=7SlILk2WMTI")

# assign the movies to list in order to pass to fresh_tomatoes
movie_list = [john_wick, inception, fight_club, kill_bill, inglorious_bastards, batman_begins,
              dark_knight, terminator_2, guardians_galaxy, captain_america_2]

# Creates a html file to display our movie list in a browser, and launches page in a browser
fresh_tomatoes.open_movies_page(movie_list)
