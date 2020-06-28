"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import base


class DivMod(base.Process, base.Value):
	def __init__(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p

	def process(self) -> str:
		a = self.a
		b = self.b
		p = self.p
		other = 1
		result_str = "$$ \\begin{aligned} {" + str(a) + "}^{" + str(b) + "} \;{mod}\; {" + str(p) + "}"
		while a != 1 and b != 1:
			result_str += "&\equiv& \;"
			if b % 2 == 0:
				result_str += "{" + str(other) + "}*" + "({" + str(a) + "} ^ {2})^{" + str(b/2) + "} \;{mod}\; {" + str(p) + "}\\\\"
				a = a * a % p
				b = int(b / 2)
			else:
				result_str += "{" + str(other) + "}*{" + str(a) + "} * {" + str(a) + "}^{" + str(b- 1) + "} \;{mod}\; {" + str(p) + "}\\\\"
				other *= a
				b = b - 1
			other %= p
			result_str += "&\equiv& \;{"+str(other)+"}*{" + str(a) + "}^{" + str(b) + "} \;{mod}\; {" + str(p) +"}\\\\"

		if a == 1:
			result_str += "&\equiv& \; {" + str(a) + "} \;{mod}\; {" + str(p) +"}\\\\"
		elif b == 1:
			result_str += "&\equiv& \; {" + str(a * other % p) + "} \;{mod}\; {" + str(p) +"}\\\\"
		return result_str + "\\end{aligned} $$"

	def value(self):
		a = self.a
		b = self.b
		p = self.p
		other = 1
		while a != 1 and b != 1:
			if b % 2 == 0:
				a = a * a % p
				b = int(b / 2)
			else:
				other *= a
				b = b - 1
			other %= p

		if a == 1:
			return a
		elif b == 1:
			return a * other % p

	def reset(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p


def main():
	d = DivMod(23, 105, 31)
	x = d.process()
	print(x)


if __name__ == '__main__':
	main()
