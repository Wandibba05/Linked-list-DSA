
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def display(self):
        current = self.head
        if not current:
            print("The list is empty.")
        else:
            print("Names in the linked list:")
            while current:
                print("→", current.data)
                current = current.next


students = LinkedList()
students.append("Ronel Meli")
students.append("Emmanuel Onyango")
students.append("Trevor Yano")
students.append("Angela Irungu")
students.append("Emmanuel Wandibba")
students.append("Mercy Nyambura")


students.display()
