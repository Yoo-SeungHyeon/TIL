class BinaryTree:
    def __init__(self):
        self.tree = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'k', 'L', 'M'
        ]

    def insert(self, value):
        self.tree.append(value)

    def get_node(self, index):
        if index < len(self.tree):
            return self.tree[index]

    def set_node(self, index, value):
        # if index >= len(self.tree):
            # self.insert(value)
        while index >= len(self.tree):
            self.tree.append(None)
        self.tree[index] = value