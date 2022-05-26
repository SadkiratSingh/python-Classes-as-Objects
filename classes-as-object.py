# creating classes dynamically
## since classes as objects, we can create them on the fly just like objects.

def choose_class(name):
    if(name == "foo"):
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

print(choose_class("foo"))

#passing class as arguments to functions

class ObjectCreator:
    pass

def echo(o):
    print(o)

echo(ObjectCreator)
echo.__call__(ObjectCreator)


#adding attributes to classes
ObjectCreator.new_attribute = "foo"
print(hasattr(ObjectCreator, "new_attribute"))

#assigning to a variable
a = ObjectCreator
print(a())