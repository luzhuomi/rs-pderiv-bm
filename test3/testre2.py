import re2 as re
import sys



def main(size,fname):
    with open(fname, 'r') as f:
        content = f.read()
        print(re.search(r"^(a?){1000,1000}(a){1000,1000}$", content.strip('\r\n')))





if len(sys.argv) < 2:
    print("usage: re2.py filename")
else:
    main(sys.argv[1])