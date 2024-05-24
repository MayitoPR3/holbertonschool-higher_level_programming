#!/usr/bin/python3


class Fish:
    """class to represent Fish"""
    def swim(self):
        """defines that the Fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """defines Fish habitat"""
        print("The fish lives in water")


class Bird:
    """class for the Bird"""
    def fly(self):
        """defines that the Bird flies"""
        print("The bird is flying")

    def habitat(self):
        """defines the Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """class for the FlyingFish"""
    def fly(self):
        """defines that it flies"""
        print("The flying fish is soaring!")

    def swim(self):
        """defines that it swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """defines habitat"""
        print("The flying fish lives both in water and the sky!")
