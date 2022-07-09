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
	Py_ssize_t allocated, size, i = 0;
	const char *type;

	if (PyList_Check(p))
	{
		size = variable->ob_size;
		allocated = list->allocated;
		printf("[*] Size of the Python List = %li\n", size);
		printf("[*] Allocated = %li\n", allocated);
		for ( ; i < size; i++)
		{
			type = list->ob_item[i]->ob_type->tp_name;
			printf("Element %li: %s\n", i, type);
		}
	}
}
