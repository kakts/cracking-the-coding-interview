import sys
import math

# 回文チェック
# 回文かどうかのチェックをしたが 回文の順列化のチェックはしていなかった
def isPalindrome(text):
  fixedList = []
  textLen = len(text)
  # 空文字除去
  for char in text:
    if char == ' ':
      continue
    fixedList.append(char)
  
  # 全部から文字 Trueとする 要確認
  if len(fixedList) == 0:
    return True

  fixedListLen = len(fixedList)
  print(fixedList)
  for i in range(math.floor(fixedListLen / 2)):
    print(i)
    if fixedList[i] != fixedList[fixedListLen - 1 - i]:
      return False
  return True
  



args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]
print(isPalindrome(text))