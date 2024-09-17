def string_splosion(str):
  a = '';
  for i in range(len(str)):
    a+=str[0:i+1]
  return a
