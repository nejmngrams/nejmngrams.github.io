import requests
import sys
sys.path.append('/mnt/brick1/justin/nejm/pdfminer-20140328/tools')
import pdf2txt
import logging

# downloads pdfs into temp.pdf, then converts temp.pdf to a text file
logging.basicConfig(filename='save_pdfs.log', level=logging.INFO)
base = 'http://www.nejm.org'

flinks = open(sys.argv[1],'r') #opens file with list of links as first column

for line in flinks:
    logging.info(line)
    tokens = line.rstrip().split()
    linkname = tokens[0]

    response = requests.get(base+linkname)

    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    linkpathsplit = linkname.split('/')
    fname = linkpathsplit[-1]+'_'+tokens[1]+'.txt'
    pdf2txt.main(['wer','-o',fname,'temp.pdf'])
