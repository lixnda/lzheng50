def rotate_left3(nums):
  a = []
  for i in range(len(nums)-1):
    a.append(nums[i+1])
  a.append(nums[0])
  return a
