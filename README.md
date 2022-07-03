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

## Value Object
There is a pattern called 'Value Object', which aims to create a class to represent the domain, that is, we must create an object to represent an abstraction.

With this abstraction we have some advantages:
* **Mutable/Imutable**
  * Leaving the decision with the developer.
* **Extension**
  * Allowed use of inheritance.
* **Methods**
  * Allowed use of methods.


## Value Object with the same behaviour as a namedtuple object
To have the same behavior as a namedtuple you need to implement the methods below:
* **__eq__**
* **__repr__**


## Dataclasses
Dataclasses were created with the aim of facilitating domain-specific objects, and through them we have the behavior of a Value Object and a namedtuple together.
