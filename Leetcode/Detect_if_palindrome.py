import math as mat


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if negative return false
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # reverse is the number reversed
        reverse = 0

        # Is the number that is used for creating reverse
        number = x

        # build the reverse string
        while number > 0:
            # grab the remainder if there is one
            lastDigit = number % 10

            # build the reverse string and move the reverse to the 10,100,1000's column
            reverse = (reverse * 10) + lastDigit

            # Shift the number down a decimal
            number = number / 10

            # Trash the popped number
            number = mat.floor(number)

        # Check if the reverse number is equal to the original number
        if reverse == x:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution.isPalindrome('self',121)
    print(solution)