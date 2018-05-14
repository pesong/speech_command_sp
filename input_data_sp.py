"""
wav data clean & prepropress use numpy and librosa
authored by psong@lighten.ai
date: 2018-05-11
"""

import numpy as np

# define constraint
MAX_NUM_WAVS_PER_CLASS = 2**27 - 1  # ~ 134m
SILENCE_LABEL = '_silence_'
SILENCE_INDEX = 0
UNKNOWN_WORD_LABEL = '_unknown_'
UNKNOWN_WORD_INDEX = 1
BACKGROUND_NOISE_DIR_NAME = '_background_noise_'
RANDOM_SEED = 59185


def prepare_words_list(wanted_words):
    """
        Description:
            Prepends common tokens to the custom word list
        Args:
            wanted_words: List of strings containing the custom words.
        Returns:
            List with the standard silence and unknown tokens added.
    """
    return [SILENCE_LABEL, UNKNOWN_WORD_LABEL] + wanted_words



