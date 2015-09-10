__author__ = 'cloudera'


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

