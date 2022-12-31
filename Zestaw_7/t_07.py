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

    #without warden
    def pop(self):
        if self!=None and self.next!=None:
            x = self
            y = self.next
            z = self.next.next

            while z!=None:
                x, y, z = y, z, z.next

            x.next=None
        elif self.next == None:
            self.val = None #usuniecie pierwszego


list = Node(5)
list.add(4)
list.add(3)
list.add(2)
list.print()
list.pop()
list.pop()
list.print()
