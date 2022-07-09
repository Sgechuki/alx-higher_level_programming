#include <Python.h>
void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to object
 *
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyVarObject *variable = (PyVarObject *) p;
	Py_ssize_t size, allocated, i = 0;
	const char *type;

	size = variable->ob_size;
	allocated = list->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for ( ; i < size; i++)
	{
		type = list->ob_item[0]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
