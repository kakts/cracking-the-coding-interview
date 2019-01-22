def isRotation(s1, s2):
  s1_len = len(s1)
  if s1_len != len(s2):
    return False
  
  for i in range(s1_len):
    # index iで左右分割する
    x = s1[:i]
    y = s1[i:]
    if (y + x) == s2:
      return True
  return False


s1 = "aadfdsadfadfafadfasfjjjkiiiiiiiijjkjkjkjksssssjjjjkjkjkjkkjfdjkjljkjkjkjrererermmvdsfksfdfdfdsaerqeeqrzfdarfareqrqreqfadfafadaff"
s2 = "jfdjkjljkjkjkjrererermmvdsfksfdfdfdsaerqeeqrzfdarfareqrqreqfadfafadaffaadfdsadfadfafadfasfjjjkiiiiiiiijjkjkjkjksssssjjjjkjkjkjkk"
for i in range(10000):
  isRotation(s1, s2)
print("finish")