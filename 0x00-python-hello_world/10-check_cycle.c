#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *after_p1 = list;
	/*by using The Tortoise and the Hare (Floyd’s Algorithm)*/

	if (list == NULL)
		return (0);
	while (after_p1 != NULL && after_p1->next != NULL)
	{
		p1 = p1->next;/*one step*/
		after_p1 = after_p1->next->next;/*two steps*/
		if (p1 == after_p1)
			/*if they catch so cycle is exist*/
			return (1);
	}
	return (0);
}
