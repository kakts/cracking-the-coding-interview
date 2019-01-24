
class Node:
  next = None
  data = None

  def __init__(self, data):
    self.data = data
  
  """
  # 次の要素を追加する
  # すでに要素が追加されている場合は子要素を再帰的に探索する
  # 連結している要素数nとした場合 最悪O(n)
  この場合 複数のオブジェクトが連結リストへの参照を必要としていて、
  連結リストの先頭が変更された場合 いくつかのオブジェクトは古い先頭ノードを参照したままになる
  なので改善の余地がある
  """
  def appendToTail(self, data):
    end = Node(data)
    n = self
    # 末端ノードが見つかるまでループ
    while n.next != None:
      n = n.next

    # 末端ノードのnextにデータ追加
    n.next = end
  
  def deleteNode(self, head, data):
    n = head
    if n.data == data:
      return head.next
    
    while n.next != None:
      if n.next.data == data:
        n.next = n.next.next
        return head
      
      n = n.next
    
    return head

class DoublyLinkedNode:
  def __init__(self, data):
    self.prev = None
    self.next = None
    self.data = data
  
  def appendToTail(self, data):
    end = DoublyLinkedNode(data)
    n = self
    # 末端ノードが見つかるまでループ
    while n.next != None:
      n = n.next

    # 末端ノードのnextにデータ追加
    n.next = end
    # 新しい末端ノードの前ノードに旧末端ノードを追加
    end.prev = n
    
  def deleteNode(self, data):
    n = self
    if n.data == data:
      # ノードの先頭を移動
      n.next.prev = None
      return n.next
    
    while n.next != None:
      if n.next.data == data:
        n.next = n.next.next
        return self
      n = n.next
    
    return self


    