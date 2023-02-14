#timer: About 45 minutes.
#link: https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        The way the code works is this:
        I knew that a opening bracket has a corresponding end bracket.
        I know orders matter.
        With these in mind, I can formulate what is to be expected.
        What I did was store what was to be expected and inserted the back brackets,
        at the start of the list to form the characters I expect.
        The moment I encounter the back brackets I check if they are to be expected,
        if they are not return false.
        I also want to make sure that the string is more than 1 character or else return false,
        And to make sure the expected list is fulfilled, hence length of 0.
        """
        expected = []
        back_brackets = ["}", "]", ")"]
        for character in s:
            """
            I think what I will do is create what I would expect and,
            if it is met then delete it over time.
            """
            if character == "(":
                expected.insert(0, ")")
                continue
            if character == "{":
                expected.insert(0, "}")
                continue
            if character == "[":
                expected.insert(0, "]")
                continue
            if character in back_brackets and len(expected) >= 1:
                if expected[0] == character:
                    #del expected[0]
                    expected.pop(0)
                else:
                    return False
            else:
                return False
        if len(s) <= 1:
            return False
        if len(expected) >= 1:
            return False
        return True
            