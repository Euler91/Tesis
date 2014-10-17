from pylab import *
import scipy.interpolate as si
import Ank

def card_poly(k):
	x = []
	y = []
	for i in range(k + 1):
		n = k + 2 + i
		x.append(n)
		y.append(Ank.card_ank(n, k))
	p = si.lagrange(x, y)
	return p

for i in range(2, 4):
	p = card_poly(i)
	print p

"""
        5      4       3        2
0.5333 x - 20 x + 312 x - 2480 x + 9983 x - 1.62e+04
        6       5         4        3            2
0.1778 x - 9.6 x + 221.8 x - 2773 x + 1.97e+04 x - 7.513e+04 x + 1.199e+05
         7         6         5        4             3             2
0.05079 x - 3.733 x + 119.8 x - 2161 x + 2.358e+04 x - 1.551e+05 x + 5.69e+05 x - 8.964e+05
        8         7         6        5             4             3
0.0127 x - 1.219 x + 51.91 x - 1275 x + 1.969e+04 x - 1.954e+05 x
              2
 + 1.216e+06 x - 4.332e+06 x + 6.758e+06
          9          8         7         6             5             4
0.002822 x - 0.3429 x + 18.71 x - 599.8 x + 1.243e+04 x - 1.722e+05 x
              3             2
 + 1.595e+06 x - 9.513e+06 x + 3.312e+07 x - 5.127e+07
"""
