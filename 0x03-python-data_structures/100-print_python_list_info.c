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
	Py_ssize_t allocated, i = 0;
	const char *type;

	if (PyList_Check(p))
	{
		allocated = list->allocated;
		printf("[*] Size of the Python List = %li\n", PyList_Size(p));
		printf("[*] Allocated = %li\n", allocated);
		for ( ; i < PyList_Size(p); i++)
		{
			type = list->ob_item[0]->ob_type->tp_name;
			printf("Element %li: %s\n", i, type);
		}
	}
}
