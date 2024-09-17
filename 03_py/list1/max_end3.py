def max_end3(nums):
  largest = max(nums[0], nums[-1])
  for i in range(len(nums)):
    nums[i]=largest
  return nums
