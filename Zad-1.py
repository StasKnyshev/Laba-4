import random
def srb(x):
    if len(x) <= 1:
        return x
    else:
        i = random.choice(x)
    l = [n for n in x if n < i]
    d = [i] * x.count(i)
    r = [n for n in x if n > i]
    return srb(l) + d + srb(r)

def rasсh(x):
    s = len(x)
    w = True
    while s > 1 or w:
        s = max(1, int(s / 1.247))
        w = False
        for j in range((len(x)) - s):
            g = j + s
            if x[j] > x[g]:
                x[j], x[g] = x[g], x[j]
                w = True
    return x