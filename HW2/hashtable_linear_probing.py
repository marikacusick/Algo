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
      
    if (key== None or value == None):
        print("key or value cannot be none")
        return
    
    hash_pos = cs5112_hash1(key) % self.array_size
    val = tuple((key, value))
    
    content = self._get_array().get(hash_pos)
    
    #if there is no item in this hash position, then set the value to that position
    if content == None:
        print ("inserted" + str(val) + " into position " + str(hash_pos))
        self._get_array().set(hash_pos,val)
    
        self.item_count = self.item_count + 1
        print ("added a value, count is now " + str(self.item_count))
        
        if float(self.size())/float(self.array_size) > self.load_factor:
            print ("need to resize array")
            self._resize_array()
    
    else:
        
        #does this key already exisit in the array?
        idx_of_key = -1
        for i in range(self.array_size):
            tup = (self._get_array().get(i))
            if tup is not None:
                if tup[0] == key:
                    idx_of_key = i
    
        #if this key exists, replace it with this value
        if (idx_of_key != -1):
            print ("Replaced " + str(self._get_array().get(idx_of_key)[1] + " with " +
                                     str(value) + " into position " + str(idx_of_key)))
            self._get_array().set(idx_of_key, val)
            print ("did not need to add to array, so the size is: " + str(self.item_count))
        
        #if not, there is a collision, and we need to check the next possible position
        else:
        
            print ("Collision")
            next_spot = self.rehash(hash_pos, self.array_size)
            print ("trying " + str(next_spot))
    
            while self._get_array().get(next_spot) != None:
                next_spot = self.rehash(next_spot, self.array_size)
                print ("trying " + str(next_spot))
        
            if self._get_array().get(next_spot)== None:
                print ("inserted" + str(val) + " into position " + str(next_spot))
                self._get_array().set(next_spot, val)
    
            self.item_count = self.item_count + 1
            print ("added a value, count is now " + str(self.item_count))
    
            if float(self.size())/float(self.array_size) > self.load_factor:
                print ("need to resize array")
                self._resize_array()

        
  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
      
    if (key == None):
        print ("key cannot be none")
        return
      
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
      
    if (key == None):
        print ("key cannot be none")
        return
      
    pos = self.find(key)
    if pos == None:
          return None
    else:
        val = self._get_array().get(pos)[1]
        self._get_array().set(pos, None)
        self.item_count = self.item_count - 1
        print ("removed item, the count is now " + str(self.item_count))
        return val

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
  
    new_length = self.array_size*2
    self.item_count = 0
    old_arr = self._get_array()
    self.array = FixedSizeArray(new_length)
    self.array_size = new_length
    
    for i in range(old_arr.size):
        if old_arr.get(i) is not None:
            val = old_arr.get(i)
            self.insert(val[0], val[1])

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array
  
#Internal helper to rehash
  def rehash(self, old_pos, size):
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
              hash_pos = self.rehash(hash_pos, self.array_size)
              if self._get_array().get(hash_pos) is None:
                  return None
              if hash_pos == pos_save:
                  raise Exception ("this is wrong")
          return hash_pos



