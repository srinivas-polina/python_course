# in python there are six types of comparators
# <, >, <=, >=, ==, !=

#temp = 95 # this is a variable that holds the value of 95
#temp == 95 # this is a comparison that checks if temp is equal to 95, it will return true

temperature = 95

if temperature > 80:
    print("It's too hot outside!")
elif temperature < 60:
    print("It's too cold outside!")
else:
    print("It's not too hot outside!")
    print("Enjoy the outdoor weather!")


####### or operator

temperature = 95

if temperature > 80 or temperature < 60:
    print("Stay Inside!")
else:
    print("Enjoy the Outdoors!")

####### and operator

temperature = 75
forecast = "sunny"

if temperature < 80 and forecast != "rainy":
    print("Enjoy the Outdoors!")
else:
    print("Stay Inside")


#### not operator
forecast = "rainy"

if not forecast == "rainy":
    print("Go Outside")
else:
    print("Stay Inside")

###boolean variable
raining = True

if raining:
    print("Stay Inside")
else:
    print("Go Outside")

#####

raining = True

if not raining:
    print("Go Outside")
else:
    print("Stay inside")