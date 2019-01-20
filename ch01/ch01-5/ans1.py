import sys
import math
args = sys.argv
if len(args) != 3:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

# nを短い方の文字列の長さとして O(n)

"""
文字列長が２以上の場合 アルゴリズムはO(1)で終了する
したがって 非常に長い文字列が実行時間を大幅に増やすことはない


両方の文字列が長いばああにのみ、実行時間が増加

"""
def oneEditAway(text1, text2):
  len_text1 = len(text1)
  len_text2 = len(text2)
  if abs(len_text1 - len_text2) >= 2:
    return False
  elif len_text1 == len_text2:
    return oneEditReplace(text1, text2)
  elif len_text1 < len_text2:
    return oneEditInsert(text1, text2)
  else:
    return oneEditInsert(text2, text1)

# 1文字置換かどうかのチェック
def oneEditReplace(text1, text2):
  foundDifference = False
  for i in range(len(text1)):
    if text1[i] != text2[i]:
      if foundDifference == True:
        return False
      
      foundDifference = True
  return True

# 1文字をs1に挿入してs2を作ることができるかのチェック
def oneEditInsert(text1, text2):
  index1 = 0
  index2 = 0
  while (index2 < len(text2) and index1 < len(text1)):
    if text1[index1] != text2[index2]:
      # 前のループですでに文字が異なるものがある場合
      if index1 != index2:
        return False
      index2 += 1
    else:
      index1 += 1
      index2 += 1
  
  return True

text1 = args[1]
text2 = args[2]
print(text1)
print(oneEditAway(text1, text2))