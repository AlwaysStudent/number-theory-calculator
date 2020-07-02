"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import base


class Jacobi(base.Process, base.Value):
	def __init__(self, a, m):
		if m % 2 != 1:
			self.a = -1
			self.m = -1
		else:
			self.a = a
			self.m = m

	def process(self) -> str:
		value = 1
		a = self.a
		m = self.m
		result = "$$ \\begin{aligned} (\\frac{" + str(a) + "}{" + str(m) + "})"
		if a % m != a:
			a = a % m
			result += " &=& (\\frac{" + str(a) + "}{" + str(m) + "}) \\\\"
		while a % m != 1 and a % m != (m - 1) and a % m != 2:
			if a > m // 2:
				a = m - a
				result += " &=& {" + str(value) + "} * (\\frac{" + str(-a) + "}{" + str(m) + "}) \\\\ "
				value = value * ((-1) ** int(((m - 1) / 2)))
				result += " &=& {" + str(value) + "} * ({-1}) ^ {\\frac{" + str(m) + " - 1}{2}} * (\\frac{" + str(a) + "}{" + str(m) + "}) \\\\ "
			if judge(a, m) == 1:
				break
			while a % 2 == 0:
				result += " &=& {" + str(value) + "} * (\\frac{2}{" + str(m) + "}) * (\\frac{" + str(a // 2) + "}{" + str(m) + "}) \\\\ "
				a = a // 2
				value = value * ((-1) ** int(((m ** 2 - 1) / 8)))
				result += " &=& {" + str(value) + "} * ({-1}) ^ {\\frac{{" + str(m) + "} ^ {2} - {1}}{8}} * {\\frac{" + str(a // 2) + "}{" + str(m) + "}) \\\\ "
			if judge(a, m) == 1:
				break
			result += "&=& {" + str(value) + "} * (\\frac{" + str(a) + "}{" + str(m) + "}) \\\\ "
			a, m = m, a
			result += "&=& {" + str(value) + "} * ({-1})^{\\frac{"+str(a)+"-{1}}{2}*\\frac{"+str(m)+"-{1}}{2}} *(\\frac{" + str(a) + "}{" + str(m) + "}) \\\\ "
			value = value * ((-1) ** int(((a - 1) * (m - 1) / 4)))
			a = a % m
			result += "&=&{" + str(value) + "} * (\\frac{" + str(a) + "}{" + str(m) + "}) \\\\ "
		if a % m != a:
			a = a % m
			result += " &=& {" + str(value) + "} * (\\frac{" + str(a) + "}{" + str(m) + "}) \\\\"
		if a % m == (m - 1):
			result += " &=& {" + str(value) + "} * ({-1}) ^ {\\frac{" + str(m) + " - {1}}{2}  \\\\ "
			value = value * ((-1) ** int(((m - 1) / 2)))
		elif a % m == 2:
			result += " &=& {" + str(value) + "} * ({-1}) ^ {\\frac{{" + str(m) + "} ^ {2} - {1}}{8}}  \\\\ "
			value = value * ((-1) ** int(((m ** 2 - 1) / 8)))
		result += " &=& {" + str(value) + "}"
		return result + " \end{aligned} $$"

	def value(self):
		result = 1
		a = self.a % self.m
		m = self.m
		while a % m != 1 and a % m != (m - 1) and a % m != 2:
			if a > m // 2:
				a = m - a
				result = result * ((-1) ** int(((m - 1) / 2)))
			if judge(a, m) == 1:
				break
			while a % 2 == 0:
				result = result * ((-1) ** int(((m ** 2 - 1) / 8)))
				a = a // 2
			if judge(a, m) == 1:
				break
			a, m = m, a
			result = result * ((-1) ** int(((a - 1) * (m - 1) / 4)))
			a = a % m
		if a % m == (m - 1):
			result = result * ((-1) ** int(((m - 1) / 2)))
		elif a % m == 2:
			result = result * ((-1) ** int(((m ** 2 - 1) / 8)))
		return result


def judge(a, m):
	if a % m == 1 or a % m == (m - 1) or a % m == 2:
		return 1


def main():
	x = Jacobi(286, 563)
	print(x.process())


if __name__ == '__main__':
	main()

