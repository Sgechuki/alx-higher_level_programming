#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks cycle
 * @list: singly linked list
 * Desc: function in C that checks if a
 * singly linked list has a cycle in it
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
