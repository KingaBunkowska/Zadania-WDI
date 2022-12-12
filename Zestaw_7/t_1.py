# poprawić żeby dało się zdjąć ostatni element listy, można spróbować doklejać Node'a na początku

class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

    def is_in(self, a):
        x = self
        while x != None:
            if x.val == a:
                return 1

            x = x.next

        return 0

    def push(self, a):
        x = Node(a)
        i = self
        while i.next != None:
            i = i.next

        i.next = x

    def size(self):
        x = self
        res = 0
        while x != None:
            res += 1
            x = x.next

        return res

    def print(self):
        x = self
        while x != None:
            print(x.val)
            x = x.next

    def pop(self):
        i = j = self
        if self.next != None:
            i = self.next
        while i.next != None:
            i = i.next
            j = j.next

        j.next = None

first = Node(3)

first.push(4)
first.push(6)
first.push(8)
first.pop()
first.pop()
first.pop()
first.pop()
first.print()

print(first.size(), first.is_in(8))
