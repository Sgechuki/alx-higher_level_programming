#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly
 * linked list is a palindrome
 * @head: pointer to head node
 * Return: 1 if True 0 if False
 */
int is_palindrome(listint_t **head)
{
	listint_t *bonet = NULL, *boot = NULL;
	int x = 0, len = 0, y = 0;

	if (!head)
		return (0);
	bonet = *head;
	for (len = 0; bonet != NULL; len++)
	{
		bonet = bonet->next;
	}
	if (len == 1 || !(*head))
		return (1);
	for (x = 0; x < (len / 2); x++)
	{
		bonet = *head;
		boot = *head;
		for (y = 0; y < x; y++)
		{
			bonet = bonet->next;
		}
		for (y = 0; y < (len - (x + 1)); y++)
		{
			boot = boot->next;
		}
		if (boot->n != bonet->n)
		{
			return (0);
		}
	}
	return (1);
}
