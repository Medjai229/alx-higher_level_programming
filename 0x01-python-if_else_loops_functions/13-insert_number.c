#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: value to be inserted
 *
 * Return: address of new node, if failed return null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *new = malloc(sizeof(listint_t));

	node = *head;

	if (!new)
		return (NULL);

	if (!(*head) || node->n >= number)
	{
		new->n = number;
		new->next = node;
		*head = new;
		return (new);
	}
	while (node)
	{
		if (node->n <= number && (!node->next || node->next->n > number))
		{
			new->n = number;
			new->next = node->next;
			node->next = new;
			return (new);
		}
		else
			node = node->next;
	}
	return (NULL);
}
