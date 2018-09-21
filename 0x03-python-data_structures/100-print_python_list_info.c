#include <stdio.h>
#include <Python.h>
#include <string.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	unsigned long list_size = PyList_Size(p);
	unsigned long i = 0;
	const char *type;

	printf("[*] Size of the Python List = %lu\n", list_size);
	printf("[*] Allocated = %lu\n", ((PyObject *)p)->alocated);
	while (i < list_size)
	{
		type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
 		printf("Element %lu: %s\n", i, type);
		i++;
	}
}
