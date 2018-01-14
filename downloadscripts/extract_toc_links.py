from bs4 import BeautifulSoup
import sys

def extract_toc_links(f,extras = ''):
    soup = BeautifulSoup(f,'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if 'toc' in href and not '/toc/nejm/377' in href and not 'medical-journal' in href and not 'lastweek' in href: #exclude recent issue toc's
            print href + '\t' + extras

if __name__ == '__main__':
    f = open(sys.argv[1])
    fstring = f.read()
    extract_toc_links(fstring)
