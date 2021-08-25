import unittest

from basic.weather_list import WeatherList


class WeatherListTest(unittest.TestCase):
    mock = WeatherList()
    def test_read_data(self):
        self.mock.read_data()

if __name__ == '__main__':
    unittest.main()