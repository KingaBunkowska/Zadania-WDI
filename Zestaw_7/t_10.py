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

        while x!= None:
            i += 1
            x = x.next

        return i

        # without warden

    def pop(self):
        if self != None and self.next != None:
            x = self
            y = self.next
            z = self.next.next

            while z != None:
                x, y, z = y, z, z.next

            res = x.next.val
            x.next = None

        elif self.next == None:
            res = self.val
            self.val = None  # usuniecie pierwszego

        try:
            return res
        except "error":
            res = None

    def add_numbers(self, other):
        def launch(list, list2):
            i = list.size()-1
            moved = 0
            while list2.size()>0:
                moved = add_number(list, list2.pop() + moved, i)
                i -= 1

            while moved!=0 and i>0:
                moved = add_number(list, moved, i)
                i -= 1

            if moved!= 0:
                list = list.add(1, first=1)

            return list

        def add_number(node, val, index):
            x = node
            for _ in range(index-1):
                x = x.next

            x.val += val
            if x.val > 9:
                x.val -= 10
                return 1
            return 0

        if self.size() >= other.size():
            node = launch(self, other)
        else:
            node = launch(other, self)

        return node


num1 = Node(9)
num1.add(2)
num1.add(3)


num2 = Node(4)
num2.add(9)
num2.add(9)

num1.print()
num2.print()
num1 = num1.add_numbers(num2)
num1.print()