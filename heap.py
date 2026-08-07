class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    def get_left_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, node_index):
        return (node_index - 1) // 2

    def heapifyUp(self, index):
        if index == 0:
            return

        parent_node_index = self.get_parent_index(index)
        parent_node = self.items[parent_node_index]
        node = self.items[index]
        if node > parent_node:
            self.items[parent_node_index] = self.items[index]
            self.items[index] = parent_node
        else:
            return

        self.heapifyUp(parent_node_index)

    def heapifyDown(self, index):
        left_index = self.get_left_index(index)
        right_index = self.get_right_index(index)
        if left_index >= self.max_size or right_index >= self.max_size:
            return

        tmp = self.items[index]
        # left = None and right = None -> return
        if self.items[left_index] == None and self.items[right_index] == None:
            return
        # left != None and right = None -> compare node with left Node
        if self.items[left_index] != None and self.items[right_index] == None:
            if self.items[left_index] > self.items[index]:
                self.items[index] = self.items[left_index]
                self.items[left_index] = tmp
                self.heapifyDown(left_index)
        # right != None and left = None -> compare node with right Node
        if self.items[right_index] != None and self.items[left_index] == None:
            if self.items[right_index] > self.items[index]:
                self.items[index] = self.items[right_index]
                self.items[right_index] = tmp
                self.heapifyDown(right_index)
        # right != None and left != None -> check which one is greater -> compare
        if self.items[right_index] != None and self.items[left_index] != None:
            if self.items[right_index] > self.items[left_index]:
                if self.items[right_index] > self.items[index]:
                    self.items[index] = self.items[right_index]
                    self.items[right_index] = tmp
                    self.heapifyDown(right_index)
            else:
                if self.items[left_index] > self.items[index]:
                    self.items[index] = self.items[left_index]
                    self.items[left_index] = tmp
                    self.heapifyDown(left_index)

    def insert(self, value):
        self.items[self.size] = value
        self.heapifyUp(self.size)
        self.size += 1
        return

    def remove(self):
        if self.size == 0:
            return None
        tmp = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1
        self.heapifyDown(0)
        return tmp

    def printHeap(self):
        print(self.items)


heap = MaxHeap(40)
heap.insert(40)
heap.insert(50)
heap.insert(30)
heap.insert(20)
heap.insert(100)
heap.remove()
heap.printHeap()
