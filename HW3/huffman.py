# Represents a Huffman tree for use in encoding/decoding strings.
# A sample usage is as follows:
#
# h = HuffmanTree([('A', 2), ('B', 7), ('C', 1)])
# assert(h.encode('ABC') == '01100')
# assert(h.decode(h.encode('ABC')) == 'ABC')
class HuffmanTree:
  # Helper object for building the Huffman tree.
  # You may modify this constructor but the grading script rlies on the left, right, and symbol fields.
  class TreeNode:
    def __init__ (self):
      self.left = None
      self.right = None
      self.symbol = None
      self.min_element = None

  # The `symbol_list` argument should be a list of tuples `(symbol, weight)`,
  # where `symbol` is a symbol that can be encoded, and `weight` is the
  # the unnormalized probabilitiy of that symbol appearing.
  def __init__(self, symbol_list):
    assert(len(symbol_list) >= 2)
    # YOUR CODE HERE
    print("Input: ")
    print(symbol_list)
    #self.root = self.TreeNode() # (place TreeNode object here)
    sorted_list = sorted(symbol_list, key=lambda x: x[1])
    while (len(sorted_list) > 1):
        print("Sorted List...")
        print(sorted_list)
        #left_node = self.TreeNode()
        #right_node = self.TreeNode()
        
        first_elem = sorted_list.pop(0)
        print("elem 1:")
        print(first_elem)
        print("elem 2: ")
        second_elem = sorted_list.pop(0)
        print(second_elem)
        

        
        ### CONVERT ELEMENTS INTO NODES IF THEY AREN'T ALREADY
        if(isinstance(first_elem[0], self.TreeNode)):
            first_elem_node = first_elem[0]
        else:
            first_elem_node = self.TreeNode()
            first_elem_node.symbol = first_elem[0]
        
        if(isinstance(second_elem[0], self.TreeNode)):
            second_elem_node = second_elem[0]
        else:
            second_elem_node = self.TreeNode()
            second_elem_node.symbol = second_elem[0]
        
        ### COMPARE WEIGHTS TO DETERMINE LEFT AND RIGHT:
        first_elem_weight = first_elem[1]
        second_elem_weight = second_elem[1]
        if (first_elem_weight < second_elem_weight):
            left_node = first_elem_node
            right_node = second_elem_node
        elif (second_elem_weight < first_elem_weight): #THINK THIS IS UNNECESSARY BECAUSE THE LIST IS SORTED
            left_node = second_elem_node
            right_node = first_elem_node
        else: # HANDLE TIES, COME BACK TO THIS
            pass
        

        ### CREATE PARENT NODE AND SET ITS CHILDREN
        parent_node = self.TreeNode()
        parent_node.left = left_node
        parent_node.right = right_node
        
        ### STORE SEPARATE WEIGHT VARIABLE FOR PARENT NODE AS SUM OF CHILDREN
        parent_node_sum = first_elem_weight + second_elem_weight
        
        
        ## CREATE TUPLE FOR PARENT, WHERE ITS "VALUE" IS NOW THE NODE ITSELF
        parent_tuple = (parent_node, parent_node_sum)
        
        sorted_list.append(parent_tuple)
        
        ## RE-SORT LIST
        sorted_list = sorted(sorted_list, key=lambda x: x[1])
        
    self.root = sorted_list.pop(0)[0] #Root is equal to the final remaining treenode    
    print("Root Symbol:")
    print(self.root.symbol)
    print("Right Child Symbol:")
    print(self.root.right.symbol)
    print("Right Child's Left Child:")
    print(self.root.right.left)
    print("Right Child's Right Child:")
    print(self.root.right.right)
    print("Left Child Symbol:")
    print(self.root.left.symbol)
    print("Left Child's Left Child Symbol:")
    print(self.root.left.left.symbol)
    print("Left Child's Right Child Symbol:")
    print(self.root.left.right.symbol)
  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.
  def encode(self, s):
    assert(s is not None)
    # YOUR CODE HERE

  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self,s):
    assert(s is not None)
    # YOUR CODE HERE

l = "Tie-break 1;C,B,A;2,1,4;(C(AB));ABC;10110;010;CA"
l = l.strip()
(testname, symbols, weights, tree, encode_input, encode_output, decode_input, decode_output) = l.split(";")
decode_output = None if decode_output == '!' else decode_output
symbols = symbols.split(",")
weights = [int(w) for w in weights.split(",")]
h = HuffmanTree(list(zip(symbols, weights)))