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
	listint_t *af_last = NULL;
	listint_t *curr = *head;
	listint_t *last = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		while (last->next != af_last)
			last = last->next;
		if (curr->n != last->n)
			return (0);
		if (curr == last || curr->next == last)
			return (1);
		curr = curr->next;
		af_last = last;
		last = curr;
	}
}
