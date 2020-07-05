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
