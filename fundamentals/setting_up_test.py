import unittest

def get_formatted_name(first, last):
    fullname = f"{first} {last}"
    return fullname.title()

class NamesTestCase(unittest.TestCase):
    """Tests for 'get_formatted_name function'"""

    def test_first_last_name(self):
        """Do names like 'Le Ngoc Dan' work?"""
        formatted_name = get_formatted_name("Le Ngoc", "Dan")
        self.assertEqual(formatted_name, 'Le Ngoc Dan')

if __name__ == "__main__":
    unittest.main()
