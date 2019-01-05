import sys
from collections import Counter

# counterを使った実装
# bcr O(n)

args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

target = args[1]
char_counter = Counter()
isUniq = True
# 重複なしの場合 O(n)
for char in target:

  print(char_counter[char], char)
  if char_counter[char] == 1:
    # 重複を見つけた段階でループ終了
    isUniq = False
    break
  char_counter[char] += 1

print(isUniq)
