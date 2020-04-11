# Base Method Calls in Python Multiple Inheritance

Python allows multiple inheritance. Method resolution order in Python is a
quite interesting topic, and it's possible to read more
[here](https://www.python.org/download/releases/2.3/mro). The idea of this blog
post is to show options when it comes to calling methods from the base classes.

If a class is extended from multiple classes like in the example below

```python
class Base1():
    def print(self):
        print("Base1")
        print(self)

class Base2():
    def print(self):
        print("Base2")
        print(self)
```

both calls

```python
class Derived(Base1, Base2):
    def print(self):
        # Calls Base1 method.
        super().print()
        # Calls Base1 method.
        super(Derived, self).print()
```

are going to call `print` method from `Base1` class.  If a caller wants to
call the `print` method from `Base2` class, an explicit call is required.

```python
class Derived(Base1, Base2):
    def print(self):
        # Calls Base2 method.
        Base2.print(self)
```

The full Python script can be found
[here](https://github.com/gitbuda/blog/blob/master/content/2019/11/23/code/main.py).

## Resources

* <https://www.python.org/download/releases/2.3/mro>
* <https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance>
* <https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc>
* <https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path>
