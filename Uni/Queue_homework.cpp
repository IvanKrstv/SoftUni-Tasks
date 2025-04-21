#include <iostream>
using namespace std;

struct elem {
	int value;
	elem *next;
} *first = NULL, *last = NULL, *p = NULL;

void enque(int n)
{
	p = last;
	last = new elem;
	last->value = n;
	last->next = NULL;
	if (p != NULL)
		p->next = last;
	if (first == NULL)
		first = last;
}

void display_queue()
{
	elem* temp = first;
	cout << "\nQueue: ";
	while (temp != NULL)
	{
		cout << temp->value << " ";
		temp = temp->next;
	}
	cout << endl;
}

void remove_element(int n)
{
	if (first == NULL) 
	{
		cout << "Queue is empty." << endl;
		return;
	}

	elem* current = first;
	elem* previous = NULL;

	for (int i = 1; i < n; i++) 
	{
		previous = current;
		current = current->next;

		if (current == NULL) 
		{
			cout << "Position is greater than the queue size." << endl;
			return;
		}
	}

	if (previous == NULL) 
	{
		first = current->next;
		if (first == NULL)
			last = NULL; 
	}
	else 
	{
		previous->next = current->next;
		if (current == last)
			last = previous;
	}

	cout << "Removed element is " << current->value << endl;
	delete current;
}


int main()
{
	int num;
	cout << "Enter integers, type 0 to end" << endl;
	do
	{
		cout << "Enter number: "; cin >> num;
		if (num != 0)
			enque(num);
	} while (num != 0);

	if (first)
		display_queue();
	else
	{
		cout << "Empty queue" << endl;
		return 0;
	}

	int pos;
	cout << "Enter the position of the item to be removed: "; cin >> pos;

	remove_element(pos);

	display_queue();

	return 0;
}

// Задача 1.5. Да се състави програма за създаване на опашка и изключване от нея на N-я елемент от началото.