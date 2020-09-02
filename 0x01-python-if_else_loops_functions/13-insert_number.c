#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the linked list
 * @number: number to be added to the linked list
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *aux = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	aux = *head;
	if (aux->n > number)
	{
		new_node->next = aux;
		*head = new_node;
		return (new_node);
	}
	else
	{
		while (aux->next)
		{
			if (aux->n <= number && aux->next->n >= number)
			{
				new_node->next = aux->next;
				aux->next = new_node;
				return (new_node);
			}
			aux = aux->next;
		}
		aux->next = new_node;
	}
	return (new_node);
}
