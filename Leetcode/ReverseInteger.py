"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
 [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

#Billy Kamerow
#5/3/2020
import math as mat
class Solution(object):
    @classmethod
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Take the number x do a factorial of the largest 10^x number
         #The solutions that returns no remaind is the largest integer.
        #Repeat this process till you reach the least integer.
        neg_limit = -0x80000000
        pos_limit = 0x7fffffff
        if x >= pos_limit:
            return 0
        if x <= neg_limit:
            return 0
        #If x is between 0 and 9 return the value
        if x <= 9 and x >=-9:
            return x

        #If x is less than 0 convert it to positive. Then perform the reversal. Then multiply by negative afterwards.
        if x < 0:
            sample = x *-1
            x = self.reversal(sample)
            if x >= pos_limit:
                return 0
            if x <= neg_limit:
                return 0
            return x*-1
        ans = self.reversal(x)
        if ans >= pos_limit:
            return 0
        if ans <= neg_limit:
            return 0
        return ans

    @classmethod
    def reversal(self,input):
        holder = 0
        #Assume all inputs are positive

        while input > 0:

            #Step 1 — Isolate the last digit in number
            lastDigit = input% (10)

            #Step 2
            holder = (holder*10) +lastDigit

            #Step 3
            input = input/10

            # Step 4 round it off to the floor to see if there is any issue
            input = mat.floor(input)

        return int(holder)


if __name__ == '__main__':
    reverse = Solution.reverse(-1563847412)
    print(reverse)
