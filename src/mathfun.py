""" interface for solving math problems. Commandline interface. EVERYTHING UNDER CONSTRUCTION."""

__author__ = "M.Ylösmäki"

import numpy as np
import vectors as vec
import geometry as ge
import json

from difflib import get_close_matches
#practicing .json data
# efficiency of loading the whole thing here or when needed, usage?
try:
    book = json.load(open("webster.json"))
except FileNotFoundError:
    print("Whoops, the dictionary is lost.")

# ask user data
# read from / write to a file ?
# learn to use database with Python (postgreSQL?)
# graphics and plotting

def help():
    print("""Hey there! Usable commands are:
    'v' = some numbers of vectors
    'g' = meaningless geometry
    'h' = list of commands
    'dict' = dictionary of something
    'q' = quit \n""")
    

def main():
    help()

    # Very much under construction....
    while True:
        what = input("What is your purpose here? ")
        print()
        if what == 'q':
            print("Now run away or I shall taunt you.")
            print()
            break

        elif what == 'v':
            # vector lengths calculated e.g.:
            x = np.array([[3,4,0],[1,4,2]])
            y = np.array([[4,4,2],[0,-3,-1]])
            print("vector angles:", vec.vector_angles(x, y))

            # vector angles calculated e.g.:
            np.random.seed(0)
            b = np.random.randint(0, 10, (3,4))
            print("vector lengths:", vec.vector_lengths(b))
            print()

        elif what == 'g':
            # triangle calculation e.g.: 
            print("hypothenuse:", ge.triangle_hypothenuse(1, 2))
            print("area:", ge.triangle_area(1, 2))
            print()

#### dictionary (or some json training maybe as in its own class in the future, at least own function)
        elif what == 'dict':
            #dictionary of something, 'ni' prints the valid keys, hits prints the meaning
            #if not a hit, throws you out of dictionary
            # maybe load the json here, maybe dictionary or something simular as own class?
            print("<book> Welcome to THE dictionary!")
            print("<book> 'ni' prints every key if needed and with linebreak you can get out")
            word = input("<book> Meaning of: ")

            while word != '':
                word = word.lower()
                if word == 'ni':
                    for x in book.keys():
                        print(x)
                elif word in book:
                    for ind, x in enumerate(book[word]):
                        print(f"{ind+1}. {x}")
                elif word.title() in book:  # in case data contains "Data"
                    for ind, x in enumerate(book[word.title()]):
                        print(f"{ind+1}. {x}")                    
                elif word.upper() in book: # in case data contains "DATA"
                    for ind, x in enumerate(book[word.upper()]):
                        print(f"{ind+1}. {x}")                    
                else:
                    # find the closest matches for word
                    almost = get_close_matches(word, book.keys())
                    if len(almost) > 0:
                        print("<book> The closest match is:", almost[0]) # inform user this wasn't 100% match
                        for i, y in enumerate(book[almost[0]]):
                            print(f"{i+1}. {y}")
                    else:
                        print("<book> Didn't find anything interesting.")
                word = input("<book> Meaning of: ")

            print("<book> Bye.\n")  ################## here ends dictionary

        elif what == 'h':
            help()
        
        else:
            print("That is not right, try again.")
            help()

if __name__ == "__main__":
    main()
	