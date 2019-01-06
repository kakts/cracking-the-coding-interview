# 文字列の最後尾から先頭に向かって編集するアプローチ
# 空白文字数を数える
# 実際に書き換える
import sys
args = sys.argv
if len(args) != 3:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py "test 11" 5
  ''')

text = args[1]
real_len = args[2]


def replaceSpaces(text, trueLength):
  spaceCount = 0
  

  for i in range(trueLength):
    # 空白文字をカウント
    if text[i] == ' ':
      spaceCount += 1
    
  # 最終的に変換語の文字数を計算する
  # 空画文字が %20になるので *2になる
  index = trueLength + spaceCount * 2
  ans = [' '] * index
  if trueLength < len(text):
    ans[trueLength] = '\0' # 文字列の終端
  
  for i in range(trueLength):
    strIndex = trueLength - 1 - i
    print(strIndex)
    if text[strIndex] == ' ':
      ans[index - 1] = '0'
      ans[index - 2] = '2'
      ans[index - 3] = '%'
      index -= 3
    else:
      ans[index - 1] = text[strIndex]
      index -= 1
    print(ans)
  return ans

print(replaceSpaces(text, int(real_len)))
