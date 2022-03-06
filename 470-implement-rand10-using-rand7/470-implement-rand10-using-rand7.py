# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        i=(49*(rand7()-1)+7*(rand7()-1)+(rand7()-1))+1
        k=(i)%10+1
        return int(k)