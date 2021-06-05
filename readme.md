# readme 
## author: Jakub Kantner

## steps 
0) put all python files in one folder together with the initial files:
- "GoogleNews-vectors-negative300.bin"
- "phrases.csv"
1) run unbinvector.py  to obtain "vectors.csv"
2) run embedding.py to created "vectors.npy" file with the feature vectors and "words.txt" with list of the words 
3) run phraseDistances.py to obtain distanceMatrix for all the phrases in the selected batch_size (currently set to the size of the phrase file). The distanceMatrix i, j-th element contains distance between the i-th and j-th phrase in the batch. The matrix is also saved to file "distanceMetrixOfPhrases.npy"
4) run onePhraseDistance to obtain closes match for the selected phrase. User is asked for the phrase in the command line and then the closest phrase is shown with the distance
