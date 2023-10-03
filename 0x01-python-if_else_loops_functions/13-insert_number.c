#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of linked list
 * @number: number to insert
 * Return: pointer to head of linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp1, *temp2;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return (NULL);
	}
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	temp1 = *head;
	if ((temp1->n) > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (temp1->next != NULL)
	{
		temp2 = temp1;
		temp1 = temp1->next;
		if (temp1->n > number)
		{
			temp2->next = node;
			node->next = temp1;
			return (node);
		}
	}
	if (temp1->next == NULL)
	{
		temp1->next = node;
		return (node);
	}
	return (NULL);
}

