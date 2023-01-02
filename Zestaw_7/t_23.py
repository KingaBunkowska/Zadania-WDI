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

    def cycle_len(self):
        y = self
        visited = [y]
        while y!= None and y.next not in visited:
            y = y.next
            visited.append(y)

        cycle_beg = y.next
        y = y.next.next
        res = 1
        while y!=cycle_beg:
            res += 1
            y = y.next

        return res


test = Node(3)
test.add(2)
test.add(3)
test.add(4)
test.add(1)
test.last().next = test
print(test.cycle_len())