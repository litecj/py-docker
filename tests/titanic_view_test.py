import unittest

from titanic.views.view import TitanicView


class TitanicViewTest(unittest.TestCase):

    mock = TitanicView()

    def test_modeling(self):
        self.mock.modeling()


    '''def test_preprocessing(self) :
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this'''

    # def test_submit(self):
    #     self.mock.submit()

if __name__ == '__main__':
    unittest.main