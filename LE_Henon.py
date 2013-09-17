# encoding: utf-8
from pylab import *
import math

# a=[0.4, 1.0] period doubling
# a=[1.0+,] chaos starts to appear

#_a = 1.4
_b = 0.3

def f(px,py,pa,pb):
    return (1 - pa*px*px + pb*py, px)

d0 = 0.0000000000001
aList = []
leList = []

for a in arange(0.1, 1.5, 0.001):
    lsum = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = d0
    lambdaList = 0
    for l in xrange(1,32100):
        x1, y1 = f(x1, y1, a, _b)
        x2, y2 = f(x2, y2, a, _b)
        # Lyapunov  
        d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        x2 = x1 + (d0 / d1) * (x2 - x1)
        y2 = y1 + (d0 / d1) * (y2 - y1)
        if l > 100:
            lsum += math.log(d1/d0)
            lambdaList += 1
        if math.fabs(x1) > 1000:
            print l, "breaking"
            break
    try:
        le = lsum / lambdaList+.0
        aList.append(a)
        leList.append(le)
        print a, le
    except:
        pass
axis('equal')
axis([0, 1.6, -1.0, 1.0])
plot(aList,leList, 'r,')
show()