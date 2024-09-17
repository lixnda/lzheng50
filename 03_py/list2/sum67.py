def sum67(nums):
  cont = True
  i = 0
  sum = 0
  while(i<len(nums)):
    if(cont==True and nums[i]==6):
      cont = False
    if(cont==True):
      sum+=nums[i]
    if(cont==False and nums[i]==7):
      cont = True
    i+=1
  return sum
