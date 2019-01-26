import sys, os
sys.path.append(os.pardir)

from linked_list.node import Node
from collections import Counter

"""
 バッファが使用できない場合
 2つのポインタを使う

 １: 先頭の要素から順番に調べるポインタ
 ２: １より後方のすべての要素を調べる
要は二重ループ

消費メモリはO(1)だが O(n^2)の計算量
"""
def deletedups(node):
  char_counter = Counter()
  
  current = node
  while current != None:
    # currentより先のノードで同じ値を持つノードを削除
    runner = current
    while runner.next != None:
      if runner.next.data == current.data:
        # 要素を削除 ポインタの向き先を１つ先にする
        runner.next = runner.next.next
      else:
        runner = runner.next
    
    current = current.next
  
