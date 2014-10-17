def isprimeF(n, b):
	return (pow(b, n-1, n) == 1)

def isprimeE(n, b):
	if (not isprimeF(n, b)):
		return False
	r = n - 1
	while (r % 2 == 0):
		r //= 2
	c = pow(b, r, n)
	if (c == 1):
		return True
	while (1):
		if (c == 1):
			return False
		if (c == n-1):
			return True
		c = pow(c, 2, n)
