# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

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

  # YOUR CODE HERE
  S = ([source], 0)
  Q = {}
  
  while (source != target):
      #visit the neighbors
      neighbors = graph.get_neighbors(source)
      x = None
      min_cost = float('inf')
      
      for neighbor in neighbors:
        if neighbor not in S[0]:
            if (neighbor[1] < min_cost):
                x = neighbor
                min_cost = neighbor[1]

      S[0].append(x)
      S[1] += min_cost
            
  explored = []
  distances = {
      source: 0
  }

  
  
  raise NotImplementedError
