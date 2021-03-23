import unittest
from full_name import full_name

class NameTestCase(unittest.TestCase):
    """Тесты для функции full_name"""

    def test_first_last_name(self):
        """Имена вида 'Shalimov Denis' работает нормально?"""
        format_name = full_name('Shalimov', 'Denis')
        self.assertEqual(format_name, 'Shalimov Denis')

    def test_first_last_middle(self):
        """Имена вида 'Shalimov Denis Valentinovich' работает нормально?"""
        format_name = full_name('Shalimov', 'Denis',  'Valentinovich')
        self.assertEqual(format_name, 'Shalimov Denis Valentinovich')


if __name__ == "__name__":
    unittest.main()