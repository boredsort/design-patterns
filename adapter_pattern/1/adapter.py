"""Adapter design pattern
"""

from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        """An abstract method A"""

class ClassA(IA):
    def method_a(self):
        print("method A")


class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_b():
        """An Abstract method B"""

class ClassB(IB):
    def method_b(self):
        print("method B")

class ClassBAdapter(IA):
    def __init__(self):
        self.classB = ClassB()

    def method_a(self):
        """Class class B method B"""
        self.classB.method_b()

ITEM = ClassA()
ITEM.method_a()


