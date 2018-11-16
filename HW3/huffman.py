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

    def custom_sort(symbol_weight_pair):
        primary_sorter = symbol_weight_pair[1] #always sort by weight first
        if(isinstance(symbol_weight_pair[0], self.TreeNode)):
            secondary_sorter = symbol_weight_pair[0].min_element
        else:
            secondary_sorter = symbol_weight_pair[0]
        
        return (primary_sorter, secondary_sorter)
    
    sorted_list = sorted(symbol_list, key=lambda x: custom_sort(x))
    while (len(sorted_list) > 1):
        
        #print (sorted_list)
        
        first_elem = sorted_list.pop(0)
        second_elem = sorted_list.pop(0)
        
                
        ### CONVERT ELEMENTS INTO NODES IF THEY AREN'T ALREADY
        if(isinstance(first_elem[0], self.TreeNode)):
            first_elem_node = first_elem[0]
        else:
            first_elem_node = self.TreeNode()
            first_elem_node.symbol = first_elem[0]
            first_elem_node.min_element = first_elem[0]
        
        if(isinstance(second_elem[0], self.TreeNode)):
            second_elem_node = second_elem[0]
        else:
            second_elem_node = self.TreeNode()
            second_elem_node.symbol = second_elem[0]
            second_elem_node.min_element = second_elem[0]
        
        ### COMPARE WEIGHTS TO DETERMINE LEFT AND RIGHT:
        first_elem_weight = first_elem[1]
        second_elem_weight = second_elem[1]
        if (first_elem_weight < second_elem_weight):
            left_node = first_elem_node
            right_node = second_elem_node
        elif (second_elem_weight < first_elem_weight): #THINK THIS IS UNNECESSARY BECAUSE THE LIST IS SORTED
            left_node = second_elem_node
            right_node = first_elem_node
        else: # HANDLE TIES IN WEIGHTS            
            if (first_elem_node.min_element < second_elem_node.min_element):
                left_node = first_elem_node
                right_node = second_elem_node
            else: #because all characters are distinct, there cannot be ties
                left_node = second_elem_node
                right_node = first_elem_node

        ### CREATE PARENT NODE AND SET ITS CHILDREN
        parent_node = self.TreeNode()
        parent_node.left = left_node
        parent_node.right = right_node
        
        #SET min element based on left and right
        parent_node.min_element = min(left_node.min_element, right_node.min_element)
        
        
        
        ### STORE SEPARATE WEIGHT VARIABLE FOR PARENT NODE AS SUM OF CHILDREN
        parent_node_sum = first_elem_weight + second_elem_weight
        
        
        ## CREATE TUPLE FOR PARENT, WHERE ITS "VALUE" IS NOW THE NODE ITSELF
        parent_tuple = (parent_node, parent_node_sum)
        
        sorted_list.append(parent_tuple)
        
        ## RE-SORT LIST
        sorted_list = sorted(sorted_list, key=lambda x: custom_sort(x))
        
    self.root = sorted_list.pop(0)[0] #Root is equal to the final remaining treenode    

  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.
  def encode(self, s):
    assert(s is not None)

    root = self.root
    this_dict = dict()
    
    def recurse_code(root, string, this_dict):

        if root.left == None and root.right == None and root.symbol!=None:
            
            this_dict[root.symbol] = string
            
            return
  
  
        recurse_code(root.left, string + "0", this_dict)
        recurse_code(root.right, string + "1", this_dict)
              
    recurse_code(root, "", this_dict)
  
    output = ""
    for char in s:
        output = output + this_dict[char]
    
    
    return output
  

  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self,s):

    string = ""
    if len(s)  <= 0:
        return string
    current = self.root
    for i in range(len(s)):

        if s[i] == "0":
            current = current.left
        if s[i] == "1":
            current = current.right

        if current.left == None and current.right == None and current.symbol!=None:
            string = string + current.symbol
            current = self.root
        
    if len(string) == 0:
        string = None
    elif self.encode(string)!= s:
        string = None


    return string



