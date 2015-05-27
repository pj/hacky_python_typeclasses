# Hacky typeclasses for Python

Basically the idea is to use python decorators to fake Haskell typeclasses (badly).

To create a method for a typeclass:

```python
from typeclass import typemethod

class Show(object):
    pass

@typemethod(Show)
def show(val):
    # If there is no default then just raise NotImplementedError()
    return str(val)
```

To create an instance:

```python
from typeclass import typeinstance
import show

class Something(object):
    def __init__(self, a):
        self.a = a

@typeinstance(Something, show.show)
def show(val):
    return "Something: " + str(val.a)
```

Then use it by importing the show method from the typeclass and ensuring that
the instance is loaded:

```python
from show import show
from something import Something

print show(Something(42))
```
