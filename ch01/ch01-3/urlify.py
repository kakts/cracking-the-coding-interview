import sys

# 空白を %20に置き換える
# O(real_len)
# 文字列の先頭から操作する
def URLify(str, real_len):
  spaceIndexList = []
  totalIndexCount = 0
  for char in str:
    if char == ' ':
      spaceIndexList.append(totalIndexCount)
    totalIndexCount += 1
  
  print(type(real_len))
  print(spaceIndexList)
  list = []
  realCount = 0
  fixedCount = 0
  for i in range(real_len):
    print(i)
    print(spaceIndexList)
    nextSpaceIndex = spaceIndexList[0] if len(spaceIndexList) > 0 else 0
    if nextSpaceIndex == i:
      list.append('%')
      list.append('2')
      list.append('0')
      if len(spaceIndexList) > 0:
        del spaceIndexList[0]
      fixedCount += 2
    else:
      print("push real" + str[realCount])
      list.append(str[realCount])
      fixedCount += 1

    realCount += 1

  return list

args = sys.argv
if len(args) != 3:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py "test 11" 5
  ''')

text = args[1]
real_len = args[2]

print(URLify(text, int(real_len)))