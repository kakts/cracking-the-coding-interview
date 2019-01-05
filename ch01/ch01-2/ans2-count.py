import sys

args = sys.argv
if len(args) != 4:
  raise Exception('''
    Please input the target string. \n
    eg: $ python 1-2.py testa testb y

    if use ignoreCase mode please input y in the third argument.
  ''')

def isAnagramText(text_a, text_b, isIgnoreCase):
  if len(text_a) != len(text_b):
    print(1)
    return False
  
  if isIgnoreCase == True:
    text_a = text_a.lower()
    text_b = text_b.lower()

  letters = [0] * 128
  for char in text_a:
    letters[ord(char)] += 1

  for char in text_b:
    letters[ord(char)] -= 1
    if letters[ord(char)] < 0:
      return False
  
  return True

text_a = args[1]
text_b = args[2]
isIgnoreCase = (args[3] == 'y')
print(isAnagramText(text_a, text_b, isIgnoreCase))
