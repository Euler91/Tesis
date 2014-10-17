import itertools as it
import random
import primality_test as pt

#Definimos el conjunto de signos
sign = [1, -1]

"""
	Input:  k >= 1
	Output: Producto cartesiano de sign consigo mismo k veces
"""
def gen_signs(k):
	return list(it.product(sign, repeat = k))

"""
	Input:  n > k >= 1
	Output: Lista de subconjuntos de tamano k del conjunto de indices (0, 1, ..., n-1)
"""
def sub_n_k_sets(n, k):
	return list(it.combinations(range(n), k))

"""
	Input:  n > 1
	Output: Lista de potencias de 2, (2^1, 2^1, ..., 2^n)
"""
def gen_pows_2(n):
	lst = []
	two = 2
	for i in range(n):
		lst.append(two)
		two = two * 2
	return lst

"""
	Input:  kset, subconjunto de tamano k del conjunto (0, 1, ..., n-1)
			ksign, conjunto de k signos
			pows, lista de potencias de 2 (2^1, 2^2, ..., 2^n)
			k >= 1
			pown, 2^n
	Output: Valor de la suma de pown mas las respectivas potencias de 2 signadas
"""
def eval_n_k_set(kset, ksign, pows, k, pown):
	sum = pown + ksign[0]
	for i in range(k):
		sum = sum + pows[kset[i]] * ksign[i+1]
	return sum

"""
	Input:  casos, producto cartesiano de todos los subconjuntos de tamano k
				   con todos los conjuntos de k signos
			pows, lista de potencias de 2 (2^1, 2^2, ..., 2^n)
			k >= 1
			pown, 2^n
	Output: Conjunto A_nk, en formato de diccionario
"""
def gen_A_nk(casos, pows, k, pown):
	A_nk = {}
	for item in casos:
		sum = eval_n_k_set(item[0], item[1], pows, k, pown)
		if sum in A_nk:
			A_nk[sum] += 1
		else:
			A_nk[sum] = 1
	return A_nk

"""
	Input:  dic, un diccionario con elementos de la forma (valor, repeticiones)
			n > 1
	Output: Lista con dos listas, la de primos y la de compuestos
"""
def get_primes(dic, n):
	primes = []
	composites = []
	for key in dic.keys():
		b = random.randrange(2, n - 1)
		if pt.isprimeE(key, b):
			primes.append((key, dic[key]))
		else:
			composites.append((key, dic[key]))
	return [primes, composites]

"""
	Input:  a > b > 1
			k >= 1
	Output: Lista de ternas de la forma (n, cantidad de primos en A_nk, cantidad de compuestos en A_nk)
"""
def count_in_range(a, b, k):
    lst = []
    for n in range(a, b + 1):
        pows = gen_pows_2(n - 1)
        pows.reverse()
        pown = 2 ** n
        kset = sub_n_k_sets(n - 1, k)
        ksign = gen_signs(k + 1)
        casos = list(it.product(kset, ksign))
        Ank = gen_A_nk(casos, pows, k, pown)
        lists = get_primes(Ank, n)
        lst.append( ( n, len(lists[0]), len(lists[1]) ) )
    return lst

"""
	Input:  n > k >= 1
	Output: Conjunto A_nk en formato de diccionario
"""
def set_Ank(n, k):
	pows = gen_pows_2(n - 1)
	pows.reverse()
	pown = 2 ** n
	kset = sub_n_k_sets(n - 1, k)
	ksign = gen_signs(k + 1)
	casos = list(it.product(kset, ksign))
	Ank = gen_A_nk(casos, pows, k, pown)
	return Ank

"""
	Input:  n > k >= 1
	Output: Cardinalidad del conjunto A_nk
"""
def card_ank(n, k):
	pows = gen_pows_2(n - 1)
	pows.reverse()
	pown = 2 ** n
	kset = sub_n_k_sets(n - 1, k)
	ksign = gen_signs(k + 1)
	casos = list(it.product(kset, ksign))
	Ank = gen_A_nk(casos, pows, k, pown)
	return len(Ank)
