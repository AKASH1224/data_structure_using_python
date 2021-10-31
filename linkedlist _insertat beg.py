class node:  # node class
    def __init__(self, data):
        self.data = data
        self.next = None


class ll:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        nb = node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp = ne

    def insert_pos(self, pos, data):
        np = node(data)
        temp = self.head
        for i in range(pos - 1):
            temp.next
        temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def display(self):
        if self.head is None:
            print("Empty Node")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
                temp = temp.next


L = ll()
n1 = node(10)
L.head = n1
n2 = node(20)
n1.next = n2
n3 = node(30)
n2.next = n3
L.insert_beg(5)
L.insert_beg(1)
L.insert_end(60)
L.insert_pos(5, 25)
L.insert_pos(3, 16)
L.display()
