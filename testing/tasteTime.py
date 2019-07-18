userName = input("What is your name?")
userTaste = input("What is your favorite genre of music?")
goodMusic = ["jazz", "rock", "hip-hop", "hiphop", "hip hop"]


def goodTaste(name, favorite):
    if int(goodMusic.index((favorite.lower())) >= 0):
        return "You have good taste " + userName + "!"
    else:
        return "There is better music out there " + userName + "!"
print(goodTaste(userName, userTaste))