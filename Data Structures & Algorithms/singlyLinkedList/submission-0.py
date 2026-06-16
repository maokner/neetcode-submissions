class LinkedList:
    
    def __init__(self):
        self.sentinel = Node(None, None)

    
    def get(self, index: int) -> int:
        curr = self.sentinel.next
        while index != 0 and curr is not None:
            curr = curr.next
            index -= 1
        if curr is None:
            return -1
        return curr.val
        

    def insertHead(self, val: int) -> None:
        self.sentinel.next = Node(val, self.sentinel.next)
        

    def insertTail(self, val: int) -> None:
        curr = self.sentinel
        while curr.next:
            curr = curr.next
        curr.next = Node(val, None)
        

    def remove(self, index: int) -> bool:
        curr = self.sentinel
        while index != 0 and curr.next:
            curr = curr.next
            index -= 1
        if not curr.next:
            return False
        curr.next = curr.next.next
        return True
        

    def getValues(self) -> List[int]:
        vals = []
        curr = self.sentinel.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
class Node:
    def __init__(self, val, nextVal):
        self.val = val
        self.next = nextVal