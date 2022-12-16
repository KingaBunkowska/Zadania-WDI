class List():
    def __init__(self, size):
        self.sentinel = Node(size)
        prev = self.sentinel
        for i in range(size):
            tmp = Node(0)
            prev.next = tmp
            prev = tmp

    def print(self):
        size = self.sentinel.val
        x = self.sentinel.next
        while x!=None:
            print(x.val)
            x = x.next

    def get_from_index(self,index):
        size = self.sentinel.val
        x = self.sentinel.next

        if index >= size:
            return "error"

        for _ in range(index):
            x = x.next

        return x.val

    def set_value(self, value, index):
        size = self.sentinel.val
        x = self.sentinel.next

        if index>= size:
            return "error"

        for _ in range(index):
            x = x.next

        x.val = value

class Node():
    def __init__(self, value = 0):
        self.val = value
        self.next = None


lista = List(6)
lista.print()
lista.set_value(3, 3)
print(lista.get_from_index(3))
lista.print()