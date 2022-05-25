class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def find(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " not found"
            return self.left.find(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            return self.right.find(value)
        else:
            return str(self.data) + " is found"

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find(7))
print(root.find(14))

