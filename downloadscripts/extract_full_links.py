from bs4 import BeautifulSoup
import sys

def extract_full_links(f, extras = ''):
    soup = BeautifulSoup(f,'html.parser')
    tocContent = soup.find('div',class_='tocContent') #focus on just toc, without most popular etc articles
    for link in tocContent.find_all('a'):
        href = link.get('href')
        if 'full' in href:
            print href + '\t' + extras

if __name__ == '__main__':
    f = open(sys.argv[1])
    fstring = f.read()
    extract_full_links(fstring)
