from unittest import TestCase, main
from project.legendary_item import LegendaryItem

class LegendaryItemTests(TestCase):
    def test_special_symbols_in_identifier_raises(self):
        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("%test", 1, 50, 20)
        self.assertEqual("Identifier can only contain letters, digits, or hyphens!", str(ex.exception))

    def test_identifier_less_than_4_chars_raises(self):
        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("asd", 1, 50, 20)
        self.assertEqual("Identifier must be at least 4 characters long!", str(ex.exception))

    def test_power_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("test", -1, 50, 20)
        self.assertEqual("Power must be a non-negative integer!", str(ex.exception))

    def test_durability_less_than_1_or_more_than_100_raises(self):
        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("test", 1, 0, 20)
        self.assertEqual("Durability must be between 1 and 100 inclusive!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("test", 1, 101, 20)
        self.assertEqual("Durability must be between 1 and 100 inclusive!", str(ex.exception))

    def test_price_equal_to_zero_or_not_multiple_to_10_raises(self):
        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("test", 1, 50, 0)
        self.assertEqual("Price must be a multiple of 10 and not 0!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            item = LegendaryItem("test", 1, 50, 7)
        self.assertEqual("Price must be a multiple of 10 and not 0!", str(ex.exception))

    def test_is_precious_false(self):
        item = LegendaryItem("test", 1, 50, 20)
        self.assertFalse(item.is_precious)

    def test_is_precious_true(self):
        item = LegendaryItem("test", 50, 50, 20)
        self.assertTrue(item.is_precious)

        item.power += 1
        self.assertEqual(51, item.power)
        self.assertTrue(item.is_precious)

    def test_init(self):
        item = LegendaryItem("test", 50, 50, 20)

        self.assertEqual("test", item.identifier)
        self.assertEqual(50, item.power)
        self.assertEqual(50, item.durability)
        self.assertEqual(20, item.price)
        self.assertTrue(item.is_precious)

    def test_enhance_durability_less_than_100(self):
        item = LegendaryItem("test", 10, 50, 20)

        item.enhance()

        self.assertEqual(20, item.power)
        self.assertEqual(60, item.durability)
        self.assertEqual(30, item.price)

    def test_enhance_durability_more_than_100(self):
        item = LegendaryItem("test", 10, 95, 20)

        item.enhance()

        self.assertEqual(20, item.power)
        self.assertEqual(100, item.durability)
        self.assertEqual(30, item.price)

    def test_evaluate_durability_less_than_min_durability(self):
        item = LegendaryItem("test", 60, 20, 20)

        result = item.evaluate(30)
        self.assertEqual("Item not eligible.", result)

    def test_evaluate_is_precious_is_false(self):
        item = LegendaryItem("test", 10, 20, 20)

        result = item.evaluate(10)
        self.assertEqual("Item not eligible.", result)

    def test_evaluate_both_cases_true(self):
        item = LegendaryItem("test", 60, 20, 20)

        result = item.evaluate(10)
        self.assertEqual("test is eligible.", result)

if __name__ == '__main__':
    main()