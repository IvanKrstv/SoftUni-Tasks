from project2.furniture import Furniture
from unittest import TestCase, main

class FurnitureTests(TestCase):
    def test_model_empty_string_or_more_than_50_chars_raises(self):
        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("", 10.0, (1, 1, 1))
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("a" * 51, 10.0, (1, 1, 1))
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_price_negative_number_raises(self):
        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("test", -1, (1, 1, 1))
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_dimensions_not_3_or_dimension_less_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("test", 10.0, (1, 1))
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("test", 10.0, (0, 1, 1))
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("test", 10.0, (-1, 1, 1))
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_weight_is_not_none_and_is_less_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("test", 10.0, (1, 1, 1), weight=0)
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            furniture = Furniture("test", 10.0, (1, 1, 1), weight=-1)
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_init(self):
        furniture = Furniture("test", 10.0, (1, 1, 1))
        self.assertEqual('test', furniture.model)
        self.assertEqual(10.0, furniture.price)
        self.assertEqual((1, 1, 1), furniture.dimensions)
        self.assertTrue(furniture.in_stock)
        self.assertIsNone(furniture.weight)

        furniture = Furniture("test", 10.0, (1, 1, 1), in_stock=False)
        self.assertEqual('test', furniture.model)
        self.assertEqual(10.0, furniture.price)
        self.assertEqual((1, 1, 1), furniture.dimensions)
        self.assertFalse(furniture.in_stock)
        self.assertIsNone(furniture.weight)

        furniture = Furniture("test", 10.0, (1, 1, 1), weight=5)
        self.assertEqual('test', furniture.model)
        self.assertEqual(10.0, furniture.price)
        self.assertEqual((1, 1, 1), furniture.dimensions)
        self.assertTrue(furniture.in_stock)
        self.assertEqual(5, furniture.weight)

    def test_get_available_status(self):
        furniture = Furniture("test", 10.0, (1, 1, 1), in_stock=False)
        result = furniture.get_available_status()
        self.assertEqual(f"Model: test is currently unavailable.", result)

        furniture = Furniture("test", 10.0, (1, 1, 1))
        result = furniture.get_available_status()
        self.assertEqual(f"Model: test is currently in stock.", result)

    def test_get_specifications(self):
        furniture = Furniture("test", 10.0, (1, 1, 1))
        result = furniture.get_specifications()
        self.assertEqual(f"Model: test has the following dimensions: 1mm x 1mm x 1mm and weighs: N/A", result)

        furniture = Furniture("test", 10.0, (1, 1, 1), weight=5)
        result = furniture.get_specifications()
        self.assertEqual(f"Model: test has the following dimensions: 1mm x 1mm x 1mm and weighs: 5", result)

if __name__ == '__main__':
    main()