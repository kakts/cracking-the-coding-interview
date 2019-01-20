# 自分の解答と同じだが 計算量が悪い O(n + k^2)

import sys
import math
args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]

# 計算量が悪い
"""
pをもとの文字列のサイズ kを連続する文字数の数 とすれば
実行時間はO(p + k^2)となる
文字列の連結には O(n^2)の計算時間を要するのでかなり遅い
"""
def compressBad(text):
  compressedText = ""
  countConsecutive = 0
  for i in range(len(text)):
    countConsecutive += 1

    # 次の文字が現在の文字と異なる場合 この文字を結果に追加する
    if i == len(text) - 1 or text[i] == text[i + 1]:
      compressedText = compressedText + text[i] + str(countConsecutive)
      countConsecutive = 0
  
  return compressedText if len(compressedText) < len(text) else text

# compressBadをstringBuilderを用いて計算量を改善した
"""
pythonでいうstring builderは 配列を使って文字をappendして最後にjoinする方法でおこなう
"""
def compress(text):
  compressedText = []
  countConsecutive = 0
  for i in range(len(text)):
    countConsecutive += 1

    # 次の文字が現在の文字と異なる場合 この文字を結果に追加する
    if i == len(text) - 1 or text[i] == text[i + 1]:
      # これにより毎回文字列を生成せずにすむ
      compressedText.append(text[i])
      compressedText.append(countConsecutive)
      countConsecutive = 0
  
  return "".join(compressedText) if len(compressedText) < len(text) else text

for i in range(100000):
  compressBad(text)
print("finish")


  
  