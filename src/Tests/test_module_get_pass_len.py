import unittest
from Modules import module_get_pass_len


class TestGetPassLen(unittest.TestCase):

    def test_values(self):
        self.assertRaises(ValueError, module_get_pass_len.get_password_length, -4)
        self.assertRaises(ValueError, module_get_pass_len.get_password_length, -5)
        self.assertRaises(ValueError, module_get_pass_len.get_password_length, -1)
        self.assertRaises(ValueError, module_get_pass_len.get_password_length, -7)

    def test_types(self):
        self.assertRaises(TypeError, module_get_pass_len.get_password_length, 5 + 2j)
        self.assertRaises(TypeError, module_get_pass_len.get_password_length, [10, 11])
        self.assertRaises(TypeError, module_get_pass_len.get_password_length, "lalala")


if __name__ == '__main__':
    unittest.main()
