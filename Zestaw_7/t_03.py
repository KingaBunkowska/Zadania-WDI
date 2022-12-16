class Node():
    def __init__(self, val = 0):
        self.val = val
        self.next = None

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

    def print(self):
        x = self
        while x != None:
            print(x.val)
            x = x.next

    def merge(self, other):
        if self.val == None:
            return other
        if other.val == None:
            return self

        prev_x = self
        prev_y = other
        x = self
        y = other

        if x.val > y.val:
            x, y = y, x
            prev_x, prev_y = prev_y, prev_x

        res = x

        while x != None and y!= None:
            done_x = 0
            while x!= None and y!=None and x.val <= y.val:
                done_x = 1
                prev_x = x
                x = x.next

            if done_x:
                prev_x.next = y
                y = y.next

            done_y = 0
            while y!= None and x!= None and y.val <= x.val:
                done_y = 1
                prev_y = y
                y = y.next

            if done_y:
                prev_y.next = x
                x = x.next

        if x == None and y!=None:
            prev_x.next = y

        if y == None and x!=None:
            prev_y.next = x

        return res



Lista1 = Node(1) # -1, 0, 1, 2, 4
Lista1.add(4, 1)
Lista1.add(2, 1)
Lista1.add(-1, 1)
Lista1.add(0, 1)

Lista1.print()

Lista2 = Node(8) # 0, 1, 3, 8
Lista2.add(0, 1)
Lista2.add(1, 1)
Lista2.add(3, 1)


Lista2.print()

Sorted_lists = Lista1.merge(Lista2)
print("------------------------")
Sorted_lists.print()