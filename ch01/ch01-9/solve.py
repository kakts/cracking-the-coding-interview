# O(n^2)
import sys
import math
from collections import Counter
args = sys.argv
if len(args) != 3:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

def isRotatedMatched(s1, s2):
  """
  print("rotated")
  print("s1:" + s1)
  print("s2:" + s2)
  """
  return s1 == s2

def isStringRotated(s1, s2):
  # 文字数が違う場合は除外
  if len(s1) != len(s2):
    return False

  # O(n^2)
  # ここで２重ループで２つの文字列を調査していく
  # 候補がみつかったら更に文字列をチェックするので
  # 最悪のケースでO(n^3)
  for i in range(len(s1)):
    for j in range(len(s2)):
      if s1[i] == s2[j]:
        if isRotatedMatched(s1, s2[j:]) == True:
          if isRotatedMatched(s1[len(s1) - j:], s2[:j]):
            return True
  
  return False

#s1 = args[1]
#s2 = args[2]

s1 = "aadfdsadfadfafadfasfjjjkiiiiiiiijjkjkjkjksssssjjjjkjkjkjkkjfdjkjljkjkjkjrererermmvdsfksfdfdfdsaerqeeqrzfdarfareqrqreqfadfafadaff"
s2 = "jfdjkjljkjkjkjrererermmvdsfksfdfdfdsaerqeeqrzfdarfareqrqreqfadfafadaffaadfdsadfadfafadfasfjjjkiiiiiiiijjkjkjkjksssssjjjjkjkjkjkk"
for i in range(10000):
  isStringRotated(s1, s2)
print("finish")