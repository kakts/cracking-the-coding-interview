import sys
import math
from collections import Counter

# O(mn)のループが二回走る
def changeToZero(matrix):
  m = len(matrix)
  n = len(matrix[0])


  foundZeroRow = [False] * m
  foundZeroColumn = [False] * n
  for i in range(m):
    for j in range(n):
      data = matrix[i][j]
      if data == 0:
        # 0にするべき行と列のインデックスを追加する
        foundZeroRow[i] = True
        foundZeroColumn[j] = True
  print(foundZeroRow)
  print(foundZeroColumn)

  for i in range(m):
    toBeDeletedRow = foundZeroRow[i]
    for j in range(n):
      toBeDeletedColumn = foundZeroColumn[j]
      if toBeDeletedRow == True or toBeDeletedColumn == True:
        matrix[i][j] = 0
  
  return matrix

def main():
  matrix = [
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
  ]
  print(matrix)
  fix = changeToZero(matrix)
  print(fix)
main()


    
        

