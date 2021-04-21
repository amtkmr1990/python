class Queue_stream:
    def __init__(self):
        self.item_block = []

    def push(self, e):
        self.item_block.append(e)

    def pop(self):
        fifo = self.item_block[0]
        self.item_block = self.item_block[1:]
        return fifo

line = Queue_stream()
line.push(1)
line.push(4)
line.push(9)

print(line.pop())
print(line.pop())
print(line.pop())