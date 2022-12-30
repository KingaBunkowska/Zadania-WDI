# poprawić żeby dało się zdjąć ostatni element listy, można spróbować doklejać Node'a na początku

class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

    def exist(self, a):
        x = self
        while x != None:
            if x.val == a:
                return 1

            x = x.next

        return 0
    def add(self, val, sort = 0):
        x = self
        if sorted:
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
            print(x.val, end=' ')
            x = x.next
        print('')
    def pop(self, ele = None):
        if ele == None:
            i = j = self
            if self.next == None:
                self.val = None
                self.next = None

            j = j.next
            while j.next != None:
                i = i.next
                j = j.next

            i.next = None
        else:
            i = self
            if self.next == None and self.val == ele:
                self.val = None
                self.next = None
                return 1
            elif self.next == None:
                return -1

            j = self.next
            while j.next != None:
                if j.val == ele:
                    i.next = j.next
                    return 1

                j = j.next
                i = i.next


linked_list = Node(1)
linked_list.add(2, 1)
linked_list.add(9, 1)
linked_list.add(7, 1)
linked_list.add(111, 1)
linked_list.add(-1, 1)

linked_list.pop(2)
linked_list.print()

print(linked_list.size())
