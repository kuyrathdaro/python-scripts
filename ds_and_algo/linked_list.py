class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def in_between(self, middle_node, data):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        new_node = Node(data)
        new_node.next = middle_node.next
        middle_node.next = new_node
    
    def remove_node(self, key):
        head = self.head
        if head is not None:
            if head.data == key:
                self.head = head.next
                head = None
                return
        while (head is not None):
            if head.data == key:
                break
            prev = head
            head = head.next

        if head == None:
            return
            
        prev.next = head.next
        head = None
    
    def llistprint(self):
        printval = self.head
        while (printval):
            print(printval.data)
            printval = printval.next

llist = SLinkedList()
llist.at_beginning("Mon")
llist.at_end("Tue")
llist.at_end("Wed")
llist.at_end("Thu")
llist.at_end("Fri")
llist.at_end("Sat")
llist.at_beginning("Sun")
llist.llistprint()