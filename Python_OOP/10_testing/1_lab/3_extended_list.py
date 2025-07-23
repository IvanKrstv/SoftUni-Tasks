class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main

class IntegerListTests(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(4, 3, 6)

    def test_init_only_integers(self):
        integer_list = IntegerList('5', 5, 3.7, 6, False)

        self.assertEqual(integer_list.get_data(), [5, 6])

    def test_add_element_not_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add('5')
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_integer(self):
        self.integer_list.add(8)

        self.assertEqual([4, 3, 6, 8], self.integer_list.get_data())

    def test_remove_index_out_of_range_raises(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

    def test_remove_index(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        removed_item = self.integer_list.remove_index(1)

        self.assertEqual(self.integer_list.get_data(), [4, 6])
        self.assertEqual(3, removed_item)

    def test_get_out_of_range_raises(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

    def test_get(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        item = self.integer_list.get(0)

        self.assertEqual(4, item)

    def test_insert_out_of_range_raises(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(4, 9)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(3, 9)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

    def test_insert_element_not_integer_raises(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, '5')
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, 5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

    def test_insert(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        self.integer_list.insert(1, 2)

        self.assertEqual(self.integer_list.get_data(), [4, 2, 3, 6])

    def test_get_biggest(self):
        integer_list = IntegerList(4, 2, -1, 10, 5, 7)

        biggest_element = integer_list.get_biggest()

        self.assertEqual(10, biggest_element)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_data(), [4, 3, 6])

        index = self.integer_list.get_index(6)

        self.assertEqual(2, index)

if __name__ == '__main__':
    main()