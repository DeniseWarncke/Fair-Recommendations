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


def calculateNDFairnes(recs, truth):

    """
        Calculate the group fairness value of input ranking.
        Called by function 'calculateNDFairness'.
        :param _ranking: A permutation of N numbers (0..N-1) that represents a ranking of N individuals, 
                                e.g., [0, 3, 5, 2, 1, 4].  Each number is an identifier of an individual.
                                Stored as a python array.
                                Can be a total ranking of input data or a partial ranking of input data.
        :param _protected_group: A set of identifiers from _ranking that represent members of the protected group
                                e.g., [0, 2, 3].  Stored as a python array for convenience, order does not matter.
        :param _user_N: The size of input items 
        :param _pro_N: The size of input protected group
        :param _gf_measure: The group fairness measure to be used in calculation        
        :return: returns the value of selected group fairness measure of this input ranking
    """

    
    # error handling for input type
    if not isinstance( _cut_point, ( int, long ) ):
        raise TypeError("Input batch size must be an integer larger than 0")
    if not isinstance( _normalizer, (int, long, float, complex) ):
        raise TypeError("Input normalizer must be a number larger than 0")
    if not isinstance( _gf_measure, str ):
        raise TypeError("Input group fairness measure must be a string that choose from ['rKL', 'rND', 'rRD']")

"""















