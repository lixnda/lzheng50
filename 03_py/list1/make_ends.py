def make_ends(nums):
  if(len(nums)<2):
    return [nums[0], nums[0]]
  return [nums[0], nums[-1]]
