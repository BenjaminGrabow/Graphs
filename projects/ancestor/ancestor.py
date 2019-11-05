from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # at vertex_id create an empty set
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
       # if v1 and v2 exist in vertices list
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 at v1 of vertices
            # (add v2 to the vertices list at the index of v1)
            self.vertices[v1].add(v2)
        # otherwise
        else:
            # raise an error
            raise KeyError("That vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been vidited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
        # then its should be an empty set
           visited=set()

        print(starting_vertex)
        visited.add(starting_vertex)
        for vertex in self.vertices[starting_vertex]:
              if vertex not in visited:
                  self.dft_recursive(vertex,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            path = q.dequeue()
            v = path[-1]
            # if that vertex has not been vidited
            if v not in visited:
                # mark it as visited (printing for a representation)
                if v == destination_vertex:
                    return path
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            path = s.pop()
            v = path[-1]
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                if v == destination_vertex:
                  return path
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    s.push(new_path)






               def earliest_ancestor(ancestors, starting_node):
                pass