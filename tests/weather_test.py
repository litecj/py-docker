import unittest

from basic.weather import Weather


class WeatherTest(unittest.TestCase):
    mock = Weather()
    def test_read_data(self):
        self.mock.read_data()

    # def test_data_merge(self):
    #     self.mock.data_merge()

    # def test_drop_feature(self):
    #     self.mock.drop_feature(self,'day','hour')
        print('*' * 100)
        print(f'1-1.Type is{type(self.mock.df)}')
        print(f'2-1.Columns is{self.mock.df}')
        print(f'3-1.Top Row is{self.mock.df.head(3)}')
        print(f'4-1.Null Count is{self.mock.df.isnull().sum()}')


if __name__ == '__main__':
    unittest.main()