import sys
import os
from txt2ngrams import *
from collections import Counter
import pickle
import logging

def uniform(c):
# takes in a counter c and sets all keys to value 1
    for k in c:
        c[k]=1

# loop through folder, store ngrams in 
count1 = Counter()
count2 = Counter()
count3 = Counter()
logging.basicConfig(filename='folder2ngrams.log', level=logging.INFO)

for fname in os.listdir(sys.argv[1]):
    logging.info(fname)
    (onegrams,bigrams,trigrams) = txt2ngrams(sys.argv[1]+fname)
    uniform(onegrams)
    uniform(bigrams)
    uniform(trigrams)
    count1 += onegrams
    count2 += bigrams
    count3 += trigrams

pickle.dump(count1,open('onefilegrams.pkl','wb'))
pickle.dump(count2,open('bifilegrams.pkl','wb'))
pickle.dump(count3,open('trifilegrams.pkl','wb'))
