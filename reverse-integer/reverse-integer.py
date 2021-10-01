class Solution:
    def reverse(self, x):
        y = str(abs(x))[::-1]
        x = int('-' + y) if x < 0 else int(y)
        return x if -2**31 < x < 2**31-1 else 0