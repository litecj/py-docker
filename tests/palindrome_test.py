import unittest

from basic.palindrome import Palindrome


class PalindromeTest(unittest.TestCase):
    mock = Palindrome()
    def test_str_to_lits(self):
        #ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        print(f'test_str_to_lists : {self.mock.str_to_lits("A man, a plan, a canal : Panama")}')

    def test_isPalindrome(self):
        ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        dict = {"RESULT": True for i in ls if ls.pop(0) != ls.pop()}
        print(f'test_isPalindrome : {dict["RESULT"]}')

if __name__ == '__main__':
    unittest.main()