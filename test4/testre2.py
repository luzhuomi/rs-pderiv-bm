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
        print(m.group(int(size)*2+1))
    t2 = time_now = datetime.datetime.now()
    print(t2-t1)

def mkpat(size):
    size = int(size)
    fst = "(a)?"
    for i in range(size-1):
        fst = "((a)?)" + f"({fst})"
    snd = "(a)"
    for j in range(size-1):
        snd = "(a)" + f"({snd})"
    pat_str = "^" + f"({snd})" + f"({fst})" + "$"
    print(pat_str)
    pat = re.compile(pat_str)
    return pat



if len(sys.argv) < 3:
    print("usage: re2.py num filename")
else:
    main(sys.argv[1], sys.argv[2])