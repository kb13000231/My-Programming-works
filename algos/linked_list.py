class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}"


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        coun = 0

        while current:
            coun += 1
            current = current.next_node

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'[Head: {current.data}]')
            elif current.next_node is None:
                nodes.append(f'[Tail: {current.data}]')
            else:
                nodes.append(f'[Tail: {current.data}]')

            current = current.next_node
        return '-> '.join(nodes)
