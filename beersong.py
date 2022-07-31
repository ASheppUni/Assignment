def song_detail():
    print("-"*25)
    print("-"*5,"Beers Song","-"*7)
    print("-"*25)


def display_verse(num):
    bottles=100
    for index in range(0,num):
        print(bottles,"bottles of beer on the wall")
        bottles=-1

def play_again():
    user_input=input("Would you like to sing a song[y/n]?")
    while user_input not in ["y","Y","n","N"]:
        print("incorrect input")
        user_input=input("Would you like to sing a song[y/n]?")
        return user_input

def start_the_song():
    while play_again() in ["y","Y"]:
        count_verse=input=("How many verses do you want to sing?")

    while not (count_verse.isdigit()):
        count_verse=input=("How many verses do you want to sing?")
    while int(count_verse) not in range (1,101):
        count_verse = int(count_verse)
        display_verse(count_verse)

if __name__ == "__main__":
    start_the_song()
