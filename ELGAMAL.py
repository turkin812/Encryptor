import random
from math import pow
import numpy as np

class MyELGAMAL:
	def __init__(self):
		pass

	def gcd(self, a, b):
		if a < b:
			return self.gcd(b, a)
		elif a % b == 0:
			return b
		else:
			return self.gcd(b, a % b)

	# Генерация болших случайных чисел
	def gen_key(self, q):
		key = random.randint(pow(10, 20), q)

		while self.gcd(q, key) != 1:
			key = random.randint(pow(10, 20), q)
		return key

	# Модульное произведение в степень
	def power(self, a, b, c):
		x = 1
		y = a
		while b > 0:
			if b % 2 == 0:
				x = (x * y) % c
			y = (y * y) % c
			b = int(b/2)
		return x % c

	def modexp(self, a, b, c):
		a %= c
		pow = 0
		if b == 0:
			pow = 1
		elif b % 2 == 0:
			pow = self.modexp(a*a, b/2, c)%c
		else:
			pow = (a*self.modexp(a, b-1, c))%c
		return pow

	def generator(self, p):
		# Перебор делителей
		fact = []
		phi = p - 1
		n = phi
		for i in range(2, n):
			if phi % i == 0:
				fact.append(i)
				while phi % i == 0:
					phi /= i

		# Поиск первообразного корня
		for g in range(2, p + 1):
			k = 0
			y = 0
			for i in range(0, len(fact)):
				ab = n / fact[i]
				y = self.modexp(g, ab, p)
				if y == 1:
					break
				k += 1
			if k == len(fact):
				return g
		return -1

	def generator_p(self):
		n = 0
		while n!=10:
			n = 0
			rnd = "1"
			b = []
			for i in range(0,10):
				b.append(0)
			for i in range(0, 20):
				rnd += str(random.randint(0, 1))
			rnd += "1"
			bmodp = 0
			p = int(rnd, 2)
			#Ferma
			for j in range(0,10):
				b[j] = random.randint(0, p-1)
				bmodp = self.power(b[j], p-1, p)
				if bmodp !=1:
					break
				else:
					n = n + 1
		return p

	def invmod(self, a, m):
		if ((a < 1) and (m < 2)):
			return -1
		u1 = m
		u2 = 0
		v1 = a
		v2 = 1
		while v1 != 0:
			q = int(u1/v1)
			t1 = u1 - (q*v1)
			t2 = u2 - (q*v2)

			u1 = v1
			u2 = v2
			v1 = t1
			v2 = t2
		if u1 == 1:
			return ((u2 + m) % m)
		else:
			return -1


	# Асимметричное шифрование
	def encrypt(self, msg, k, h, g, q):
		en_msg = []
		# k = self.gen_key(q) # Сессионный ключ ////// Закрытый ключ для отправителя - сессионный ключ (от 1 до q-1)

		s = self.power(h, k, q) # B = Y^k * M mod p
		p = self.power(g, k, q) # A = g^k mod(p)

		# print('g^k used: ', p) # A
		# print('g^ak used: ', s) # Почти B
		for i in range(0, len(msg)):
			en_msg.append(msg[i])
		for i in range(0, len(en_msg)):
			 # Это B
			en_msg[i]=s*ord(en_msg[i])
			# en_msg.append(s * ord(v))
			# Отправляем шифротекст (A, B) and public key: (p,g,Y)
		return en_msg, p


	def decrypt(self, en_msg, key, p, q):
		dr_msg = []
		h = self.power(p, key, q)
		for i in range(0, len(en_msg)):
			dr_msg.append(chr(int(en_msg[i]/h)))
			# ik = p*self.power(v, q-1-key, q)
			# en_msg.append(chr(ik))
			#dr_msg.append(chr((int(en_msg[i])*(self.power(p, q-1-key, q))))) # M = B*A^(p-1-X) mod p; en_msg[i]*power(p, q-1-key, q)  en_msg[i]/h
		return dr_msg

	#def main(self):
	#	msg = 'Laura'
	#
	#		print('Original Message: ', msg)
	#		q = random.randint(pow(10, 20), pow(10, 50)) # - p
	#		g = random.randint(2, q) # g
	#		key = gen_key(q) # Закрытый ключ для получателя -X (допустим оно простое)
	#
	#		h = power(g, key, q) # - Y => h, q, g - открытый ключ: (p, g, h) - закрытый: key; в нашей сист открытый это q, g, h
	#		print('g used: ', g)
	#		print('g^a used: ', h)
	#
	#		en_msg, p = encrypt(msg, q, h, g) # пара- шифр текст, отправляем шифр текст и открытый ключ (выводим) + закрытый ключ X
	#		dr_msg = decrypt(en_msg, p, key, q) #Берем секретный ключ X и Боря по формуле расшифровывает 
	#
	#		print(''.join(dr_msg))
	

if __name__ == '__main__':
	md = MyELGAMAL()