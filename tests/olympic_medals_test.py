import unittest

from basic.olympic_medals import Olympic

class OlympicMedalsTest(unittest.TestCase):
    mock = Olympic()

    def test_read_wiki(self):
        self.mock.read_wiki()

if __name__ == '__main__':
    unittest.main()