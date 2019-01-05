# ans1の改良版 
# ビットベクトルを使って消費メモリを1/8にできる

import sys

args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

# アルファベットの小文字だけ使用すると仮定する
def isUniqueChars(text):
  checker = 0
  for char in text:
    val = ord(char) - ord("a")
    # 0から25桁それぞれにビットをたてる
    if ((checker & (1 << val)) > 0):
      print("faund")
      return False
    
    checker |= (1 << val)
  return True

print(isUniqueChars(args[1]))
