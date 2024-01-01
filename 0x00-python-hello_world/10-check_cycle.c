#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle or not
 * @list: pointer to the list to be checked
 *
 * Return: 1 if there is a cycle 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (1);
}
