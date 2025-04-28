#include <iostream>
using namespace std;

struct elem {
	int key;
	elem* next;
}*leftt = NULL, *rightt = NULL;

void push_l(int n)
{
    elem* p;
    p = leftt;
    leftt = new elem;
    leftt->key = n;
    leftt->next = p;
    if (rightt == NULL)
    { 
        rightt = leftt;
    }
}
void push_r(int n)
{
    elem* p;
    p = rightt;
    rightt = new elem;
    rightt->key = n;
    rightt->next = NULL;
    if (leftt == NULL)	
        leftt = rightt;
    else
        p->next = rightt;
}

int pop_l(int& n)
{
    elem* p;
    if (leftt)
    {
        n = leftt->key;
        p = leftt;
        leftt = leftt->next;
        if (leftt == NULL)
            rightt = NULL;
        delete p;
        return 1;
    } 
    else
        return 0;
}
int pop_r(int& n)
{
    elem* p;
    if (rightt)
    {
        n = rightt->key;
        if (leftt == rightt) 
        {
            delete rightt;
            leftt = rightt = NULL;
        }
        else
        {
            p = leftt;
            while (p->next != rightt)
                p = p->next;
            p->next = NULL;
            delete rightt;
            rightt = p;
        }
        return 1;
    } 
    else
        return 0;
}

void print_deck(elem* left)
{
    elem* temp = left;
    cout << "Deck: ";
    while (temp != NULL)
    {
        cout << temp->key << " ";
        temp = temp->next;
    }
    cout << endl;
}

int search(elem* left, int searched_element)
{
    elem* temp = left;
    int counter = 1;
    while (temp != NULL)
    {
        if (temp->key == searched_element)
            return counter;
        temp = temp->next;
        counter++;
    }

    return 0;
}

int main()
{
    int num;
    cout << "Enter numbers for the deck, 0 for end" << endl;
    do 
    {
        cout << "Enter number: "; cin >> num;
        if (num != 0)
            push_r(num);
    } while (num != 0);

    print_deck(leftt);

    int element;
    cout << "Enter number to be searched: "; cin >> element;
    int position = search(leftt, element); 

    if (position == 0)
        cout << "The number is not in the deck." << endl;
    else
        cout << "The number is on position " << position << endl;

    return 0;
}

// Задача 2.3. Да се състави функция за търсене на елемент в зададен дек.