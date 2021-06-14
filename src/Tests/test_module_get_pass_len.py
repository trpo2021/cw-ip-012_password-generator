import unittest
from src.Modules import module_get_pass_len
import get_password_length

class TestGetPassLen(unittest.TestCase):

    def test_values(self):
        self.assertRaises(ValueError, get_password_length, -4)
        self.assertRaises(ValueError, get_password_length, -5)
        self.assertRaises(ValueError, get_password_length, -1)
        self.assertRaises(ValueError, get_password_length, -7)

    def test_types(self):
        self.assertRaises(TypeError, get_password_length, 5+2j)

if __name__ == '__main__':
    unittest.main()