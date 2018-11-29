# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #YOUR CODE HERE
    sub_string = string[i:j+1]
    sub_string_is_word = is_word(sub_string)

    if sub_string_is_word:
        return RespaceTableCell(True, None)
    else:
        if len(sub_string) == 1: # no way to look elsewhere
            return RespaceTableCell(False, None)
        else:
            for split_point in range(i,j):
                cell_left = T.get(i, split_point)
                cell_below = T.get(split_point+1, j)
                
                if (cell_left.value and cell_below.value):
                    return RespaceTableCell(True, split_point)
            
            return RespaceTableCell(False, None) #no valid splits

    
    

                 
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    #YOUR CODE HERE
    #Do 0,0 --> 1,1 --> 2,2 --> 3,3 --> 4,4 --> 5,5
    # -->
    
    print(N)
    cellOrderArr = []
    i = 0
    j = 0
    start_j = 0
    while(True):
        if (start_j > N-1):
            break
        cellOrderArr.append((i,j))
        if (j == N-1):
            i = 0
            start_j += 1
            j = start_j
        else:
            i += 1
            j += 1
        
    
    print(cellOrderArr)
    return cellOrderArr

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    #YOUR CODE HERE
    #N = len(s) 
    #i = 0
    #j = 0
    #start_j = 0
    #while(True):
        #if (start_j > N-1):
            #break
        #print(str(i)+","+str(j))
        #cell = table.get(i,j)
        #print(cell)
        #if (j == N-1):
            #i = 0
            #start_j += 1
            #j = start_j
        #else:
            #i += 1
            #j += 1
    
    
    top_right_cell = table.get(0,len(s)-1)
    print(top_right_cell)
    return None


if __name__ == "__main__":
    # Example usage.
    #from dynamic_programming import DynamicProgramTable
    #s = "itwasthebestoftimes"
    #wordlist = ["of", "it", "the", "best", "times", "was"]
    #D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    #print(D)
    #D.fill(string=s, is_word=lambda w:w in wordlist)
    #print respace_from_table(s, D)
    
    from dynamic_programming import DynamicProgramTable
    s = "iamace"
    wordlist = ["i", "a", "am", "ace"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    print(D)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)
