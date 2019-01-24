
# 単方向連結リスト
class SingleLinkedList:
  def __init__(self):
    self.head = None
    self.prev = None
    self.node = None
  
  # 末端にノードを追加する
  def appendNode(self, new_node):
    node = head
    while node.next != None:
      node = node.next

    node.next = new_node
    count += 1
  
  # データ数を取得
  def len(self):
    return self.count
  
  # データを削除する

class D

# 双方向連結リスト
class DoubleLinkedList:

  # 初期化 先頭データ追加
  def __init__(self, data):
    self.prev = None
    self.next = None
    self.data = None
  
  def appendNode(self, data):
    if self.data == None:
      self.data = data