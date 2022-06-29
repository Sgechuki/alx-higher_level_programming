#include "lists.h"

/**
 * check_cycle - function in C that checks if a
 * singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (slow->next != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	free(slow);
	free(fast);
	return (0);
}
