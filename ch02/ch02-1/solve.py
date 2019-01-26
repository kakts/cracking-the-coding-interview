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
def deleteDuplicateData(list):
  char_counter = Counter()
  node = list
  before = None
  char_counter[node.data] += 1
  while node.next != None:
    node = node.next
    # 先頭ノードで除去する場合はありえないのでbefore != Noneはいれない
    if char_counter[node.data] >= 1:
      before.next = node.next
    char_counter[node.data] += 1
    before = node
  return list

fixed = deleteDuplicateData(list)
fixed.showAllNodeData()
