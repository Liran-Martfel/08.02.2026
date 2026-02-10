import random

CAPITAL_CITIES = [
    "TOKYO", "PARIS", "LONDON", "BERLIN", "MADRID",
    "ROME", "VIENNA", "PRAGUE", "WARSAW", "ATHENS",
    "CAIRO", "ANKARA", "BEIJING", "SEOUL", "HANOI",
    "BANGKOK", "CANBERRA", "OTTAWA", "BRASILIA", "BUENOS AIRES"]

city = random.choice(CAPITAL_CITIES)
print(city)
print('_ ' * len(city))
guess: str = input("Please enter your letter guess: ")
guess = guess.upper()
while city is not guess:
    for i in range (len(city)):
        if guess in city:
            city = city.replace ("_ ", guess)

            guess = input("you got the letter right - Please enter your next letter guess: ")
            guess = guess.upper()
        else:
            guess = input("incorrect letter - enter your letter guess: ")
            guess = guess.upper()
            continue
