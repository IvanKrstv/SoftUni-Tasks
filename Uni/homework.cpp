#include <iostream>
using namespace std;

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
	
	int left_num = 1;
	int right_num = size_matrix * size_matrix - size_matrix;

	for (int j = 0; j < size_matrix; j++)
	{
		for (int i = 0; i < size_matrix; i++)
		{
			if (i == j)
				matrix[i][j] = 0;
			else if (j < i)
			{
				matrix[i][j] = left_num;
				left_num++;
			}
			else if (j > i)
			{
				matrix[i][j] = right_num;
				right_num--;
			}
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