from unittest import TestCase, main
from custom_list import CustomList


class CustomListTests(TestCase):
    def setUp(self):
        pass

    def test_init_no_params(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

    def test_init_with_params(self):
        cl = CustomList(4, 'asd', 9.8)
        self.assertEqual([4, 'asd', 9.8], cl._CustomList__data)

    def test_append_no_args(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

        result = cl.append(5)
        self.assertEqual([5], cl._CustomList__data)
        self.assertEqual([5], result)

    def test_append_with_existing_values(self):
        cl = CustomList(4, 'asd', 9.8)
        self.assertEqual([4, 'asd', 9.8], cl._CustomList__data)

        result = cl.append(5)
        self.assertEqual([4, 'asd', 9.8, 5], cl._CustomList__data)
        self.assertEqual([4, 'asd', 9.8, 5], result)

    def test_remove_by_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.remove(0)
        self.assertEqual([10, 5], cl._CustomList__data)
        self.assertEqual(5, result)

    def test_remove_invalid_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        with self.assertRaises(IndexError) as ex:
            result = cl.remove(4)
        self.assertEqual(f"Index must be between 0 and 2", str(ex.exception))
        self.assertEqual([5, 10, 5], cl._CustomList__data)

    def test_get_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.get(0)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(5, result)

    def test_extend(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.extend([1, 2, 3 ])
        self.assertEqual([5, 10, 5, 1, 2, 3], cl._CustomList__data)
        self.assertEqual([5, 10, 5, 1, 2, 3], result)

    def test_extend_on_empty_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

        result = cl.extend([1, 2, 3])
        self.assertEqual([1, 2, 3], cl._CustomList__data)
        self.assertEqual([1, 2, 3], result)

    def test_insert_invalid_index(self):
        cl = CustomList(5, 6, 5)

        with self.assertRaises(IndexError) as ex:
            cl.insert(-1, 100)
        self.assertEqual([5, 6, 5], cl._CustomList__data)
        self.assertEqual("Index must be between 0 and 2", str(ex.exception))


    def test_insert_in_front(self):
        cl = CustomList(5, 6, 5)
        self.assertEqual([5, 6, 5], cl._CustomList__data)

        cl.insert(0, 100)
        self.assertEqual([100, 5, 6, 5], cl._CustomList__data)

    def test_insert_in_the_middle(self):
        cl = CustomList(5, 6, 5)
        self.assertEqual([5, 6, 5], cl._CustomList__data)

        cl.insert(2, 100)
        self.assertEqual([5, 6, 100, 5], cl._CustomList__data)

    def test_pop(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.pop()
        self.assertEqual([5, 10], cl._CustomList__data)
        self.assertEqual(5, result)

    def test_clear(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.clear()
        self.assertEqual([], cl._CustomList__data)
        self.assertIsNone(result)

    def test_index_value_does_not_exist(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.index(100)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(-1, result)

    def test_index_return_first_occurence(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.index(5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(0, result)

    def test_count_no_values(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.count(100)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(0, result)

    def test_count(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.count(5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(2, result)

    def test_reverse(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.reverse()
        self.assertEqual([1, 10, 5], cl._CustomList__data)
        self.assertEqual([5, 10, 1], result)

    def test_copy(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.copy()

        self.assertEqual([1, 10, 5], cl._CustomList__data)
        self.assertEqual([1, 10, 5], result)
        self.assertNotEqual(id(cl._CustomList__data), id(result))

    def test_nested_objects_are_copied_too(self):
        cl = CustomList([1, 2], 3, 4)
        self.assertEqual([[1, 2], 3, 4], cl._CustomList__data)

        result = cl.copy()

        self.assertNotEqual(id(cl._CustomList__data), id(result))
        self.assertNotEqual(id(cl._CustomList__data[0]), id(result[0]))
        self.assertEqual([1, 2], cl._CustomList__data[0])

    def test_size(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

        result = cl.size()
        self.assertEqual([], cl._CustomList__data)
        self.assertEqual(0, result)

        cl.append(10)
        cl.append(20)

        result = cl.size()
        self.assertEqual([10, 20], cl._CustomList__data)
        self.assertEqual(2, result)

    def test_add_first(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.add_first(100)
        self.assertEqual([100, 1, 10, 5], cl._CustomList__data)
        self.assertIsNone(result)

    def test_dictionize_odd_values(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.dictionize()
        self.assertEqual([1, 10, 5], cl._CustomList__data)
        self.assertEqual({1: 10, 5: " "}, result)

    def test_dictionize_even_values(self):
        cl = CustomList(1, 10, 5, 6)
        self.assertEqual([1, 10, 5, 6], cl._CustomList__data)

        result = cl.dictionize()
        self.assertEqual([1, 10, 5, 6], cl._CustomList__data)
        self.assertEqual({1: 10, 5: 6}, result)

    def test_dictionaze_no_values(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)
        result = cl.dictionize()
        self.assertEqual([], cl._CustomList__data)
        self.assertEqual({}, result)

    def test_move(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.move(2)

        self.assertEqual([5, 1, 10], cl._CustomList__data)
        self.assertEqual([5, 1, 10], result)


if __name__ == '__main__':
    main()