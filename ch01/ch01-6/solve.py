import sys
import math
from collections import Counter
args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]

def compressText(text):
  original_len = len(text)

  compressed_text = ''
  successor_count = 1
  # 次の文字と異なるときにcompressed_textに書き出す
  for i in range(original_len):

    if i == original_len - 1 or text[i] != text[i + 1]:
      compressed_text = compressed_text + text[i] + str(successor_count)
      successor_count = 1 # 連続カウント数を初期値に戻す
    else:
      successor_count += 1
  
  if original_len == len(compressed_text):
    return text
  else:
    return compressed_text


print(compressText(text))

  


  
  