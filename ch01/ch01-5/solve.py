import sys
import math
from collections import Counter
args = sys.argv
if len(args) != 3:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

def isDeletedChar(text1_counter, text2_counter):
  existCount = 0
  print(text1_counter)
  print(text2_counter)
  for char, count in text1_counter.items():
    print(text2_counter[char])
    if text2_counter[char] > 0:
      existCount += 1
  print(existCount)
  return existCount == len(list(text1_counter)) - 1

def isReplacedOneChar(text1, text2):
  # 異なる文字が場所が一箇所しか無いかどうか
  diff_count = 0
  for i in range(len(text1)):
    print(text1[i])
    if text1[i] != text2[i]:
      diff_count += 1
    # 異なる場所が2箇所あった時点でfalse
    if diff_count > 1:
      return False
  print(diff_count)
  return True

# TODO
def isReplaceableAtOneTime(text1, text2):
  # len(text1) > len(text2) 前提
  index1 = 0
  index2 = 0
  for i in range(len(text1)):
    if text1[i] == text2[i]:
      index1 += 1
      index2 += 1
    else:
      if text1[index1 + 2] == text2[index2]
    
    if index1 - index2 > 1:
      return False

# 誤答 文字数のカウントしかみてなかった
# 文字数は１文字削除で並び順が違っててもTrueになっていた
def wrongIsReplaceableAtOneTime(text1, text2):
  # 同じ文字の場合
  if text1 == text2:
    return True

  len_text1 = len(text1)
  len_text2 = len(text2)

  # 文字数の絶対値が1より大きい場合 ありえない
  if abs(len_text1 - len_text2) > 1:
    return False

  text1_counter = Counter()
  text2_counter = Counter()
  for char in text1:
    text1_counter[char] += 1

  for char in text2:
    text2_counter[char] += 1

  # 文字数が違う場合は 文字列長が長いものを判定し、
  # その文字列から1文字削除するともう一方の文字列になるかをチェックする
  if len_text1 == len_text2:
    # 1文字のみ置き換わっているかチェックする
    return isReplacedOneChar(text1, text2)
  elif len_text1 > len_text2:
    # text2から1文字除去したものがtext1かどうかチェックする
    return isDeletedChar(text1_counter, text2_counter)
  else:
    # text2から1文字除去したものがtext1かどうかチェックする
    return isDeletedChar(text2_counter, text1_counter)
  
text1 = args[1]
text2 = args[2]
print(isReplaceableAtOneTime(text1, text2))

  


  
  