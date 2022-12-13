class List():
    def __init__(self, size):
        for _ in range(size):
            tmp = Node()
            tmp.next = self.next
            self.next = tmp




class Node():
    def __init__(self, size = 1, value = 0):
        for i in range(size-1):
            tmp = Node()
            tmp.next = self.next

            self.val = value
            self.next = None

    def value(self, a):
        x = self
        for i in range(a):
            if x == None:
                return "error"
            x = x.next

        return x.val

    def print(self):
        i = self
        while i != None:
            print(self.val)
            i = i.next


lista = List(3)
lista.print()