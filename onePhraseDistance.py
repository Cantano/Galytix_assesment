#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:03:24 2021

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


def L2dist(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)


batch_size = 50

phrases = pd.read_csv("phrases.csv", encoding='latin1')
phrases = phrases.values.tolist()

phrase_vectors = np.load("phrase_vectors.npy")

print("user input")
input_phrase = input()
input_phrase = remove_puntc(input_phrase)

input_phrase = input_phrase.split(" ")

numOfVecs = 0.0
vec = np.zeros((1, 300))

for word in input_phrase:
    if word in words:
        numOfVecs += 1.0
        location = words.index(word)
        vec += vectors[location]

if numOfVecs == 0:
    numOfVecs = 1
normalized_vec = vec / numOfVecs

best_dist = 9999
best_index = -1

for i in range(len(phrase_vectors)):
    dist = L2dist(normalized_vec, phrase_vectors[i])
    if dist < best_dist:
        best_dist = dist
        best_index = i

print("the closest match is:")
print('"', phrases[best_index][0], '"')
print("and the distance is", best_dist)



