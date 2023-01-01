class Node:
    def __init__(self, beg, end):
        self.beg = beg
        self.end = end
        self.next = None

    def print(self):
        x = self
        while x!= None:
            print(x.beg, x.end, end =' ')
            x = x.next

        print('')

    def add(self, beg, end):
        tmp = Node(beg, end)
        tmp.next = self
        return tmp

    def reduce(self):
        if not (self!=None and self.next != None):
            return self

        x, y = self, self.next
        next_good = 0
        while x != None:
            next_good = 0
            z, y = x, x.next
            while y!= None:
                deleted = 0

                if x.beg >= y.beg and x.end >= y.end and y.end >= x.beg:
                    x.beg = y.beg
                    deleted = 1

                elif x.beg <= y.beg and x.end >= y.beg and x.end >= y.end:
                    deleted = 1

                elif x.beg <= y.beg and y.beg <= x.end and x.end <= y.end:
                    x.end = y.end
                    deleted = 1

                elif y.beg <= x.beg and x.end <= y.end:
                    x.beg = y.beg
                    x.end = y.end
                    deleted = 1

                if deleted == 0 and next_good ==0:
                    x.next = y
                    next_good = 1

                if deleted == 1:
                    z.next = y.next

                z, y = y, y.next

            x = x.next

        return self


test = Node(15, 19)
test = test.add(2, 5)
test = test.add(7, 11)
test = test.add(8, 12)
test = test.add(5, 6)
test = test.add(13, 17)
test.print()
test = test.reduce()
test.print()