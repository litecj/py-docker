import unittest

from basic.weather import Weather


class WeatherTest(unittest.TestCase):
    mock = Weather()
    def test_read_data(self):
        self.mock.read_data()

    def test_data_merge(self):
        self.mock.data_merge()


if __name__ == '__main__':
    unittest.main()