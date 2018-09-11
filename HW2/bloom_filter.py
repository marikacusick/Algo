# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # Adds an element to the bloom filter using three hash functions.
  def add_elem(self, elem):    
    index_to_add_h1 = cs5112_hash1(elem) % self.size
    self.array.set(index_to_add_h1, True)
        
    index_to_add_h2 = cs5112_hash2(elem) % self.size
    self.array.set(index_to_add_h2, True)
       
    index_to_add_h3 = cs5112_hash3(elem) % self.size
    self.array.set(index_to_add_h3, True)
    
    return
    
    raise NotImplementedError
    

  # Returns False if the given element is was definitely not added to the
  # filter. Returns True if it's possible that the element was added to the
  # filter (but not necessarily certain).
  def check_membership(self, elem):
    index_h1 = cs5112_hash1(elem) % self.size
    index_h2 = cs5112_hash2(elem) % self.size
    index_h3 = cs5112_hash3(elem) % self.size
    
    return(self.array.get(index_h1) and self.array.get(index_h2) and self.array.get(index_h3))

    raise NotImplementedError
