#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:01:28 2021

@author: kantnerj
"""


import gensim; 
from gensim.models  import KeyedVectors; 
location = "GoogleNews-vectors-negative300.bin"
wv = KeyedVectors.load_word2vec_format(location, binary=True, limit=1000000) ;
wv.save_word2vec_format('vectors.csv')
