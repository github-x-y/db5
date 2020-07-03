import re
class countpatt:
    def __init__(self,fname):
        self.fname=fname
    def count(self,what):
        R_D = {}
        patt = re.compile(what)
        with open(self.fname) as f1:
            for line in f1:
                m = patt.search(line)
                if m:
                    key = m.group()
                    R_D[key]=R_D.get(key,0) +1
        return R_D
if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE|Chrome'
    a1 = countpatt(fname)
    a1 = a1.count(ip)
    a2 = countpatt(fname)
    a2 = a2.count(br)
    a1 = list(a1.items())
    a2 = list(a2.items())
    a1.sort(key=lambda seq:seq[-1],reverse=True)
    a2.sort(key=lambda seq:seq[-1],reverse=True)
    for i in a1:
        print('%s %s次' % i)
    for i in a2:
        print('%s %s次' % i)
