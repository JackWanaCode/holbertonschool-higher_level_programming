#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_pal - check is palindrome array
 * @arr: pointer to array
 * @len: length of array
 * Return: 1 is palindrome, else 0
 */
int check_pal(char *arr, int len)
{
	int i, j;

	for (i = 0, j = len - 1; i < len / 2; i++, j--)
		if (arr[i] != arr[j])
			return (0);
	return (1);
}

/**
 * is_palindrome - check linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 is palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	int i, len, ret;
	char *arr;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (i = 0; curr; curr = curr->next, i++)
		;
	len = i;
	arr = malloc(sizeof(int) * len);
	for (i = 0, curr = *head; curr; curr = curr->next, i++)
	{
		arr[i] = curr->n;
	}
	ret = check_pal(arr, len);
	free(arr);
	return (ret);
}
