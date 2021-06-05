# readme 
## author: Jakub Kantner

## steps:

### Calculations
0) put all python files in one folder together with the initial files:
- "GoogleNews-vectors-negative300.bin"
- "phrases.csv"
1) run `bash runAll.sh` to run all files that
- unbin the vectors
- calculate distanceMatrix for the phrases in phrases.csv (i,j-th element of the matrix is the distance between i-th and j-th 
phrase in the file). This matrix is also stored in "distanceMatrixOfPhrases.npy" file
- ask user for a phrase -> then calculate its closes match from phrases and its distance and display them in command line 

### App
I did not have enough time to implement the OOP approach so if you want to calculate another user input just run 
`python onePhraseDistance.py` -> it will just do the par when it asks for the phrase and calculates best match and distance

##Alternatively
you can run the functions separately as stated in the following steps 
0) put all python files in one folder together with the initial files:
- "GoogleNews-vectors-negative300.bin"
- "phrases.csv"
1) run unbinvector.py  to obtain "vectors.csv"
2) run embedding.py to created "vectors.npy" file with the feature vectors and "words.txt" with list of the words 
3) run phraseDistances.py to obtain distanceMatrix for all the phrases in the selected batch_size (currently set to the size of the phrase file). The distanceMatrix i, j-th element contains distance between the i-th and j-th phrase in the batch. The matrix is also saved to file "distanceMetrixOfPhrases.npy"
4) run onePhraseDistance to obtain closes match for the selected phrase. User is asked for the phrase in the command line and then the closest phrase is shown with the distance

