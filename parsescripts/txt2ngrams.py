import sys
import re
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

def txt2ngrams(fname):
# opens txt file of name fname and extracts ngrams
# returns tuple (1grams, 2grams)

    f = open(fname,'r')

    text = f.read()
    text = text.replace('-\n','') #deals speficially with broken words at endlines
    text = re.sub(r'[,*.;\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n-]', ' ', text)

    token = nltk.word_tokenize(text)
    bigrams = ngrams(token,2)
    trigrams = ngrams(token,3)

    count1 = Counter(token)
    count2 = Counter(bigrams)
    count3 = Counter(trigrams)

    return (count1,count2,count3)

if __name__ == '__main__':
    print txt2ngrams(sys.argv[1])
