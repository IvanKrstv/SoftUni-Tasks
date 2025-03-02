#include <iostream>
using namespace std;

int main()
{
	int matrix[20][20];
	int size_matrix;

	cout << "What size would you like the matrix to be? (Maximum size: 20)\nEnter size: ";
	cin >> size_matrix;

	while (!cin || (size_matrix < 1 || size_matrix > 20))
	{
		if (!cin)
		{
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
		}
		cout << "\nPlease enter a number between 1 and 20!\nEnter new number: ";
		cin >> size_matrix;
	}

	cout << endl;

	for (int i = 0; i < size_matrix; i++)
	{
		for (int j = 0; j < i; j++)
			cout << 0 << "\t";

		for (int j = i; j < size_matrix; j++)
			cout << size_matrix - i << "\t";

		cout << endl;
	}
	return 0;
}
