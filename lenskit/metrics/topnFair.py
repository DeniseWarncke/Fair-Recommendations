"""
Fair Top-N evaluation metrics.


Lav measures ud fra : item, score, user, rank, algorithm, protected

"""



from __future__ import division
import numpy as np
import math
from scipy.stats import spearmanr
from scipy.stats import pearsonr


ND_DIFFERENCE="rND" #represent normalized difference group fairness measure
KL_DIVERGENCE="rKL" #represent kl-divergence group fairness measure
RD_DIFFERENCE="rRD" #represent ratio difference group fairness measure
LOG_BASE=2 #log base used in logorithm function

NORM_CUTPOINT=10 # cut-off point used in normalizer computation
NORM_ITERATION=10 # max iterations used in normalizer computation
#NORM_FILE="normalizer.txt" # externally text file for normalizers



def 


def calculateNDFairnes(recs, truth):

_ranking """A permutation of N numbers (0..N-1) that represents a ranking of N individuals, 
                                e.g., [0, 3, 5, 2, 1, 4].  Each number is an identifier of an individual.
                                Stored as a python array."""

_protected_group """A set of identifiers from _ranking that represent members of the protected group
                                e.g., [0, 2, 3].  Stored as a python array for convenience, order does not matter."""

_cut_point """Cut range for the calculation of group fairness, e.g., 10, 20, 30,..."""

_gf_measure """Group fairness measure to be used in the calculation, 
                            one of 'rKL', 'rND', 'rRD'."""

_normalizer """The normalizer of the input _gf_measure that is computed externally for efficiency."""

    # error handling for input type
    if not isinstance( _cut_point, ( int, long ) ):
        raise TypeError("Input batch size must be an integer larger than 0")
    if not isinstance( _normalizer, (int, long, float, complex) ):
        raise TypeError("Input normalizer must be a number larger than 0")
    if not isinstance( _gf_measure, str ):
        raise TypeError("Input group fairness measure must be a string that choose from ['rKL', 'rND', 'rRD']")

    















