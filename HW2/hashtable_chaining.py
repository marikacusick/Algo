# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

class SingleLinkedList:  
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return
    def add_list_item(self, item):
        "add an item at the end of the list"

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return
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
    # YOUR CODE HERE
    if (key == None or value == None):
        raise Exception ("key or value cannot be none")
   
    hash_slot = cs5112_hash1(key) % self.array_size
    print("Hash Position = " + str(hash_slot))
    key_val = tuple((key, value))
    
    content_in_slot =  self._get_array().get(hash_slot) ## IS THIS A POINTER OR CAN I MODIFY DIRECTLY??
    
    print(key_val)
    #if there is no item in this hash position, then set the value to that position
    if content_in_slot == None:
        print ("inserted " + str(key_val) + " into position " + str(hash_slot))
        nested_list = SingleLinkedList()
        new_node = SLLNode(key_val)
        nested_list.head = new_node
        self.item_count = self.item_count + 1        
        self._get_array().set(hash_slot,nested_list)
    
    #if it's not None at position, then explore the linked list at that position
        # if key is already in the linked list, replace that node with new (key, value)
        # if not, append (key, value) to linked list
    else:                
        cur_node = content_in_slot.head
        while (cur_node != None):
            if (cur_node.get_value()[0] == key):
                print("Replaced " + str(cur_node.get_value()) + " with " + str(key_val) + " in nested list at position "+str(hash_slot)) 
                cur_node.set_value(key_val)
                break
            if (cur_node.get_next() == None):
                new_node = SLLNode(key_val)
                cur_node.set_next(new_node)
                
                self.item_count = self.item_count + 1
                print("Appending " + str(key_val) + " to list at position " + str(hash_slot))
                break
            
            cur_node = cur_node.get_next()
        
        self._get_array().set(hash_slot,content_in_slot) 
    
    if float(self.size())/float(self.array_size) > self.load_factor:
        print ("need to resize array")
        self._resize_array()
    

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # YOUR CODE HERE
    if (key == None):
        raise Exception ("key cannot be none")
    
    hash_slot = cs5112_hash1(key) % self.array_size
    content_in_slot = self._get_array().get(hash_slot)
    
    if (content_in_slot == None):
        return content_in_slot   
    else:
        cur_node = content_in_slot.head
        
        while(cur_node != None):
            if (cur_node.get_value()[0] == key):
                return cur_node.get_value()[1]
            cur_node = cur_node.get_next()
        
        return None # return None if key not found at this position

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # YOUR CODE HERE
    if (key == None):
         raise Exception ("key cannot be none")
    
    hash_slot = cs5112_hash1(key) % self.array_size
    content_in_slot = self._get_array().get(hash_slot)
    
    if (content_in_slot == None):
        return content_in_slot
    else:
        cur_node = content_in_slot.head
        prev_node = None

        while (cur_node != None):
            if (cur_node.get_value()[0] == key):
                if (prev_node != None):
                    prev_node.set_next(cur_node.get_next())  ## HOW DO I ALTER THE ORIGINAL LINKED LIST?
                else:
                    content_in_slot.head = cur_node.get_next()
                
                self.item_count = self.item_count - 1
                self._get_array().set(hash_slot,content_in_slot)
                return cur_node.get_value()[1]
            
            prev_node = cur_node
            cur_node = cur_node.get_next()

        return None
        
        

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
            cur_node = val.head
            while(cur_node != None):
                kv = cur_node.get_value()
                k = kv[0]
                v = kv[1]
                self.insert(k, v)
                cur_node = cur_node.get_next()
            

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array
