#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 is palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head;
	listint_t *bf_last = NULL;

	if (!(*head))
		return (1);
	while (last->next)
	{
		bf_last = last;
		last = last->next;
	}
	if (*head == last || *head == bf_last)
		return (1);
	else if ((*head)->n != last->n)
		return (0);
	bf_last->next = NULL;
	return (is_palindrome(&(*head)->next));
}
