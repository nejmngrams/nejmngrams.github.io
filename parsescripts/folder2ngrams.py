import sys
import os
from txt2ngrams import *
from collections import Counter
import pickle
import logging

# loop through folder, store ngrams in 
count1 = Counter()
count2 = Counter()
count3 = Counter()
logging.basicConfig(filename='folder2ngrams.log', level=logging.INFO)

for fname in os.listdir(sys.argv[1]):
    logging.info(fname)
    (onegrams,bigrams,trigrams) = txt2ngrams(sys.argv[1]+fname)
    count1 += onegrams
    count2 += bigrams
    count3 += trigrams

pickle.dump(count1,open('onegrams.pkl','wb'))
pickle.dump(count2,open('bigrams.pkl','wb'))
pickle.dump(count3,open('trigrams.pkl','wb'))
