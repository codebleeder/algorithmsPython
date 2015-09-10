__author__ = 'cloudera'


class Graph:
    def __init__(self, n, adjacency_list, visit_list):
        self.n = n
        self.adjacency_list = adjacency_list
        self.visited_list = visit_list

    def print_graph(self):
        print 'n = ', self.n
        print 'adjacency_list = ', self.adjacency_list
        print 'visited_list = ', self.visited_list

    def dfs(self):
        for node in self.visited_list:
            if self.visited_list[node] == False:
                self.visit(node)

    def visit(self, node):
        if self.adjacency_list[node] != [None]:
            for adj_node in self.adjacency_list[node]:
                if self.visited_list[adj_node] == False and self.adjacency_list[adj_node] is not [None]:
                    self.visit(adj_node)
        self.visited_list[node] = True
        print 'visited = ', node

# test
adj_list = {1: [1, 3],
            2: [None],
            3: [4, 5],
            4: [None],
            5: [None]
            }

v_list = {1: False, 2: False, 3: False, 4: False, 5: False}

g = Graph(5, adj_list, v_list)
#g.print_graph()
g.dfs()