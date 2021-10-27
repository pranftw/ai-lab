class Queue:
    def __init__(self, type):
        self.type = type #fifo or lifo
        self.que = []

    def push(self, data):
        self.que.append(data)

    def pop(self):
        if(self.type=="lifo"):
            return self.que.pop(-1)
        elif(self.type=="fifo"):
            return self.que.pop(0)


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        if(parent is not(None)):
            self.parent.children.append(self)
        self.children = []


class BFS:
    def __init__(self, root_node):
        self.root_node = root_node
        self.queue = Queue("fifo")
        self.queue.push(self.root_node)
        self.order = []
    
    def recurse(self, node):
        self.order.append(node.data)
        for child in node.children:
            self.queue.push(child)
        self.recurse(self.queue.pop())


class DFS:
    def __init__(self, root_node):
        self.root_node = root_node
        self.queue = Queue("lifo")
    
    def recurse(self, node):
        pass
    

if __name__=='__main__':
    node_0 = Node("0", None)
    node_1 = Node("1", node_0)
    node_2 = Node("2", node_0)
    node_3 = Node("3", node_0)
    node_4 = Node("4", node_1)
    node_5 = Node("5", node_1)

    bfs = BFS(node_0)
    bfs.recurse(bfs.root_node)
    print(bfs.order)