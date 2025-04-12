#include <iostream>
using namespace std;

struct elem {
    int value;
    elem* next;
}*start_main = NULL, *start_positives = NULL, *start_negatives = NULL;

void push(elem*& start, int n) 
{
    elem* p = new elem;
    p->value = n;
    p->next = start;
    start = p;
}

void display(elem* start) 
{
    if (start != NULL) 
    {
        elem* temp = start;
        while (temp != NULL) 
        {
            cout << temp->value << "\t";
            temp = temp->next;
        }
        cout << endl;
    }
    else
        cout << "Empty stack" << endl;
}

int main()
{
    int size_stack;
    cout << "Enter size of stack: ";
    cin >> size_stack;

    for (int i = 0; i < size_stack; i++)
    {
        int current_element;
        cout << "Enter element No. " << i + 1 << ": ";
        cin >> current_element;
        push(start_main, current_element);

        if (current_element > 0)
            push(start_positives, current_element);
        else if (current_element < 0)
            push(start_negatives, current_element);
    }
    
    cout << "\nMain stack: "; display(start_main);
    cout << "Positives stack: "; display(start_positives);
    cout << "Negatives stack: "; display(start_negatives);

    return 0;
}

// Zadacha 5: Da se sastavi programma, koqto suzdava dinamichen stack S s celi chisla i sled tova go preobrazuva v dva drugi stacka – P i Q,
// koito sadurzhat suotvetno polozhitelni i otricatelnite elementi na S. Sudurjanieto na trite stacka da se izvede na ekran.