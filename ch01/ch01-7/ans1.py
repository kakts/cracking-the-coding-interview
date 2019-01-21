import sys
args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]

# 行列のインデックスごとに入れ替える
# 計算量O(n^2) どんなアルゴリズムでも n^2の要素にふれなくてはいけない
def rotate1(matrix):

  # 縦と横が同じサイズでない場合
  n = len(matrix)
  if len(matrix) == 0 or len(matrix) != len(matrix[0]):
    return False

  layer = 0
  while layer < n:
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
      offset = i - first
      top = matrix[first][i]

      // 左端 → 上端
      matrix[first][i] = matrix[last - offset][first]

      // 下端 → 左端
      matrix[last - offset][first] = matrix[last][last - offset]

      // 右端 → 下端
      matrix[last][last - offset] = matrix[i][last]

      // 上端 → 右端
      matrix[i][last] = top 
    layer += 1
  
  return Tr

  

