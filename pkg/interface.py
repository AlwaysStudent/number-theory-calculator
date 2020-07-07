"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
from abc import ABCMeta, abstractmethod


class Process(metaclass=ABCMeta):
	@abstractmethod
	def process(self) -> str:
		pass


class Value(metaclass=ABCMeta):
	@abstractmethod
	def value(self):
		pass


class Encode(metaclass=ABCMeta):
	@abstractmethod
	def encode(self, plain_text):
		pass


class Decode(metaclass=ABCMeta):
	@abstractmethod
	def decode(self, crypto_text):
		pass


if __name__ == '__main__':
	pass
