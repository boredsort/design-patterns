from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """The Builder interface specifies methods for creating the different parts of the 
    Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    """The Concrete builder classes follow the Builder interface and
    provide specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """A fresh builder instance should contain a blank product object, which is
        used in the further assemly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """Concrete Builders are supposed to provide their own methods for retreiving
        results. That's because various types of builders may create entirely different
        products that don't follow the same interface. Therefore, such methods cannot
        be declared in the base Builder interface (at least in a statically typed programming
        language).

        Usually, after returning the end result to the client, a builder instance is expected
        to be ready to start producing another product. That's why it's a usual practice to call
        the reset method at the end of the `getProduct` method body. However, this behavior is
        not mandatory, and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        
        """

        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """It makes sense to use the Builder pattern only when your products are quite complex and
    require extensive configuration

    Unlike in other creational patterns, different concrete builders can produce unrelated products.
    In other words, results of various builders may not always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Products parts: {', '.join(self.parts)}", end="")


class Director:
    """The director works with any builder instance that client code passes to it. This way, the 
    client code may alter the final type of the newly assembled product.
    """
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:

        self._builder = builder

    """The director can construct several product variations using the same building stemps.
    """
    

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Cutom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()