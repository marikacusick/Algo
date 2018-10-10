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
    self.root = None # (place TreeNode object here)

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
