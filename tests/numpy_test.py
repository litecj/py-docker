import unittest

from basic.numpy_lib import Numpy


class NumpyTest (unittest.TestCase) :
    mock = Numpy()

    def test_np_linspace(self):
        self.mock.np_linspace()

    def test_np_arange(self):
        self.mock.np_arange()

    def test_np_mask(self):
        self.mock.np_mask()

    def test_np_eye(self):
        self.mock.np_eye()

    def test_indexing_slicing(self):
        self.mock.indexing_slicing()

if __name__ == '__main__':
    unittest.main()