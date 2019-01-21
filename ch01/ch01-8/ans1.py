# 自分で書いたのと同じ
# まだ改良の余地がある
def setZeros(matrix):
  m = len(matrix)
  n = len(matrix[0])
  row = [False] * m
  column = [False] * n

  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 0:
        row[i] = True
        column[j] = True

  # 行を0で埋める
  for i in range(len(row)):
    if row[i] == True:
      nullifyRow(matrix, i)
  
  # 列を0で埋める
  for j in range(len(column)):
    if column[j] == True:
      nullifyColumn(matrix, j)


def nullifyRow(matrix, row):
  for j in range(len(matrix[0])):
    matrix[row][j] = 0

def nullifyColumn(matrix, column):
  for k in range(len(matrix)):
    matrix[k][column] = 0

