import datetime
import re2 as re
import sys



def main(size, fname):
    #  pat = re.compile(r"^(((a)?){1000,1000})((a){1000,1000})$")

    pat = mkpat(size)
    t1 = time_now = datetime.datetime.now()
    with open(fname, 'r') as f:
        content = f.read()
        m = pat.match(content.strip('\r\n'))
        print(m.groups())
    t2 = time_now = datetime.datetime.now()
    print(t2-t1)

def mkpat(size):
    size = int(size)
    pat_str = "^" + ("((a)?)" * size) + ("(a)" * size) + "$"
    pat = re.compile(pat_str)
    return pat



if len(sys.argv) < 3:
    print("usage: re2.py num filename")
else:
    main(sys.argv[1], sys.argv[2])