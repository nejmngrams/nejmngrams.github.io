from extract_toc_links import *
import requests

base = 'http://www.nejm.org'

f = open('../html/yearlinks.txt','r')

for line in f:
    link = base + line.rstrip()
    r = requests.get(link)

    #get the year to print out as last column
    tokens = link.split('/')

    extract_toc_links(r.text, tokens[-1])
