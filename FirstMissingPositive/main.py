import unittest

class Solution:
  def firstMissingPositive(self, nums) -> int:
    # if len(nums) == 0:
    #   return none
    if 1 not in nums:
      return 1
    for i in range(len(nums)):
      if i+1 not in nums:
        return i+1
    return len(nums)+1
      
class SolutionTest(unittest.TestCase):
  def test(self):
    x = Solution()
    self.assertEqual(x.firstMissingPositive([1,2,3,4]),5)
    self.assertEqual(x.firstMissingPositive([1,23,4,5]),2)
    self.assertEqual(x.firstMissingPositive([1,2,0]),3)
    self.assertEqual(x.firstMissingPositive([3,4,-1,1]),2)
    self.assertEqual(x.firstMissingPositive([7,8,9,11,12]),1)


# x = Solution()
# print(x.firstMissingPositive([1,2,3,4]))
if __name__ == '__main__':
    unittest.main()