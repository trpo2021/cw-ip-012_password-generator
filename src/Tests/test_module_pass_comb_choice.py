import unittest
from Modules import module_password_combination_choice


class TestPassCombChoice(unittest.TestCase):

    def test_types(self):
        self.assertRaises(TypeError, module_password_combination_choice.password_combination_choice, "lalala", "blabla", "tratata", "lololo")


if __name__ == '__main__':
    unittest.main()
