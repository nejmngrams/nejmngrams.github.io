from extract_full_links import *
import requests

base = 'http://www.nejm.org'

f = open('../html/tocs.txt','r')

for line in f:
    tokens = line.rstrip().split()
    link = base + tokens[0]
    r = requests.get(link)
    extract_full_links(r.text,tokens[1])
