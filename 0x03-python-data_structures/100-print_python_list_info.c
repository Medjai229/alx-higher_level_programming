#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *obj;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
