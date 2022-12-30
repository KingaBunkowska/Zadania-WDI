class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # copied from t_01.py
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

    #iterative
    def reversed(self, warden = 0):
        if warden:
            x = self.next
        else:
            x = self
        if x != None and x.next!=None:
            y = x.next
            z = x.next.next
            x.next = None
        elif x.next == None:
            return self
        elif x.next.next == None:
            z = None

        while z != None:
            y.next = x
            x, y = y, z
            z = z.next

        y.next = x
        if warden:
            self.next = y
            return self
        else:
            return y

test = Node(8)
test.add(5)
test.add(4)
test.add(3)
test.add(2)
test.add(1)

test.print()
test = test.reversed()
test.print()