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

	def process(self):
		pass

	def value(self):
		pass


def main():
	pass


if __name__ == '__main__':
	main()

