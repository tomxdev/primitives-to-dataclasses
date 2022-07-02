# primitives-to-dataclasses
Avoiding the complexity of the primitives


## Namedtuple
Key Features for a NamedTuple.
* **Imutable**
  * Does not allow receiving new values by assignment.
  * Keeps the same state until the end of execution.
* **Representation**
  * Implement __repr__ and __str__
* **Is comparable**
  * Implement __eq__
* **Is dynamically created**
  * namedtuple('name', *args)
  
## Namedtuple with typing
Key Features for a NamedTuple with typing.
* **Imutable**
  * Maybe you don't want
* **Extension**
  * Cannot extend tuples(inheritance).
* The representation of the object is always complete.
* Cannot create methods or functions.