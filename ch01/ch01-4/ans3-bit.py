import sys
import math
from collections import Counter

def toggle(bitVector, index):
  if index < 0:
    return bitVector

  # index分だけ左シフトしたものをマスクとする
  mask = 1 << index
  
  if bitVector & mask == 0:
    bitVector |= mask
  else:
    # すでにフラグが立っていた場合
    # maskのビットを反転したものとandする
    # 該当のビットのみオフにする
    bitVector &= ~mask
  return bitVector

# 1bitだけフラグが立っているかチェックする
# 001000 & (001000 - 1) = 001000 & (000111) = 0
# 2bit以上フラグが立っていた場合
# 001010 & (001010 - 1) = 001010 & (001001) = 001000 != 0
def checkExactlyOneBitSet(bitVector):
  return bitVector & (bitVector - 1) == 0

def isPermutationPalindrome(phrase):
  bitVector = createBitVector(phrase)
  print(bitVector)
  return bitVector == 0 or checkExactlyOneBitSet(bitVector)

def createBitVector(phrase):
  bitVector = 0
  for char in phrase:
    x = ord(char) - ord('a')
    print("x" + str(x))
    bitVector = toggle(bitVector, x)
  return bitVector

args = sys.argv
if len(args) != 2:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-1.py test
  ''')

text = args[1]
print(isPermutationPalindrome(text))



