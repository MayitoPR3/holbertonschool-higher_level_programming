#!/usr/bin/python3


class SwimMixin:
    """class named SwimMixin"""
    def swim(self):
        """defines that the creature swims"""
        print("The creature swims!")


class FlyMixin:
    """defines that the creature flies"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class named Dragon"""
    def roar(self):
        """defines the dragon roars"""
        print("The dragon roars!")
