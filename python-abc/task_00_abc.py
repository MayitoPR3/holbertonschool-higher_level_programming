#!/usr/bin/python3
"""
_summary_
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Parent Class for Animals"""

    @abstractmethod
    def sound(self):
        """
        Defines the abstract class Animal
        """
        pass


class Dog(Animal):
    """Class for Dog"""
    def sound(self):
        """Defines the sound of bark for Dog class"""
        return "Bark"


class Cat(Animal):
    """Class for Cat"""
    def sound(self):
        """Defines the sound of Meow for Cat class"""
        return "Meow"
