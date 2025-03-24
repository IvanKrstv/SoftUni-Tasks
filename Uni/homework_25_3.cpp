#include <iostream>
using namespace std;

int min_number(int matrix[20][20], int size, int i);
int max_number(int matrix[20][20], int size, int i);


int main()
{
	int matrix[20][20];
	int size_matrix;

	// Input
	cout << "What size would you like the matrix to be? (Maximum size: 20)\nEnter size: ";
	cin >> size_matrix;
	while (size_matrix < 1 || size_matrix > 20)
	{
		cout << "\nPlease enter a number between 1 and 20!\nEnter new number: ";
		cin >> size_matrix;
	}
	cout << endl;
	for (int i = 0; i < size_matrix; i++)
	{
		for (int j = 0; j < size_matrix; j++)
		{
			cout << "Enter element [" << i << "][" << j << "]: "; cin >> matrix[i][j];
		}
	}
	cout << endl;

	// Output
	for (int i = 0; i < size_matrix; i++)
	{
		for (int j = 0; j < size_matrix; j++)
			cout << matrix[i][j] << "\t";
		cout << endl;
	}
	cout << endl;

	for (int i = 0; i < size_matrix; i++)
	{
		cout << "Min element in row " << i + 1 << ": " << min_number(matrix, size_matrix, i) << endl;
		cout << "Max element in row " << i + 1 << ": " << max_number(matrix, size_matrix, i) << endl;
	}

	return 0;
}

int min_number(int matrix[20][20], int size, int i)
{
	int min_number = matrix[i][0];
	for (int j = 1; j < size; j++)
	{
		if (matrix[i][j] < min_number)
			min_number = matrix[i][j];
	}

	return min_number;
}

int max_number(int matrix[20][20], int size, int i)
{
	int max_number = matrix[i][0];
	for (int j = 1; j < size; j++)
	{
		if (matrix[i][j] > max_number)
			max_number = matrix[i][j];
	}

	return max_number;
}

// Zadacha 3.
// Da se napishe funktsiya, koyato formira matrica X(n, m) s razlichni po stoynost tseli chisla.
// Da se nameryat nay - malkiya element za vseki red i nay - golemiya ot tyah.