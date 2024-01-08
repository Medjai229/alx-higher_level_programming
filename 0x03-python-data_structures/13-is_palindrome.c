#include "lists.h"

/**
 * aux_palind - funct to know if it is palindrome
 * @head: head list
 * @end: end list
 *
 * Return: 0 if it is not palindrome 1 if it is
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head list
 *
 * Return: 0 if it is not palindrome 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

