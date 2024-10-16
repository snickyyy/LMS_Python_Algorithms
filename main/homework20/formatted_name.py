import unittest


def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()


class TestNameFormater(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(formatted_name('john', 'doe'), 'John Doe')
        self.assertEqual(formatted_name("walter", "white", "||"), 'Walter || White')

    def test_type_raises(self):
        self.assertRaises(TypeError, formatted_name, 'john', 123)
        self.assertRaises(TypeError, formatted_name, 123, 'doe')
        self.assertRaises(TypeError, formatted_name, 'john', 'doe', 123)

    def test_dont_correct_values(self):
        self.assertEqual(formatted_name('jOhn', 'dOE', 'sMiTh'), 'John Smith Doe')
        self.assertEqual(formatted_name('   john   ', '   doe   '), 'John Doe')
        self.assertEqual(formatted_name('j', 'd', 's'), 'J S D')

def main():
    unittest.main()


if __name__ == "__main__":
    main()
