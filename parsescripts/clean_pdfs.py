import sys
import logging
from pdfClean import *

def extractFileName(line):
    tokens = line.rstrip().split()
    linkname = tokens[0]
    linkpathsplit = linkname.split('/')
    fname = linkpathsplit[-1]+'_'+tokens[1]+'.txt'
    return fname

# downloads pdfs into temp.pdf, then converts temp.pdf to a text file
logging.basicConfig(filename='clean_pdfs.log', level=logging.INFO)

flinks = open(sys.argv[1],'r') #opens file with list of links as first column

cleandir = "clean/" #directory where the cleaned files will live

linkname1 = extractFileName(flinks.readline())
for line in flinks:
    logging.info(line)
    linkname2 = extractFileName(line) 

    cleanFiles(linkname1,linkname2,"Downloaded from nejm.org",cleandir+linkname2)

    linkname1 = linkname2

