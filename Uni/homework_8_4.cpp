#include <iostream>
using namespace std;

int main()
{
	int x[20], y[20], uncommon_elements[20];
	int n, m, uncommon_elements_size = 0;

	cout << "How many numbers in array x? (Maximum size: 20)\nEnter size: ";
	cin >> n; 
	cout << "How many numbers in array y? (Maximum size: 20)\nEnter size: ";
	cin >> m;
	cout << endl;

	// Input
	for (int i = 0; i < n; i++)
	{
		cout << "Enter element " << i + 1 << " in x: ";
		cin >> x[i];
	}
	for (int i = 0; i < m; i++)
	{
		cout << "Enter element " << i + 1 << " in y: ";
		cin >> y[i];
	}

	for (int i = 0; i < n; i++)
	{
		bool in_y = false;
		for (int j = 0; j < m; j++)
		{
			if (x[i] == y[j])
			{
				in_y = true;
				break;
			}
		}
		if (!in_y)
		{
			uncommon_elements[uncommon_elements_size] = x[i];
			uncommon_elements_size++;
		}
	}
	
	if (uncommon_elements_size > 0)
	{
		int min_element = uncommon_elements[0];
		for (int i = 1; i < uncommon_elements_size; i++)
		{
			if (uncommon_elements[i] < min_element)
				min_element = uncommon_elements[i];
		}
		cout << "Min element in x, which is not in y is: " << min_element << endl;
	}
	else cout << "There are no elements in x that are not in y!" << endl;


	return 0;
}

// Zadacha 8. Da se sastavi programa, koyato sformira dva masiva - x[n] i y[m] i namira MIN element ot vsichki v x, koito ne se sadarzhat v y.