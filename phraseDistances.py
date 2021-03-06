#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:17:36 2021

@author: kantnerj
"""

import numpy as np

import pickle

import pandas as pd

with open("words.txt", "rb") as fp:  # Unpickling
    words = pickle.load(fp)

vectors = np.load("vectors.npy")


def remove_puntc(phrase):
    phrase = phrase.rstrip('"')
    phrase = phrase.lstrip('"')
    phrase = phrase.rstrip("'")
    phrase = phrase.lstrip("'")
    phrase = phrase.rstrip("!")
    phrase = phrase.rstrip("?")

    return phrase


batch_size = 50

phrases = pd.read_csv("phrases.csv", encoding='latin1')
phrases = phrases.values.tolist()

normalized_vectors = np.zeros((batch_size, 300))

for i in range(batch_size):

    phrase = phrases[i][0]
    phrase = remove_puntc(phrase)
    phrase = phrase.split(" ")

    numOfVecs = 0.0
    vec = np.zeros((1, 300))

    for word in phrase:
        if word in words:
            numOfVecs += 1.0
            location = words.index(word)
            vec += vectors[location]

    normalized_vec = vec / numOfVecs
    normalized_vectors[i] = normalized_vec


def L2dist(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)


distanceMatrix = np.zeros((batch_size, batch_size))

for i in range(batch_size):
    for j in range(batch_size):
        distanceMatrix[i][j] = L2dist(normalized_vectors[i], normalized_vectors[j])

np.save("distanceMatrixOfPhrases", distanceMatrix)
np.save("phrase_vectors", normalized_vectors)


