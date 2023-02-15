# time: across two days and about 3 hours in total
# link: https://leetcode.com/problems/sqrtx/description/
class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Here's how to find it.
        It's based on fractions.
        find the square root that is in between x.
        if x is 8
        then the nearest two square roots are 4
        9
        then u realise there is a 5 difference.
        that means translated it should be 2.8 as the squareroot,
        abouts.
        to find the nearest square root
        """
        
        """
        Above was the original intention but fractions don't work in leetcode for this solution.
        
        I realised list comprehensions did not work for looping through a list even though it is said,
        to be efficient.
        Instead I resorted to generators to loop through data I wanted using the next method to retrieve the object.
        Generators allow the data that is looped to not be stored in memory dramatically reducing the amount of ,
        memory used. 
        """
        if x == 0:
            return 0

        def generate_nums(start, end):
            current = start
            while current < end:
                yield current
                current += 1
        
        def check_sqrt(i):
            yield(i*i)

        start_range = 0

        if x > 100000:
            start_range = 1300
        my_nums = generate_nums(start_range, x+1)
        for i in my_nums:
            root = next(check_sqrt(i))
            if root > x:
                return i-1
            if root == x:
                return i
        return 5