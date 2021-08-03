import unittest

from titanic.views.view import TitanicView


class TitanicViewTest(unittest.TestCase):

    mock = TitanicView()

    def test_modeling(self):
        this = self.mock.preprocessing()


    '''def test_preprocessing(self) :
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this'''

if __name__ == '__main__':
    unittest.main