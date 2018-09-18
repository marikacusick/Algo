# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("chaining", HashTableChaining), ("linear probing", HashTableProbing)]:
#for (name, HashTable) in [("linear probing", HashTableProbing)]:
    table = HashTable()
    table.insert("example_key", "example_value")

    table.insert("A", "dog")
    table.insert("B", "cat")
    table.insert("A" , "giraffe")
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


    if table.get("example_key") != "example_value":
        print("%s hash table did not return example value"%name)

#this returns dog, is there a way to return giraffe? Do you have to make sure that the keys are unique?
    print (table.get("A")) #should return giraffe
    print(table.get("Z")) # should return None

    table.remove("example_key")
    if table.size() != 0:
        print("%s hash table had non-zero size"%name)
        print ("table size is " + str(table.size()))
