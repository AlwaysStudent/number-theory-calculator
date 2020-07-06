"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import Interface


class PowerMod(Interface.Process, Interface.Value):
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
			result_str += "&\equiv \;"
			if b % 2 == 0:
				result_str += "{" + str(other) + "}*" + "({" + str(a) + "} ^ {2})^{" + str(b//2) + "} \;{mod}\; {" + str(p) + "}\\\\"
				a = a * a % p
				b = int(b / 2)
			else:
				result_str += "{" + str(other) + "}*{" + str(a) + "} * {" + str(a) + "}^{" + str(b - 1) + "} \;{mod}\; {" + str(p) + "}\\\\"
				other *= a
				b = b - 1
			other %= p
			result_str += "&\equiv \;{"+str(other)+"}*{" + str(a) + "}^{" + str(b) + "} \;{mod}\; {" + str(p) +"}\\\\"

		result_str += "&\equiv \; {" + str(a * other % p) + "} \;{mod}\; {" + str(p) +"}\\\\"
		return result_str + "\\end{aligned} $$"

	def value(self):
		a = self.a
		b = self.b
		p = self.p
		other = 1
		while a != 1 and b != 1:
			if b % 2 == 0:
				a = a * a % p
				b = b // 2
			else:
				other *= a
				b = b - 1
			other %= p

		return a * other % p

	def reset(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p


def main():
	d = PowerMod(7436133, 893757623151968546283637638899442808021098453179411214608595, 1125462283718436691277195836049780558406143209043783553843055)
	d1 = PowerMod(848621962257723720981692265660116543140807576731957426725602, 398060176530948938286368548018134344346374814870348726396683, 1125462283718436691277195836049780558406143209043783553843055)
	x = d.value()
	y = d1.value()
	print(x)
	print(y)
	print(pow(7436133, 102860041892705348374968750821439727614888888193859070233443, 1034875383501851225162176146739552686685173972413185352398045))
	print(pow(438183029114329075967406214470176287011931617856231048068283, 443540622442318561601874925630290974589996477090745719672067, 1034875383501851225162176146739552686685173972413185352398045))
	print(pow(7436133, 102860041892705348374968750821439727614888888193859070233443 * 443540622442318561601874925630290974589996477090745719672067, 1034875383501851225162176146739552686685173972413185352398045))


if __name__ == '__main__':
	main()
