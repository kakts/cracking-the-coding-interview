import sys
import math
from collections import Counter

# 回文チェック
# 回文かどうかのチェックをしたが 回文の順列化のチェックはしていなかった
def isPalindrome(text):
  textLen = len(text)
  isOdd = textLen % 2 != 0

  # O(n)
  charCounter = Counter()
  for char in text:
    if char == ' ':
      continue
    charCounter[char] += 1

  isExistOddChar = False
  print(charCounter)
  for elem, cnt in charCounter.items():
    print(elem)
    print(cnt)
    print(cnt // 2)
    if cnt % 2 != 0:
      # すでに他の文字で奇数個のものがある場合はFalse
      if isExistOddChar == True:
        return False
      isExistOddChar = True
    
  return True





args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]
print(isPalindrome(text))