def reverse3(nums):
  a = []
  for i in range(len(nums)-1, -1, -1):
    a.append(nums[i])
  return a
