import unittest

from basic.menu_lunch import MenuLunch


class MenuLunchTest (unittest.TestCase):
    mock = MenuLunch()
    def test_menu_lunch(self):
        self.mock.menu_lunch()


if __name__ == '__main__':
    unittest.main