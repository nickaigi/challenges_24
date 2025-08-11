"""
Derived from https://realpython.com/python-metaclasses/

Metaclasses allow you to define the behavior of classes.
They act as the blueprint for creating classes and can modify class creation and behavior.

"type" is a metaclass of which classes are instances.
Just as an ordinary object is an instance of a class, any new-style class in Python and thus any class in Python 3 is an instance of the 'type' metaclass.

You can call type() with three args: type(<name>, <bases>, <dct>)
    <name> specifies the class name. This becomes the __name__ attribute of the class

    <bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class

    <dct> specifies a 'namespace dictionary' containing definitions for the class body. This becomes the __dict__ attribute of the class

Calling 'type' in this manner creates a new instance of the 'type' metaclass -> "It dynamically creates a new class"
"""

class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


if __name__ == '__main__':
    # Example 1
    # <bases> and <dct> args are both empty.
    # no inheritance from any parent, and nothing is initially placed in the namespace dictionary
    Foo = type('Foo', (), {})
    x = Foo()
    print(x)

    # Example 1
    Bar = type('Bar', (Foo,), dict(attr=100))
    x = Bar()
    print(x.attr)  # 100

    print(x.__class__)  # <class '__main__.Bar'>
    print(x.__class__.__bases__)  # <class '__main__.Foo'>
    
    # Example 3
    # <bases> is emtpy
    # two objects are placed in the namespace dictionary via the <dct> argument.
    # attr : an attirbute
    # attr_val : a function which becomes a method of the defined class
    Foo = type(
        'Foo',
        (),
        {
            'attr': 100,
            'attr_val': lambda x: x.attr
        }
    )

    x = Foo()
    print(x.attr)  # 100
    print(x.attr_val())  # 100

    class Foo:
        pass

    f = Foo()

    # The expression Foo() creates a new instance of class Foo.
    # When the interpreter encounters Foo(), the following occurs:
    # 1. The __call__() method of Foo's parent class is called.
    # Since Foo is a standard new-style class, its parent class is the 'type' metaclass, so type's __call__() method is invoked
    #
    # 2. that __call__() method in turn invokes the following:
    #     __new__()
    #     __init__()
    


