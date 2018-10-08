# 0x06. Python - Classes and Objects

## Target

- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance

- What is an attribute

- What are and how to use public, protected and private attributes

- What is self

- What is a method

- What is the special __init__ method and how to use it

- What is Data Abstraction, Data Encapsulation, and Information Hiding

- What is a property

- What is the difference between an attribute and a property in Python

- What is the Pythonic way to write getters and setters in Python

advanced:

- How to dynamically create arbitrary new attributes for existing instances of a class

- How to bind attributes to object and classes

- What is and what does contain __dict__ of a class and of an instance of a class

- How does Python find the attributes of an object or class
How to use the getattr function

## 0. My first square

Write an empty class Square that defines a square:

You are not allowed to import any module

File: 0-square.py

## 1. Square with size

Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size

Instantiation with size (no type/value verification)

You are not allowed to import any module

Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

File: 1-square.py

## 2. Size validation

Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

You are not allowed to import any module

File: 2-square.py

## 3. Area of a square

Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size

Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

Public instance method: def area(self): that returns the current square area

You are not allowed to import any module

File: 3-square.py

## 4. Access and update private attribute

Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:

property def size(self): to retrieve it

property setter def size(self, value): to set it:

 - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

 - if size is less than 0, raise a ValueError exception with the message size must be >= 0

Instantiation with optional size: def __init__(self, size=0):

Public instance method: def area(self): that returns the current square area

You are not allowed to import any module

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignation of a private attribute and also define how this one will be available from outside (get the attribute value) - by copy? by assignation, etc. Also, adding type/value validation in the setter will centralize the logic, you will do it in only one place.

File: 4-square.py

## 5. Printing a square

Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:

 - property def size(self): to retrieve it

 - property setter def size(self, value): to set it:

   - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

   - if size is less than 0, raise a ValueError exception with the message size must be >= 0

Instantiation with optional size: def __init__(self, size=0):

Public instance method: def area(self): that returns the current square area

Public instance method: def my_print(self): that prints in stdout the square with the character #:

 - if size is equal to 0, print an empty line

You are not allowed to import any module

File: 5-square.py

## 6. Coordinates of a square

Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:

 - property def size(self): to retrieve it

 - property setter def size(self, value): to set it:

   - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

   - if size is less than 0, raise a ValueError exception with the message size must be >= 0

Private instance attribute: position:

 - property def position(self): to retrieve it

 - property setter def position(self, value): to set it:

   - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers

Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):

Public instance method: def area(self): that returns the current square area

Public instance method: def my_print(self): that prints in stdout the square with the character #:

 - if size is equal to 0, print an empty line

 - position should be use by using space - Don’t fill lines by spaces when position[1] > 0

You are not allowed to import any module

File: 6-square.py

## 7. Singly linked list

Write a class Node that defines a node of a singly linked list by:

Private instance attribute: data:

 - property def data(self): to retrieve it

 - property setter def data(self, value): to set it:

   -data must be an integer, otherwise raise a TypeError exception with the message data must be an integer

Private instance attribute: next_node:

 - property def next_node(self): to retrieve it

 - property setter def next_node(self, value): to set it:

   - next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object

Instantiation with data and next_node: def __init__(self, data, next_node=None):

And, write a class SinglyLinkedList that defines a singly linked list by:

 - Private instance attribute: head (no setter or getter)

 - Simple instantiation: def __init__(self):

 - Should be printable:

   - print the entire list in stdout

   - one node number by line

 - Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)

 - You are not allowed to import any module

100-singly_linked_list.py

## 8. Print Square instance

Write a class Square that defines a square by: (based on 6-square.py)

Private instance attribute: size:

 - property def size(self): to retrieve it

 - property setter def size(self, value): to set it:

   - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

   - if size is less than 0, raise a ValueError exception with the message size must be >= 0

Private instance attribute: position:

 - property def position(self): to retrieve it

 - property setter def position(self, value): to set it:

   - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer

Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):

Public instance method: def area(self): that returns the current square area

Public instance method: def my_print(self): that prints in stdout the square with the character #:

 - if size is equal to 0, print an empty line

 - position should be use by using space

Printing a Square instance should have the same behavior as my_print()

You are not allowed to import any module

File: 101-square.py

## 9. Compare 2 squares

Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:

 - property def size(self): to retrieve it

 - property setter def size(self, value): to set it:

   - size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number

   - if size is less than 0, raise a ValueError exception with the message size must be >= 0

Instantiation with size: def __init__(self, size=0):

Public instance method: def area(self): that returns the current square area

Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area

You are not allowed to import any module

File: 102-square.py