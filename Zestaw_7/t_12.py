class Node:
    def __init__(self, string):
        self.string = string
        self.next = None

    def add(self, string, first=0, last=1):
        x = self
        if first:
            tmp = Node(string)
            tmp.next = self
            return tmp
        elif last and first == 0:
            tmp = Node(string)
            self.last().next = tmp
            return self
        else:
            tmp = Node(string)
            tmp.next = x.next
            x.next = tmp
            return self

    def print(self):
        x = self
        while x != None:
            print(x.string, end=' ')
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
        if self.string == None:
            return 0
        x = self
        i = 1

        while x != None:
            i += 1
            x = x.next

        return i

    def key_add(self, key):
        if self.string ==key:
            return 0

        if self!=None and self.next!= None:
            x, y = self, self.next
        else:
            return "Blad"

        while y!=None:
            if y.string == key:
                return 1
            x, y = y, y.next

        self.add(key)
        return 1


test = Node("1")
test.add("2")
test.add("3")
test.add("5")
test.add("7")
test.add("0")
test.print()
print(test.key_add("1"))
test.print()