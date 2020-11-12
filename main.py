# account
data = """
foo 123
foo 444
bar  90
zot 100
bar 666
""".split("\n")

def read(data):
    rr = list()
    for r in data:
        if not r.strip():
            continue
        k, v = r.split()
        v = int(v)
        rr.append((k,v))
    return rr 

rr = read(data)

def single_tot(rr, key):
    t = 0
    for k, v in rr:
        if k == key:
            t += v
    return t

tot_foo = single_tot(rr, "foo")

def totals(rr):
    kk = set() 
    tt = list()
    for k, v in rr:
        kk.add(k)
    for k in kk:
        t = single_tot(rr, k)
        tt.append((k, t))
    return tt

tt = totals(rr)

def output(tt):
    f = "Key %s -> Tot: %d"
    for k,v in tt:
        s = f % (k, v)  
        print(s)

output(tt)











