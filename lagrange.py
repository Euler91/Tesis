from numpy.polynomial import Polynomial as P
from fractions import Fraction as fr
import Ank

def lagrange(xl, yl):
	k = len(xl)
	L = P([fr(0, 1)])
	for j in range(k):
		lj = P([fr(1, 1)])
		xj = xl[j]
		for i in range(k):
			xi = xl[i]
			if i != j:
				lj = lj * P([fr(- xi, xj - xi), fr(1, xj - xi)])
		L = L + fr(yl[j], 1) * lj
	return L

def card_poly(k):
	x = []
	y = []
	for i in range(k + 1):
		n = k + 2 + i
		x.append(n)
		y.append(Ank.card_ank(n, k))
	p = lagrange(x, y)
	return p

for i in range(5, 11):
	p = card_poly(i)
	print p

"""
poly([-16198 149752/15 -2480 312 -20 8/15])

poly([119870 -1126936/15 886592/45 -8320/3 1996/9 -48/5 8/45])

poly([-896406 59745032/105 -2326784/15 1060912/45 -6484/3 5392/45 -56/15 16/315])

poly([6757582 -90968648/21 383048368/315 -2931296/15 885848/45 -3824/3 2336/45 -128/105 4/315])

poly([-51265126 10433497112/315 -2996678416/315 904473056/567 -7749856/45 1677464/135 -26992/45 3536/189 -12/35 8/2835])
"""
