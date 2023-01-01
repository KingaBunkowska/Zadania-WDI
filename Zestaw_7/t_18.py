class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # example of adding: list = list.add(3) # it should be fine to do just list.add(3, last = 1) (not first)
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
        elif first:
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

    def size(self):
        if self.val == None:
            return 0
        x = self
        i = 1

        while x != None:
            i += 1
            x = x.next

        return i

    def unique(self, memory = 1):
        if memory:
            t = []
            x, y = self, self.next
            t.append(self.val)
            while y != None:
                if y.val in t:
                    x.next = y.next
                    #print(x.val, y.val, y.next.val)
                    y = y.next
                else:
                    t.append(y.val)
                    x, y = x.next, y.next

            return self
        else:
            x = self
            while x.next!=None:
                a, y = x, x.next
                while y!=None:
                    if y.val == x.val:
                        a.next = y.next
                        y = y.next
                    else:
                        a, y = a.next, y.next

                x = x.next

            return self


test = Node(1)
test.add(1)
test.add(2)
test.add(4)
test.add(2)
test.add(9)
test.add(2)
test.add(4)
test.add(4)
test.add(4)
test.add(4)
test.add(9)
test.add(1)
test.add(17)
test.add(9)
test.print()
test = test.unique(memory = 0)
test.print()




