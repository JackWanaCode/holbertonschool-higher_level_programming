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
	listint_t *curr = *head;
	listint_t *curr2 = NULL;
	listint_t *head2 = *head;
	listint_t *next_curr2 = *head;
	int check = 0, i = 0, len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (i = 0; head2->next; head2 = head2->next, i++)
		;
	len = i;

	for (i = 0; i < len; i++)
	{
		if (check == 0)
		{
			curr2 = next_curr2;
			next_curr2 = next_curr2->next;
		}
		if (i == len / 2 + 1)
		{
			head2 = curr2->next;
			curr2->next = NULL;
			check = 1;
		}
		else if (check == 1)
		{
			next_curr2 = next_curr2->next;
			head2->next = curr2;
			curr2 = head2;
			head2 = next_curr2;
		}
	}
	next_curr2->next = curr2;
	while (next_curr2)
	{
		if (curr->n != next_curr2->n)
			return (0);
		curr = curr->next;
		next_curr2 = next_curr2->next;
	}
	return (1);

}
