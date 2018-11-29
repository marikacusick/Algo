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
    return RespaceTableCell(False, None)

        
        
    #if (row == 0):
     #   return RespaceTableCell(True, 0)
    #if (row > col):
    #    cellAbove = T.get(row-1, col)
    #    return RespaceTableCell(cellAbove.value, cellAbove.index)
    
    
    #if(is_word(sub_string)):
    #    sub_string_length = len(sub_string)
    #    whole_string_length = len(string)
    #    jump_ahead = whole_string_length - sub_string_length
    #    return RespaceTableCell(True, jump_ahead)

    

                  
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
    s = "itwasi"
    wordlist = ["i", "it", "was", "as", "a"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    print(D)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)
