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

def tot(rr, key):
    t = 0
    for k, v in rr:
        if k == key:
            t += v
    return t

t = tot(rr, "foo")
print(t)





