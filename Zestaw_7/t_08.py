class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # example of adding: list = list.add(3, first= 1) # it should be fine to do just list.add(3, last = 1) (not first)
    def add(self, val, sort = 0, first=0, last=1):
        x = self
        if sort:
            if x.val > val:
                tmp = Node(x.val)
                tmp.next = x.next
                x.val = val
                x.next = tmp

                return self
            while x.next != None:
                if x.next.val >= val:
                    tmp = Node(val)
                    tmp.next = x.next
                    x.next = tmp
                    return self

                x = x.next
            tmp = Node(val)
            x.next = tmp
            return self
        elif first and last == 0:
            tmp = Node(val)
            tmp.next = self
            return tmp
        elif last and first == 0:
            tmp = Node(val)
            self.last().next = tmp
            return self
        else:
            tmp = Node(val)
            tmp.next = x.next
            x.next = tmp
            return self

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

    def rm_every_second(self):
        if self.next != None:
            x = self
            y = self.next.next

            while y!= None and y.next!= None:
                x.next = y
                x = y
                y = y.next.next

            x.next = y

        return self


list = Node(1)
list = list.add(2)
list = list.add(3)
list = list.add(4)
list = list.add(5)
list = list.add(6)
list = list.add(7)
list = list.add(8)
list = list.add(9)
list.print()
list.rm_every_second()
list.print()

