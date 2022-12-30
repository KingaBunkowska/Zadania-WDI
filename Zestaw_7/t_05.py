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

    def sort_by_last_digit(self, warden = 0):

        t = [Node(-i) for i in range(10)]
        if self == None:
            return 0

        x, y = self, self.next
        while y != None:
            t[x.val%10].next, x.next = x, t[x.val%10].next
            x, y = y, y.next

        t[x.val % 10].next, x.next = x, t[x.val % 10].next

        first = False
        first_i = False
        last = False
        for i in range(10):
            if t[i].next != None and first == False:
                first = t[i].next
                first_i = i
                last = t[i].last()
                break

        for j in range(first_i+1, 10):
            if t[j].next != None:
                last.next = t[j].next
                last = t[j].last()

        return first


test = Node(8)
test.add(2)
test.add(12)
test.add(22)
test.add(13)
test.add(62)
test.add(7)
test.add(88)
test.add(91)
test.add(27)

test.print()
test = test.sort_by_last_digit()
test.print()
