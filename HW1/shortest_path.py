# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError
import heapq


def shortest_path(graph, source, target):
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    #
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path
    #
    # NOTE: Please see instructions.txt for additional information about the
    # return value of this method.
    
    
    priority = [(source, 0)]
    
    
    seen = set()
    distances = {}
    previous = {}
    distances[source] = 0
    previous[source] = None
    path = []
    
    while priority:
        
        (current, cost) = heapq.heappop(priority)
        #(current, cost) = priority.pop()
        
        if current not in seen:
            seen.add(current)
            
            if current == target:
                
                while previous[current] is not None:
                    path = [current] + path
                    current = previous[current]
                
                path = [source] + path
                result = tuple((path, distances[target]))
                
                print ("result")
                print (result)
                return result
        
            for neigh in graph.get_neighbors(current):
                
                neigh_node = neigh[0]
                neigh_dist = neigh[1]
                
                if neigh_node in seen:
                    continue
            
                prev = distances.get(neigh_node, None)
                alt = cost + neigh_dist
                
                if prev is None or alt < prev:
                    distances[neigh_node] = alt
                    previous[neigh_node] = current
                    heapq.heappush(priority, (neigh_node, alt))
                    #priority.append((neigh_node, alt))





  
  
