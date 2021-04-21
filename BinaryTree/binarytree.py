class BinaryTree:
    def __init__(self, head):
        self.head = head

    def add(self, new_node):
        current = self.head
        while current:
            if new_node == current.value:
                raise ValueError('This value already exist')
            elif new_node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break

    def find(self, value):
        current = self.head
        while current:
            print(type(current.value))
            if value == current.value:
                return f'{value} found ...'
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    return f'{value} Not Found ...'
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    return f'{value} Not Found ...'
                    break

    def inorder(self):
        self._recursive(self.head)

    def _recursive(self, current_node):
        if current_node:
            print(current_node)
        if not current_node:
            return
        self._recursive(current_node.left)

        self._recursive(current_node.right)

