from abc import ABCMeta, abstractmethod


class Process(metaclass=ABCMeta):
	@abstractmethod
	def process(self) -> str:
		pass


class Value(metaclass=ABCMeta):
	@abstractmethod
	def value(self):
		pass


class Encrypto(metaclass=ABCMeta):
	@abstractmethod
	def encrypto(self, plain_text):
		pass


class Decrypto(metaclass=ABCMeta):
	@abstractmethod
	def decrypto(self, crypto_text):
		pass


if __name__ == '__main__':
	pass
