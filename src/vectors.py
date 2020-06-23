"""Module contains functions for solving vector problems. E.g. vector_angles(X, Y) and vector_lengths(a)."""

__author__ = "M.Ylösmäki"

import numpy as np
from math import pi

def vector_angles(X, Y):
    """Calculates vector angles as degrees. Arrays X and Y are same shape (n,m),
    a row in the array corresponds to a vector. Returns an array (n) of angles."""
    dot_prod = np.sum(X*Y, axis=1)
    magn_x = np.sqrt(np.sum(X**2, axis=1))
    magn_y = np.sqrt(np.sum(Y**2, axis=1))
    cos_a = dot_prod / (magn_x * magn_y)
    rad = np.arccos(np.clip(cos_a, -1, 1))
    return rad*180/pi

def vector_lengths(a):
    """Calculates vector lengths (Eucledian norm) as vectors as rows in (n,m) array"""
    tmp = np.sum(a**2, axis=1)
    return np.sqrt(tmp)
	