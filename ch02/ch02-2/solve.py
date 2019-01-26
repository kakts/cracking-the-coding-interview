import sys, os
sys.path.append(os.pardir)

from linked_list.node import Node
from collections import Counter


list = Node("a")
list.appendToTail("b")
list.appendToTail("a")
list.appendToTail("d")
list.appendToTail("b")
list.appendToTail("c")

list.showAllNodeData()

# Nを連結リストの要素数としてO(N)
def findNodeFromTail(node, index_from_tail):
  node_data_list = []
  node_data_list.append(node.data)
  while node.next != None:
    node = node.next
    node_data_list.append(node.data)
  
  data_len = len(node_data_list)
  # もし指定インデックスが要素数より多い場合は先頭を返す 
  if index_from_tail > data_len:
    return node_data_list[0]

  return node_data_list[data_len - 1 - index_from_tail]

result = findNodeFromTail(list, 2)
print("result: " + result)
