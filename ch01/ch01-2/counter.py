# Counterを使った解答

import sys
from collections import Counter

args = sys.argv
if len(args) != 4:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-2.py testa testb y

    if use ignoreCase mode please input y in the third argument.
  ''')

text_a = args[1]
text_b = args[2]
isIgnoreCase = (args[3] == 'y')

def isAnagramText(text_a, text_b, isIgnoreCase):
  if len(text_a) != len(text_b):
    return False

  # あえてメソッド内で行っている
  if isIgnoreCase == True:
    text_a = text_a.lower()
    text_b = text_b.lower()

  # text_aの文字の使用数をカウントする
  # Counterの引数に渡せばよいがあえて自前でやる
  char_counter_a = Counter()
  # O(len(text_a))
  for char in text_a:
    char_counter_a[char] += 1

  # O(len(text_b))
  for char in text_b:
    # text_aに含まれない文字 または すでにチェックが完了した文字がある場合はすぐに終了
    if char_counter_a[char] == 0:
      return False
    char_counter_a[char] -= 1

  return True

print(isAnagramText(text_a, text_b, isIgnoreCase))

