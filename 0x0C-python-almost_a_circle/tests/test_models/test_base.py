import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_string_id(self):
        with self.assertRaises(TypeError):
            b = Base("string_id")


if __name__ == '__main__':
    unittest.main()

