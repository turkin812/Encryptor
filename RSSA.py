import random
import numpy as np
import sys

class MyRSA:
	def __init__(self):
		self.array = []

	@staticmethod
	def divider(n):
		i = 2
		j = 0 # флаг
		while i**2 <= n and j != 1:
			if n%i == 0:
				j = 1
			i += 1
		if j == 1:
			return False
		else:
			return True

	def p_q(self):
		p = 0
		q = 0
		i = 0
		while i != 10:
			p = random.randint(2 ** 15, 2 ** 16)
			if self.divider(p):
				i += 1
			else:
				continue
		j = 0
		while j != 10:
			q = random.randint(2**15, 2**16)
			if self.divider(q):
				j += 1
			else:
				continue
		return p*q, (p-1)*(q-1)



	@staticmethod
	def gcd(a: int, b: int):
		while b!=0:
			a,b=b,a%b
		return a
	sys.setrecursionlimit(1000000000)
	def E(self, f: int):
		e = 0
		while True:
			e = random.randint(0, f)
			if self.gcd(e, f) == 1:
				break
			else:
				continue
		return e

	def get_d(self, e: int, f: int):
		i=0
		while True:
			if (e*i)%f == 1:
				return i
			else:
				i+=1

	def ext_gcd(self, a: int, b: int):
		if b == 0:
			x1 = 1
			y1 = 0
			x = x1
			y = y1
			r = a
			return r, x, y
		else:
			r, x1, y1 = self.ext_gcd(b, a % b)
			x = y1
			y = x1 - (a // b) * y1
			return r, x, y

	#sys.setrecursionlimit(1000000000)
	def pow_h_1(self, x: int, y: int, N: int):
		if y == 0:
			return 1
		z = self.pow_h(x, y//2, N)
		if (y % 2 == 0):
			return (z*z)%N
		else:
			return (x*z*z)%N

	def pow_h(self, number, degree, mod):
		if degree == 0:
			return 1
		result = 1
		while degree > 0:
			if degree % 2 == 1:
				result = (result*number)%mod
			degree /=2
			number = (number*number)%mod
		return result



		

	def encode_RSA(self, word: str):
		N, f = self.p_q()
		e = self.E(f)
		ret = []
		for v in word:
			n = ord(v)
			ret.append(self.pow_h(n,e,N))
		return ret, N, e, f

	def decode_RSA(self, word: list, N: int, e: int, f: int, r:int, d:int, y:int):
		#r, d, y = self.ext_gcd(e, f)
		ret = []
		for v in word:
			sim = self.pow_h(v,d,N)
			ret.append(chr(sim))
		return np.array(ret)
	
	# l = encode_RSA(otherString)

	# s = decode_RSA(l,d,N)

if __name__ == '__main__':
	md = MyRSA()