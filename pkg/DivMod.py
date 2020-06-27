"""
Author: AlwaysStudent
PythonVersion: 3.7
"""


class DivMod:
	def __init__(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p
		self.value = self.__run()

	def __run(self):
		a = self.a
		b = self.b
		p = self.p
		while a != 1 and b != 1:
			if b % 2 == 0:
				a = a * a % p
				b = b / 2
			else:
				a = a * self.a % p

		if a == 1:
			return 1
		if b == 1:
			return a % p

	def print(self):
		print(self.a, self.b, self.value, self.p)
		print("$$ {%d}^{%d} \equiv {%d} \;\mathnormal{mod}\; {%d} $$" % (self.a, self.b, self.value, self.p))


def main():
	d = DivMod(3, 1024, 10)
	d.print()


if __name__ == '__main__':
	main()
