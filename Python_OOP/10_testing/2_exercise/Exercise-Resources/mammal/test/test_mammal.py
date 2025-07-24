from unittest import TestCase, main
from project.mammal import Mammal

class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("test_name", "test_type", "test_sound")

    def test_init(self):
        self.assertEqual("test_name", self.mammal.name)
        self.assertEqual("test_type", self.mammal.type)
        self.assertEqual("test_sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"test_name makes test_sound", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"test_name is of type test_type", self.mammal.info())


if __name__ == '__main__':
    main()