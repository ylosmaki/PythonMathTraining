"Module contains functions hypotheneuse(a,b) and area(a,b) for calculating hypotheneuse and area of a right-angled triangle"

__author__ = "M.Ylösmäki"

import math

def triangle_hypothenuse(a, b):
    "returns the length of the hypothenuse when given the lengths of two other sides (a and b) of a right-angled triangle"
    c = math.sqrt(a**2 + b**2)
    return c

def triangle_area(a, b):
    "returns the area of the right-angled triangle, when two sides (a and b), perpendicular to each other, are given as parameters"
    #or something
    c = (a * b) / 2
    return c
	