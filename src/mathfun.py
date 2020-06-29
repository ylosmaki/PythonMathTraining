""" interface for solving math problems. Commandline interface. EVERYTHING UNDER CONSTRUCTION."""

__author__ = "M.Ylösmäki"

import numpy as np
import vectors as vec
import geometry as ge
import json

#practicing .json data
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
    while True: # there has to be another way?
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

        elif what == 'dict':
            #dictionary of something, 'ni' prints the valid keys, hits prints the meaning
            #if not a hit, throws you out of dictionary
            print("<book> 'ni' prints every key if needed")
            while True:
                word = input("<book> Meaning of: ")
                if word == 'ni':
                    for x in book.keys():
                        print(x)
                elif word in book.keys():
                    for ind, x in enumerate(book[word]):
                        print(f"{ind+1}. {x}")
                else:
                    print("<book> Not found. Bye.")
                    break
        
        elif what == 'h':
            help()
        
        else:
            print("That is not right, try again.")
            help()

if __name__ == "__main__":
    main()
	