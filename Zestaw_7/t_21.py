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

    def rm_longest_increasing_list(self):
        if self.val == None or self.next == None:
            return self
        if self.val < self.next.val:
            self.val = self.next = None
            return self

        x, y, z = self, self, self.next
        max_len = 0
        beginning = None
        end = None
        only_one = 1


        while x != None and x.next != None:
            y, z = x, x.next
            lenght = 1
            while z!= None:
                if y.val < z.val:
                    lenght += 1
                else:
                    if lenght == max_len:
                        only_one = 0
                    elif lenght > max_len:
                        max_len = lenght
                        beginning = x
                        end = y
                        only_one = 1

                    x = y
                    break



                y, z = y.next, z.next
                if z == None:
                    if lenght == max_len:
                        only_one = 0
                    elif lenght > max_len:
                        max_len = lenght
                        beginning = x
                        end = y
            x = x.next

        if only_one and max_len > 0:

            i = self
            while i != None and i.next != beginning:
                i = i.next

            if end != None:
                i.next = end.next

            if self == beginning:
                return end.next

        return self


test = Node(3)
test.add(2)
test.add(1)
test.add(3)
test.add(7)
test.add(1)
test.add(2)
test.add(3)
test.add(4)


test.print()
test = test.rm_longest_increasing_list()
test.print()