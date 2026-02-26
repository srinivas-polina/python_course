#creating a movie schedle, where we will create a dictinary of the current movie showtimes and then ask the user if they want to look a certain showtime.

current_movies = {}

current_movies["The Grinch"] = "11:00 PM"
current_movies["Rudolph"] = "2:00 PM"
current_movies["Frosty the Snowman"] = "3:00 PM"
current_movies["Christmas Vaction"] = "5:00 PM"

print("We are showing the following movies today:")
for key in current_movies:
    print(key)

movie = input("Which movie showtime do you want to look up? \n")
showtime = current_movies.get(movie)

if movie in current_movies:
    print("The show time of", movie, "is", showtime)
else:
    print("Sorry, we dont have that movie today")