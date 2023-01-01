class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def add(self, val):
        tmp = Node(val)
        tmp.next = self
        self.prev = tmp
        return tmp

    def print(self):
        x = self
        while x != None:
            print(x.val, end=' ')
            x = x.next
        print('')

    def rm_odd_ones_binary(self):
        def odd_binary(val):
            binary = ""
            while val != 0:
                binary = str(val%2) + binary
                val //= 2

            ones = 0
            for digit in binary:
                if digit == '1':
                    ones += 1

            return ones % 2

        first = self
        while first != None and odd_binary(first.val):
            first = first.next

        x = first.next
        while x != None and x.next != None:
            if odd_binary(x.val):
                y, x = x.prev, x.next
                y.next = x
                x.prev = y
            else:
                x = x.next

        if x.next == None and odd_binary(x.val):
            x.prev.next = None

        return first


test = Node(1)      #1
test = test.add(2)  #10
test = test.add(3)  #11
test = test.add(4)  #100
test = test.add(5)  #101
test = test.add(7)  #111
test = test.add(2)
test = test.add(8)  #1000
test = test.add(2)
test = test.add(5)


test.print()
test = test.rm_odd_ones_binary()
test.print()