# takes two pdf files with overlapping contents (such as redundant pages) and removes
# lines that appear in the 1st file from the 2nd
# also removes semicolon-separated tagged lines from file

import sys

def cleanFiles(f1, f2, remove_tags, outf):

    #make list of lines from file 1
    with open(f1) as f:
        content1 = f.readlines()

    tags = remove_tags.split(';')

    of = open(outf,'w')

    file2 = open(f2,'r')
    for line in file2:
        if not line in content1 and not any(s in line for s in tags):
            of.write(line)

if __name__ == '__main__':
    cleanFiles(*sys.argv[1:])
