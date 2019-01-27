import sys, os
sys.path.append(os.pardir)

from linked_list.node import Node
from collections import Counter


list = Node("c")
list.appendToTail("b")
list.appendToTail("c")
list.appendToTail("a")
list.appendToTail("d")
list.appendToTail("b")
list.appendToTail("c")

list.showAllNodeData()


target_count = 0
target_node = None
current_node = list
while target_count < 4:
  target_node = current_node.next
  current_node = current_node.next
  target_count += 1

print("target")
print(target_node.data)

# 先頭ノードからもアクセスできる版
# Nを連結リストの要素数として最悪O(N)
def deleteTargetNode(list, target_node):
  current = list

  while current.next != None:
    if current.next == target_node:
      current.next =target_node.next
      current = current.next
      break
    current = current.next
  return list

# O(1)
def deleteTargetNode2(target_node):
  if target_node.next == None:
    return None
  
  target_node.data = target_node.next.data
  target_node.next = target_node.next.next
  return target_node

result = deleteTargetNode(list, target_node)
print("reuslt: ---")
result.showAllNodeData()