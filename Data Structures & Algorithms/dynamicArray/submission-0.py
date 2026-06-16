class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.arr = [None for _ in range(capacity)]


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        lastVal = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return lastVal
 

    def resize(self) -> None:
        self.arr.extend([None for _ in range(self.cap)])
        self.cap *= 2


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
