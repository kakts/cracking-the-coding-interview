import sys
from collections import Set

# counterを使った実装
# bcr O(n)

args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

target = args[1]
char_set = set()
isUniq = True
# 重複なしの場合 O(n)
for char in target:
  if char in char_set:
    # 重複を見つけた段階でループ終了
    isUniq = False
    break
  char_set.add(char)

print(isUniq)
