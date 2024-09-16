def front_times(str, n):
  if(len(str)<3):
    a=str
  else:
    a=str[:3]
  b = ""
  for i in range(n):
    b+=a
  return b
