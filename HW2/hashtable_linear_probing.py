# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    hash_pos = cs5112_hash1(key) % self.array_size
    
    
    val = tuple((key, value))
    
    #if there is no item in this hash position, then set the value to that position
    if self._get_array().get(hash_pos) == None:
        self._get_array().set(hash_pos,val)
    
    #if there is another value in the hash position, we must rehash in order to get to the next position
    else:
        print ("Collision")
        next_spot = rehash(hash_pos, self.array_size)
    
        while self._get_array().get(next_spot) != None:
            next_spot = rehash(next_spot, self.array_size)

        if self._get_array().get(next_spot)== None:
            self._get_array().set(hash_pos, val)

    self.item_count = self.item_count + 1
    
    if float(self.size())/float(self.array_size) > self.load_factor:
        self._resize_array()

    #there needs to be a way to resize the array here after a certain number of additions
    
    #raise NotImplementedError()
        
  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
      
    pos = self.find(key)
    if pos == None:
        return None
    else:
        return self._get_array().get(pos)[1]

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
  
    pos = self.find(key)
    if pos == None:
          return None
    else:
        val = self._get_array().get(pos)[1]
        self._get_array().set(pos, None)
        return val
    
    #raise NotImplementedError()

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count
  #raise NotImplementedError()

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
  
    new_length = self.array_size*2
    #self.item_count = 0
    old_arr = self._get_array()
    self.array = FixedSizeArray(new_length)
    for i in range(self.array_size):
        if old_arr.get(i) is not None:
            self._get_array().set(i, old_arr.get(i))

  
    #raise NotImplementedError()

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array
  
#Internal helper to rehash
  def rehash(old_pos, size):
      return (old_pos + 1) % size

# helper function to get the index
  def find(self, key):
      hash_pos = cs5112_hash1(key) % self.array_size
      if self._get_array().get(hash_pos) is None:
          return None
      if self._get_array().get(hash_pos)[0] == key:
          return hash_pos
      if self._get_array().get(hash_pos)[0]!=key:
          pos_save = hash_pos
          while self._get_array().get(hash_pos)[0]!=key:
              hash_pos = rehash(hash_pos, self.array_size)
              if self._get_array().get(hash_pos) is None:
                  return None
              if hash_pos == pos_save:
                  raise Exception ("this is wrong")
          return hash_pos



