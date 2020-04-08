#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Base1():
    def print(self):
        print("Base1")
        print(self)


class Base2():
    def print(self):
        print("Base2")
        print(self)


class Derived(Base1, Base2):
    def print(self):
        # Calls Base1 method.
        super().print()
        # Calls Base1 method.
        super(Derived, self).print()
        # Calls Base2 method.
        Base2.print(self)


def main():
    print("Multiple inheritance experiment in python 3")
    obj = Derived()
    obj.print()
    print(Derived.mro())


if __name__ == '__main__':
    main()
