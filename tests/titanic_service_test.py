import os
import unittest

from titanic.model.service import TitanicService


class TitanicServiceTest(unittest.TestCase):

    mock = TitanicService()

    def test_new_model(self) :
        # self.mock.new_model('train.csv')
        # print(os.getcwd())
        # print(self.mock.new_model("train"))
        print(self.mock.new_model("test"))



if __name__ == '__main__':
    unittest.main()