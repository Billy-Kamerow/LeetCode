
#Billy Kamerow
#Objective:
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #Cycle through nums from the beginngin to the end and look to see which integers add to the target
        length = len(nums)
        for i in range(0, length):
            for w in range(i+1, length):
                if nums[i] + nums[w] == target:
                    print('you got it')
                    indice1 = i
                    indice2 = w
                    print(i)
                    print(w)
                else:
                    pass


        return(indice1,indice2)

if __name__ == '__main__':
    print('alpha')
    numbers = Solution.twoSum('self',[1,2,3,4,5],7)
    print(numbers)
