# python-Classes-as-Objects
This repository talks about type, metclasses etc. features existing in python.

Lets declare a class in python and create object from it as below:

```py
class ObjectCreator(object):
  pass
>>> my_obj = ObjectCreator()
>>> print(my_obj)
<__main__.ObjectCreator object at 0x0000027ADB911B70>
```
We say classes are pieces of code that describe how to produce an object and thats true in python too. However, classes are more than that in python. Classes are objects themselves in python world.

Now since classs is an object:-
- we can assign class to a variable
- we can copy it
- we can add attributes to it
- we can pass it as a function parameter

Please refer to these [code files](https://github.com/SadkiratSingh/python-Classes-as-Objects/blob/main/classes-as-object.py) here which make use of python classes as objects.


