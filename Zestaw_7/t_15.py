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

    def rm_15(self):
        def count_trinary(val):  #return tuple(no_of_one,  no_of_two)
            trinary = ""
            while val != 0:
                trinary = str(val%3) + trinary
                val //= 3

            one = two = 0
            for digit in trinary:
                if digit == '1':
                    one += 1
                elif digit == '2':
                    two += 1

            return one, two

        def to_rm(val):
            one, two= count_trinary(val)
            return one>two

        if self.val == None:
            return "Invalid list"

        first = self
        while to_rm(first.val) and first!= None:
            first = first.next

        if first == None:
            first = Node(None)
            return first

        x, y = first, first.next
        while y != None:
            if to_rm(y.val):
                y = y.next
                x.next = y
            else:
                x, y = y, y.next

        return first


test = Node(1)
test.add(4)
test.add(5)
test.add(8)
test.add(9)
test.add(10)
test.print()
test = test.rm_15()
test.print()