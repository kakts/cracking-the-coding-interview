# solve.pyの改良版 最悪のケースでO(n^3)
# こちらのスクリプトは全部多重ループがないためO(n)でいける
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

  # 同じ文字列だったらTrue
  if s1 == s2:
    return True

  # s1の先頭文字を保持しておく
  s1_first_char = s1[0]

  # 文字数カウント どちらも文字数が同じなので1ループで完結
  # s1の先頭文字がs2のどの位置に含まれているかもチェックする
  # s1の先頭文字がs2のどの位置に含まれるかを保持する配列
  # のちのちこの文字に対するループを行う
  s1_first_char_index_s2 = []

  # s1の先頭文字がs1中にいくつ存在するか
  s1_first_char_count = 0
  for i in range(len(s1)):
    if s1_first_char == s1[i]:
      s1_first_char_count += 1
    if s1_first_char == s2[i]:
      s1_first_char_index_s2.append(i)
  
  """
  print("s1_first_char_index_s2")
  print(s1_first_char_index_s2)
  """
  # 条件を満たす場合
  # s1の先頭文字がs1に含まれる数 == s1の先頭文字がs2に含まれる数
  # そうでない場合は条件を満たさない
  if s1_first_char_count != len(s1_first_char_index_s2):
    return True

  # s1の先頭文字がs2に含まれていない場合 条件を満たさない
  if len(s1_first_char_index_s2) == 0:
    return False

  # 最悪O(n)
  for index in s1_first_char_index_s2:
    if isRotatedMatched(s1, s2[index:]) == True and isRotatedMatched(s1[(len(s1) - index):], s2[:index]):
      # 条件を満たした時点でループ終了
      return True
  return False




#s1 = args[1]
#s2 = args[2]
s1 = "aadfdsadfadfafadfasfjjjkiiiiiiiijjkjkjkjksssssjjjjkjkjkjkkjfdjkjljkjkjkjrererermmvdsfksfdfdfdsaerqeeqrzfdarfareqrqreqfadfafadaff"
s2 = "jfdjkjljkjkjkjrererermmvdsfksfdfdfdsaerqeeqrzfdarfareqrqreqfadfafadaffaadfdsadfadfafadfasfjjjkiiiiiiiijjkjkjkjksssssjjjjkjkjkjkk"

for i in range(10000):
  isStringRotated(s1, s2)
print("finish")