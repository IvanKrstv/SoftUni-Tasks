#include <iostream>
using namespace std;

int main()
{
	int matrix[20][20];
	int size_matrix;

	cout << "What size would you like the matrix to be? (Maximum size: 20)\nEnter size: ";
	cin >> size_matrix;

	while (size_matrix < 1 || size_matrix > 20)
	{
		cout << "\nPlease enter a number between 1 and 20!\nEnter new number: ";
		cin >> size_matrix;
	}
	cout << endl;

	int current_number = size_matrix;

	for (int i = 0; i < size_matrix / 2; i++)
	{
		int changes = i; // number of changes of number in a row

		for (int j = 0; j < changes; j++)
		{
			matrix[i][j] = current_number;
			current_number--;
		}

		for (int j = changes; j < size_matrix - changes; j++)
			matrix[i][j] = current_number;

		for (int j = size_matrix - changes; j < size_matrix; j++)
		{
			current_number++;
			matrix[i][j] = current_number;
		}
	}

	for (int i = size_matrix / 2; i < size_matrix; i++)
	{
		int changes = size_matrix - i - 1;
		for (int j = 0; j < changes; j++)
		{
			matrix[i][j] = current_number;
			current_number--;
		}

		for (int j = changes; j < size_matrix - changes; j++)
			matrix[i][j] = current_number;

		for (int j = size_matrix - changes; j < size_matrix; j++)
		{
			current_number++;
			matrix[i][j] = current_number;
		}
	}

	// Output
	for (int i = 0; i < size_matrix; i++)
	{
		for (int j = 0; j < size_matrix; j++)
			cout << matrix[i][j] << "\t";
		cout << endl;
	}

	return 0;
}