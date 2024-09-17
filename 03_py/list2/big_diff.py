def big_diff(nums):
  mina = nums[0]
  maxa = nums[0]
  for i in nums:
    mina = min(i, mina)
    maxa = max(i, maxa)
  return maxa-mina
