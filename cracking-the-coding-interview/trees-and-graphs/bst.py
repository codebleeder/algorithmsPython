__author__ = 'cloudera'


class Node:
    def __init__(self):
        self.parent = None
        self.right = None
        self.left = None
        self.key = None

    def get_parent(self):
        return self.parent

    def set_parent(self, node_in):
        self.parent = node_in

    def get_right(self):
        try:
            return self.right
        except ValueError:
            print 'leaf node'

    def set_right(self, node_in):
        self.right = node_in

    def get_left(self):
        if self.left is not None:
            return self.left
        else:
            print 'leaf node'

    def set_left(self, node_in):
        self.left = node_in

    def get_key(self):
        return self.key

    def set_key(self, key_in):
        self.key = key_in

def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.get_left())
        print x.get_key()
        inorder_tree_walk(x.get_right())

def preorder_tree_walk(x):
    if x is not None:
        print x.get_key()
        preorder_tree_walk(x.get_left())
        preorder_tree_walk(x.get_right())

def postorder_tree_walk(x):
    if x is not None:
        preorder_tree_walk(x.get_left())
        preorder_tree_walk(x.get_right())
        print x.get_key()

def insert_node(root, x):
    p = None
    q = root
    while q is not None:
        p = q
        if q.get_key() > x.get_key():
            q = q.get_left()
        else:
            q = q.get_right()
    if p.get_key() > x.get_key():
        p.set_left(x)
    else:
        p.set_right(x)

x = Node()
y = Node()
z = Node()

x.set_key(5)
y.set_key(3)
z.set_key(6)
x.set_left(y)
x.set_right(z)
y.set_parent(x)
z.set_parent(x)

a = Node()
a.set_key(8)

#insert_node(x, a)
#inorder_tree_walk(x)
#preorder_tree_walk(x)
#postorder_tree_walk(x)

# graph traversal


class Vertex:
    def __init__(self, key):
        self.neighbors = {}
        self.id = key

    def add_neighbor(self, id, weight):
        self.neighbors[id] = weight

    def get_connections(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_weight(self, id):
        return self.neighbors[id]


class Graph:
    def __init__(self, adj_list = {}, num_vertices = 0):
        self.adj_list = adj_list
        self.num_vertices = num_vertices

    def add_vertex(self, id):
        new_vertex = Vertex(id)
        self.adj_list[id] = new_vertex
        self.num_vertices += 1

    def get_vertex(self, id):
        if id in self.adj_list:
            return self.adj_list[id]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm in self.adj_list and to in self.adj_list:
            self.adj_list[frm].add_neighbor(self.adj_list[to], cost)

    def get_vertices(self):
        return self.adj_list.keys()

    def get_num_vertices(self):
        return self.num_vertices

# construct graph
g = Graph()
for i in range(6):
    g.add_vertex(i)

#print g.adj_list
g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)

for i in range(0, g.get_num_vertices()):
    print i, '->'
    for connection in g.get_vertex(i).get_connections():
        print connection.get_id()
