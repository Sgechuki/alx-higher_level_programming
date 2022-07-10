#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic contents of a list
 * @p: pointer to object
 *
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyVarObject *var = (PyVarObject *) p;
	Py_ssize_t alloc, size, i;
	const char *type;

	if (PyList_Check(p))
	{
		alloc = list->allocated;
		size = var->ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %li\n", size);
		printf("[*] Allocated = %li\n", alloc);
		for (i = 0; i < size; i++)
		{
			type = list->ob_item[i]->ob_type->tp_name;
			printf("Element %li: %s\n", i, type);
			if (PyBytes_Check(list->ob_item[i]))
			{
				print_python_bytes(list->ob_item[i]);
			}
		}
	}
}

/**
 * print_python_bytes - print some basic info about
 * Python bytes objects
 * @p: pointer to object
 *
 */
void print_python_bytes(PyObject *p)
{
	char *string = NULL;
	Py_ssize_t size, i;

	if (PyBytes_Check(p))
	{
		PyBytes_AsStringAndSize(p, &string, &size);
		printf("[.] bytes object info\n");
		printf("  size: %li\n", size);
		printf("  trying string: %s\n", string);
		if (size < 10)
		{
			printf("  first %li bytes:", size + 1);
		}
		else
		{
			printf("  first 10 bytes:");
		}
		for (i = 0; i <= size && i < 10; i++)
		{
			printf(" %02hhx", string[i]);
		}
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

