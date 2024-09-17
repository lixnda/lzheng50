def centered_average(nums):
  mina = nums[0]
  maxa = nums[0]
  suma = 0
  for i in nums:
    mina=min(i, mina)
    maxa=max(i, maxa)
    suma+=i
  return (suma-mina-maxa)/(len(nums)-2)
