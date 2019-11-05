from util import Stack

def earliest_ancestor(ancestors, starting_node):
   # create a queue
    q = Queue()
    # enqueue a list holding the starting vertex id
    q.enqueue([starting_node])
    # created an empty visited set
    visited = set()
    # while the queue is not empty
    while q.size() > 0:
        # dequeue to the path
        path = q.dequeue()
        # set a vert to the last item in the path
        vert = path[-1]
        # if vert is not in visited
        if vert not in visited:
            # add vert to visited set
            visited.add(vert)
            # if vert is equal to endWord
            # if vert == endWord:               // if vert has now parent return vert
                # return path
                # return path
            # loop over next vert in vertices at the index of vert
            for next_vert in get_neighbors(vert):
                # set a new path equal to a new list of the path (copy)
                new_path = list(path)
                # append next vert to new path
                new_path.append(next_vert)
                # enqueue the new path
                q.enqueue(new_path)