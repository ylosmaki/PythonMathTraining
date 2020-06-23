""" interface for solving math problems. Commandline interface. EVERYTHING UNDER CONSTRUCTION."""

__author__ = "M.Ylösmäki"

import numpy as np
import vectors
import triangles
# try:
#     from src import triangles
# except ModuleNotFoundError:
#     import triangles

# ask user data
# read from / write to a file ?
# learn to use database with Python (postgreSQL?)
# graphics and plotting

def help():
    print("""Hey there! Usable commands are:
    'v' = some numbers of vectors
    't' = meaningless triangles
    'h' = list of commands
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
            print("vector angles:", vectors.vector_angles(x, y))

            # vector angles calculated e.g.:
            np.random.seed(0)
            b = np.random.randint(0, 10, (3,4))
            print("vector lengths:", vectors.vector_lengths(b))
            print()

        elif what == 't':
            # triangle calculation e.g.: 
            print("hypothenuse:", triangles.hypothenuse(1, 2))
            print("area:", triangles.area(1, 2))
            print()
        
        elif what == 'h':
            help()
        
        else:
            print("That is not right, try again.")
            help()

if __name__ == "__main__":
    main()
	