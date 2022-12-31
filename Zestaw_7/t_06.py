class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val, sort = 0):
        x = self
        if sort:
            if x.val > val:
                tmp = Node(x.val)
                tmp.next = x.next
                x.val = val
                x.next = tmp

                return
            while x.next != None:
                if x.next.val >= val:
                    tmp = Node(val)
                    tmp.next = x.next
                    x.next = tmp
                    return

                x = x.next
            tmp = Node(val)
            x.next = tmp
        else:
            tmp = Node(val)
            tmp.next = x.next
            x.next = tmp

    def print(self):
        x = self
        while x != None:
            print(x.val, end=' ')
            x = x.next
        print('')

    def last(self):
        if self == None:
            return None
        a, b = self, self.next
        while b != None:
            a, b = b, b.next

        return a

    def add_last(self, val):
        tmp = Node(val)
        self.last().next = tmp


list = Node(4)
list.add_last(5)
list.add_last(6)
list.add_last(7)
list.print()
