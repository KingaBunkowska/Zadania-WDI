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

    def first_even_fives_in_octal(self):
        def even_fives(val):  #return boolean
            octal = ""
            while val != 0:
                octal = str(val%8) + octal
                val //= 8

            fives = 0
            for digit in octal:
                if digit == '5':
                    fives += 1

            return not fives % 2

        if self.val == None:
            return self

        tmp = self
        x = self.next
        eligible = other = Node(None)
        if even_fives(tmp.val):
            eligible = tmp
            eligible.next = None
        else:
            other = tmp
            other.next = None

        while x!= None:
            tmp = x.next
            x.next = None
            if even_fives(x.val):
                if eligible.val == None:
                    eligible = x
                else:
                    eligible.last().next = x
            else:
                if other.val == None:
                    other = x
                else:
                    other.last().next = x

            x = tmp

        other.last().next = None
        eligible.last().next = other

        return eligible


test = Node(45) #even
test.add(13)    #odd
test.add(41)    #odd
test.add(21)    #odd
test.add(8)     #even
test.add(7)     #even
test.add(5)     #odd
test.add(7)     #even
test.add(5)     #odd
test.add(45)    #even

# 45 8 7 7 45 | 13 41 21 5 5

test.print()
test = test.first_even_fives_in_octal()
test.print()

test = Node(5)
test.first_even_fives_in_octal()