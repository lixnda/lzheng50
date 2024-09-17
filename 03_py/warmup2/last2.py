def last2(str):
  a = str[-2:]
  count = 0
  for i in range(len(str)-2):
    if(str[i:i+2]==a):
      count+=1
  return count
