import sys
import os
from txt2ngrams import *
import re
import pandas as pd
from collections import Counter
import logging

def extractFileName(line):
    tokens = line.rstrip().split()
    linkname = tokens[0]
    linkpathsplit = linkname.split('/')
    fname = linkpathsplit[-1]+'_'+tokens[1]+'.txt'
    return fname

def extractYear(fname): #extracts year from filename
    tokens = re.split(r'[_.]',fname)
    return int(tokens[-2])

# loop through file with names, store ngrams in 
count1 = Counter()
count2 = Counter()
count3 = Counter()
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()

logging.basicConfig(filename='ngrams.log', level=logging.INFO)
f = open(sys.argv[1],'r')
year = 2017

for line in f:
    logging.info(line)
    fname = extractFileName(line)
    yindex = extractYear(fname)
    (onegrams,bigrams,trigrams) = txt2ngrams(fname)
    if yindex==year:
        count1 += onegrams
        count2 += bigrams
        count3 += trigrams
    else:
        df1 = pd.concat([df1,pd.Series(count1,name=year)],ignore_index=True,axis=1)
        df2 = pd.concat([df2,pd.Series(count2,name=year)],ignore_index=True,axis=1)
        df3 = pd.concat([df3,pd.Series(count3,name=year)],ignore_index=True,axis=1)
        count1 = onegrams
        count2 = bigrams
        count3 = trigrams
        year = yindex

#handle leftover year
df1 = pd.concat([df1,pd.Series(count1,name=year)],ignore_index=True,axis=1)
df2 = pd.concat([df2,pd.Series(count2,name=year)],ignore_index=True,axis=1)
df3 = pd.concat([df3,pd.Series(count3,name=year)],ignore_index=True,axis=1)
df1.fillna(0) # 0 out NaN terms
df2.fillna(0) # 0 out NaN terms
df3.fillna(0) # 0 out NaN terms

df1.to_pickle('onegrams.pkl')
df2.to_pickle('bigrams.pkl')
df3.to_pickle('trigrams.pkl')
