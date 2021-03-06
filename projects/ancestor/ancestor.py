from util import Queue

def earliest_ancestor(ancestors, starting_node):

    q = Queue()

    q.enqueue(starting_node)

    visited = []
    while q.size() > 0:

        vert = q.dequeue()

        tempArr = []
        for item in ancestors:
          if vert == item[1]:
            tempArr.append(item[0])
          
        if len(tempArr) == 1:
          q.enqueue(tempArr[0])
          visited.append(tempArr[0])          
        if len(tempArr) > 1:
          tempArr.sort()
          q.enqueue(tempArr[0])
          visited.append(tempArr[0])
    
    if visited == []:
      return -1
    
    return visited[-1]