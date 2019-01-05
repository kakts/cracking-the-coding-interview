import sys

# ascii文字の文字列がすべて固有（重複する文字がない）かチェックする
# ascii文字 128種類
def isUniqChars(str):
  if len(str) > 128:
    return False
  
  char_set = [False] * 128

  for char in str:
    # 文字列をasciiに変換
    ascii_char = ord(char)
    if char_set[ascii_char] == True:
      return False
    char_set[ascii_char] = True
  
  return True

args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]
print(isUniqChars(text))