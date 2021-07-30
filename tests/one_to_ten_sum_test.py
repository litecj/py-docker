import unittest

from basic.one_to_ten_sum import OneToTenSum


class OneToTenSumTest(unittest.TestCase):
    mock = OneToTenSum()
    def test_one_to_ten_sum(self):
        self.mock.one_to_ten_sum()

    def test_one_to_ten_sum_2(self):
        self.mock.one_to_ten_sum_2()

if __name__ == '__main__':
    unittest.main()