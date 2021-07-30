class Palindrome (object):

    def str_to_lits(self, payload : str) -> [] :
        '''strs = []
        ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        for char in ls :
            if char.isalnum():
                strs.append(char.lower())'''
        return [i for i in payload if i.isalnum()]

    def isPalindrome(ls: []) -> bool:
        """while len(ls) > 1:
            if ls.pop(0) != ls.pop():
                return False
            else:return True"""

        return [i for i in ls if ls.pop(0) != ls.pop()]




