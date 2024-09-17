def sum13(nums):
  if(len(nums)==0):
    return 0

  count = 0
  i = 0
  while(i<len(nums)):
    if(nums[i]==13):
      i+=2
    else:
      count+=nums[i]
      i+=1
  return count
