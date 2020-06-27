"""
Author: AlwaysStudent
PythonVersion: 3.7
"""


class Jacobi:
	def __init__(self, a, m):
		if m % 2 != 1:
			print("[Error] m should be a odd number.")
		else:
			self.a = a
			self.m = m

	def calculator(self):
		_cal(1, self.a, self.m)



def _cal(result, a, m):
	if a > m:
		a = a % m
	while a % 2 == 0:
		a = a / 2
		result *= (-1) ** ((m ** 2 - 1) / 8)


