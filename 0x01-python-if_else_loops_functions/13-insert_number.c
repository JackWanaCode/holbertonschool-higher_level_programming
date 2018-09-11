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
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
	}
	while (curr)
	{
		if (curr && curr->n > number)
		{
			if (prev == NULL)
				*head = new;
			else
				prev->next = new;
			new->next = curr;
			break;
		}
		else if (curr->n == number)
			return (NULL);
		prev = curr;
                curr = curr->next;
	}
	if (prev && prev->n < number)
	{
		prev->next = new;
	}
	return (new);
}
