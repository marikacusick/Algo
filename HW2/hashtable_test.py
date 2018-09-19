# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("chaining", HashTableChaining), ("linear probing", HashTableProbing)]:
#for (name, HashTable) in [("linear probing", HashTableProbing)]:
    table = HashTable()

    table.insert("A", "dog")
    table.insert("B", "cat")
    table.insert("A" , "giraffe")
    print(table.size() == 2) 
    table.insert("C", "fly")
    table.insert("D", "mosquito")
    table.insert("E", "horse")
    table.insert("F", "eagle")
    table.insert("G", "bird")
    table.insert("H", "bison")
    table.insert("I", "boar")
    table.insert("J", "butterfly")
    table.insert("K", "ant")
    table.insert("L", "anaconda")
    table.insert("M", "bear")
    table.insert("N", "chicken")
    table.insert("O", "dolphin")
    print(table.size() == 15)


#this returns dog, is there a way to return giraffe? Do you have to make sure that the keys are unique?
    print (table.get("A")) #should return giraffe
       
    print(table.get("Z")) # should return None
    
    ## TEST THE REMOVE FUNCTION
    print(table.remove("Z")) # should return None because Z was never inserted
    print(table.size() == 15) #should still be 15 because nothing was removed
    print(table.remove("E")) #should return horse
    print(table.size() == 14) #should now be 14 because an item was removed
    print(table.get("E")) # should return None now that E is removed

    
    print(table.remove("A")) #should return giraffe
    print(table.get("A")) # should return None now that A is removed
    
    if table.size() != 0:
        print("%s hash table had non-zero size"%name)
        print ("table size is " + str(table.size()))
