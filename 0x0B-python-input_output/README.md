# 0x0B. Python - Input/Output

## Target

- How to open a file

- How to write text in a file

- How to read the full content of a file

- How to read a file line by line

- How to move the cursor in a file

- How to make sure a file is closed after using it

- What is and how to use the with statement

- What is JSON

- What is serialization

- What is deserialization

- How to convert a Python data structure to a JSON string

- How to convert a JSON string to a Python data structure

## Task

### 0. Read file

Write a function that reads a text file (UTF8) and prints it to stdout:

- Prototype: def read_file(filename=""):

- You must use the with statement

- You don’t need to manage file permission/file doesn’t exist exceptions.

- You are not allowed to import any module

File: 0-read_file.py

### 1. Number of lines

Write a function that returns the number of lines of a text file:

- Prototype: def number_of_lines(filename=""):

- You must use the with statement

- You don’t need to manage file permission/file doesn’t exist exceptions.

- You are not allowed to import any module

File: 1-number_of_lines.py

### 2. Read n lines

Write a function that reads n lines of a text file (UTF8) and prints it to stdout:

- Prototype: def read_lines(filename="", nb_lines=0):

- Read the entire file if nb_lines is lower or equal to 0 OR greater or equal to the total number of lines of the file

- You must use the with statement

- You don’t need to manage file permission/file doesn’t exist exceptions.

- You are not allowed to import any module

File: 2-read_lines.py

### 3. Write to a file

Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

- Prototype: def write_file(filename="", text=""):

- You must use the with statement

- You don’t need to manage file permission exceptions.

- You are not allowed to import any module

File: 3-write_file.py

### 4. Append to a file


Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

- Prototype: def append_write(filename="", text=""):

- If the file doesn’t exist, it should be created

- You must use the with statement

- You don’t need to manage file permission/file doesn’t exist exceptions.

- You are not allowed to import any module

File: 4-append_write.py

### 5. To JSON string

Write a function that returns the JSON representation of an object (string):

- Prototype: def to_json_string(my_obj):

- You don’t need to manage exceptions if the object can’t be serialized.

File: 5-to_json_string.py

### 6. From JSON string to Object

Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: def from_json_string(my_str):

- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

File: 6-from_json_string.py

### 7. Save Object to a file

Write a function that writes an Object to a text file, using a JSON representation:

- Prototype: def save_to_json_file(my_obj, filename):

- You must use the with statement

- You don’t need to manage exceptions if the object can’t be serialized.

- You don’t need to manage file permission exceptions.

File: 7-save_to_json_file.py

### 8. Create object from a JSON file

Write a function that creates an Object from a “JSON file”:

- Prototype: def load_from_json_file(filename):

- You must use the with statement

- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

- You don’t need to manage file permissions / exceptions.

File: 8-load_from_json_file.py

9. Load, add, save

Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function save_to_json_file from 7-save_to_json_file.py

- You must use your function load_from_json_file from 8-load_from_json_file.py

- The list must be saved as a JSON representation in a file named add_item.json

- If the file doesn’t exist, it should be created

- You don’t need to manage file permissions / exceptions.

File: 9-add_item.py

### 10. Class to JSON

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: def class_to_json(obj):

- obj is an instance of a Class

- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean

- You are not allowed to import any module

File: 10-class_to_json.py

### 11. Student to JSON

Write a class Student that defines a student by:

- Public instance attributes:

  - first_name

  - last_name

  - age

- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):

- Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)

- You are not allowed to import any module

File: 11-student.py

### 12. Student to JSON with filter

Write a class Student that defines a student by: (based on 11-student.py)

- Public instance attributes:

  - first_name

  - last_name

  - age

- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):

- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):

  - If attrs is a list of strings, only attributes name contain in this list must be retrieved.

  - Otherwise, all attributes must be retrieved

 - You are not allowed to import any module

File: 12-student.py

### 13. Student to disk and reload

Write a class Student that defines a student by: (based on 12-student.py)

- Public instance attributes:

  - first_name

  - last_name

  - age

- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):

- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):

  - If attrs is a list of strings, only attributes name contain in this list must be retrieved.

  - Otherwise, all attributes must be retrieved

- Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:

  - You can assume json will always be a dictionary

  - A dictionary key will be the public attribute name

  - A dictionary value will be the value of the public attribute

- You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

File: 13-student.py

### 14. Pascal's Triangle

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0

- You can assume n will be always an integer

File 14-pascal_triangle.py

### 15. Search and update

Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

- Prototype: def append_after(filename="", search_string="", new_string=""):

- You must use the with statement

- You don’t need to manage file permission/file doesn’t exist exceptions.

- You are not allowed to import any module

File: 100-append_after.py

### 16. Log parsing

Write a script that reads stdin line by line and computes metrics:

- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

- Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:

  - Total file size: File size: <total size>

  - where is the sum of all previous (see input format above)

  - Number of lines by status code:

    - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

    - if a status code doesn’t appear, don’t print anything for this status code

    - format: <status code>: <number>

    - status codes should be printed in ascending order

File: 101-stats.py

### 17. Hack the VM


Write a script that finds a string in the heap of a running process, and replaces it.

- Read The /proc filesystem

- Usage: read_write_heap.py pid search_string replace_string

  - where pid is the pid of the running process

  - and strings are ASCII

- The script should look only in the heap of the process

- Output: you can print whatever you think is interesting

- On usage error, print an error message on stdout and exit with status code 1

File: read_write_heap.py