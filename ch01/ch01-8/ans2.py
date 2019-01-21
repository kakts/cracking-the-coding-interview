# ans1.pyの改良版
"""
行配列の代わりに最初の行を使用し、 列配列の代わりに最初の列を使用することで、空間計算量をO(1)に減らせる
１ 最初の行と最初の列に０があるか確認し、rowHasZeroとcolumnHasZeroを設定する
２ matrix[i][j]が0のときは常に matrix[i][0]とmatrix[0][j]を0に設定し
matrixの残りを操作する
３ matrixの残りを操作し  matrix[i][0]に0がある場合は行iを０でうめる
４ matrixの残りを操作し、matrix[0[j]に０がある場合は列jを０でうめる
５ 必要に応じて 最初の行と最初の列を０にする
"""

def setZerosImp(matrix):
  rowHasZero = False
  columnHasZero = False

  # 最初の行に0があるかチェック
  # O(m)
  for j in range(len(matrix[0])):
    if matrix[0][j] == 0:
      rowHasZero = True
      break
  
  # 最初の列に0があるかチェック
  # O(n)
  for i in range(len(matrix)):
    if matrix[i][0] == 0:
      columnHasZero = True
      break

  # 残りの行列に0があるかをチェック
  for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
      if matrix[i][j] == 0:
        # 先頭の行、列を0にする
        matrix[i][0] = 0
        matrix[0][j] = 0
  
  # 最初の列の値に基づいて行を0でうめる
  for i in range(1, len(matrix)):
    if matrix[i][0] == 0:
      nullifyRow(matrix, i)

  # 最初の行の値に基づいて列を0で埋める
  for j in range(1, len(matrix[0])):
    if matrix[0][j] == 0:
      nullifyColumn(matrix, j)

  # 最初の行を0でうめる
  if rowHasZero == True:
    nullifyRow(matrix, 0)
  
  # 最初の列を0でうめる
  if columnHasZero == True:
    nullifyColumn(matrix, 0)

  return matrix

def nullifyRow(matrix, row):
  for j in range(len(matrix[0])):
    matrix[row][j] = 0

def nullifyColumn(matrix, column):
  for k in range(len(matrix)):
    matrix[k][column] = 0

def main():
  list = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
  ]
  fix = setZerosImp(list)
  return fix

print(main())
  