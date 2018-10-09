# 0x09. Python - Everything is object

## Target

- What is an object

- What is the difference between a class and an object or instance

- What is the difference between immutable object and mutable object

- What is a reference

- What is an assignment

- What is an alias

- How to know if two variables are identical

- How to know if two variables are linked to the same object

- How to display the variable identifier (which is the memory address in the CPython implementation)

- What is mutable and immutable

- What are the builtin mutable types

- What are the builtin immutable types

- How does Python pass variables to functions

## Requirement

- Only one line

- No Shebang

- All your files should end with a new line

- All the answers should be only one line in a file. No space before or after the answer.

## 0. Who I am?

What function would you use to print the type of an object? Write the name of the function in the file, without the ()

File: 0-answer.txt

## 1. Where are you?

How to get variable identifier (which is the memory address in the CPython implementation)? Write the name of the function in the file, without the ()

File: 1-answer.txt

## 2. Right count

In the following code, do a and b point to the same object? Answer with Yes or No.

File: 2-answer.txt

## 3. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

File: 3-answer.txt

## 4. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

File: 4-answer.txt

## 5. Right count =+

In the following code, do a and b point to the same object? Answer with Yes or No.

File: 4-answer.txt

## 5. Right count =+

In the following code, do a and b point to the same object? Answer with Yes or No.

File: 5-answer.txt

## 6. Is equal

What should these 3 lines print:

File: 6-answer.txt

## 7. Is the same

What should these 3 lines print:

File: 7-answer.txt

## 8. Is really equal

What should these 3 lines print:

File: 8-answer.txt

## 9. Is really the same

What should these 3 lines print:

File: 9-answer.txt

## 10. And with a list, is it equal

What should these 3 lines print:

File: 10-answer.txt

## 11. And with a list, is it the same

What should these 3 lines print:

File: 11-answer.txt

## 12. And with a list, is it really equal

What should these 3 lines print:

File: 12-answer.txt

## 13. And with a list, is it really the same

What should these 3 lines print:

File: 13-answer.txt

## 14. List append

What does this script print?

l1 = [1, 2, 3]

l2 = l1

l1.append(4)

print(l2)

File: 14-answer.txt

## 15. List add

What does this script print?

l1 = [1, 2, 3]

l2 = l1

l1 = l1 + [4]

print(l2)

File: 15-answer.txt

## 16. Integer incrementation

What does this script print?

def increment(n):

    n += 1

a = 1

increment(a)

print(a)

File: 16-answer.txt

## 17. List incrementation

What does this script print?

def increment(n):

    n.append(4)

l = [1, 2, 3]

increment(l)

print(l)

File: 17-answer.txt

## 18. List assignation

What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]

l2 = [4, 5, 6]

assign_value(l1, l2)

print(l1)

File: 18-answer.txt

## 19. Copy a list object

Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects

Your file should be maximum 3-line long (no documentation needed)

You are not allowed to import any module

File: 19-copy_list.py

## 20. Tuple or not?

a = ()

Is a a tuple? Answer with Yes or No.

File: 20-answer.txt

## 21. Tuple or not?

a = (1, 2)

Is a a tuple? Answer with Yes or No.

File: 21-answer.txt

## 22. Tuple or not?

a = (1)

Is a a tuple? Answer with Yes or No.

File: 22-answer.txt

## 23. Tuple or not?

a = (1, )

Is a a tuple? Answer with Yes or No.

File: 23-answer.txt

## 24. Richard Sim's special #0

What does this script print?

a = (1)

b = (1)

a is b

File: 24-answer.txt

## 25. Richard Sim's special #1

What does this script print?

a = (1, 2)

b = (1, 2)

a is b

File: 25-answer.txt

## 26. Richard Sim's special #2

What does this script print?

a = ()

b = ()

a is b

File: 26-answer.txt

## 27. Richard Sim's special #3

>>> id(a)

139926795932424

>>> a

[1, 2, 3, 4]

>>> a = a + [5]

>>> id(a)

Will the last line of this script print 139926795932424? Answer with Yes or No.

File: 27-answer.txt

## 28. Richard Sim's special #4

>>> a

[1, 2, 3]

>>> id (a)

139926795932424

>>> a += [4]

>>> id(a)

Will the last line of this script print 139926795932424? Answer with Yes or No.

File: 28-answer.txt

## 29. Python3: Mutable, Immutable... everything is object!

Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

- Introduction

- id and type

- mutable objects

- immutable objects

- why does it matter and how differently does Python treat mutable and immutable objects

- how arguments are passed to functions and what does that imply for mutable and immutable objects

If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on Twitter and LinkedIn.

When done, please add all urls below (blog post, tweet, etc.)

## 30. Clear strings

guillaume@ubuntu:/python3$ cat string.py 

a = "HBTN"

b = "HBTN"

del a

del b

c = "HBTN"

guillaume@ubuntu:/python3$ 

Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many string objects are created by the execution of the first line of the script? (106-line1.txt)

How many string objects are created by the execution of the second line of the script (106-line2.txt)

After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)

After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)

How many string objects are created by the execution of the last line of the script (106-line5.txt)

File: 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt
