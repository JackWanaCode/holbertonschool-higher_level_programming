#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node: insert a node in sorted list
 * @head: head of linked list
 * @number: value of new node
 * Return: new node or NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = *head;
	listint_t *curr = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (curr)
	{
		prev = curr;
		curr = curr->next;
		if (curr && curr->n >= number)
		{
			if (prev == *head)
				*head = new;
			else
				prev->next = new;
			new->next = curr;
			return (new);
		}
	}
	if (prev->n < number)
	{
		prev->next = new;
		return (new);
	}
	return (NULL);
}
