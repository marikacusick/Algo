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
    row = i
    col = j
    
    if (col == len(string)): ## you're in the 'special' column
        cell_to_left = T.get(i, j-1)
        if (cell_to_left.index > 0):
            return RespaceTableCell(True, cell_to_left.index)
        else:
            return RespaceTableCell(False, 0)
    else:
        sub_string = string[row:col+1]
        sub_string_isword = is_word(sub_string)
       
        if (sub_string_isword):
            return RespaceTableCell(True, len(sub_string))
        else:
            if (row == col): # You are at the beginning of the row, so no cell to the left
                return RespaceTableCell(False, 0)
            else:
                cell_to_left = T.get(i, j-1)
                return RespaceTableCell(False, cell_to_left.index)

        
        
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
    #Do 0,0 --> 0,1 --> 0,2 --> 0,3 --> 0,4 --> 0,5
        #--> 1,1, 1,2 .....
        #--> 2,2, 2,3
    cellOrderArr = []
    for i in range(N):
        for j in range(N+1):         
            if (i > j):
                continue
            else:
                #print(str(i) + "," + str(j))
                cell = (i, j)
                cellOrderArr.append(cell)
    
    print(cellOrderArr)
    return cellOrderArr

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    #YOUR CODE HERE
    num_rows = len(s) + 1
    num_cols = len(s) + 1
    
    for i in range(len(s)):
        for j in range(len(s)+1):         
            if (i > j):
                continue
            else:
                print(str(i) + "," + str(j))
                print(table.get(i,j))
    
    print("......................................")
    
    def recurse_through(table, row, col_to_check):
        print("next cell.............")
        print(row, col_to_check)
        most_true = 0
        for (row_index) in range(row-1, -1, -1):
            cell = table.get(row_index, col_to_check)
            if (cell.value and cell.index > most_true):
                most_true = cell.index
                
        print(most_true)
        
        #if (not next_cell.value):
            #return
    
    last_col = len(s)
    last_row = len(s) - 1
    
    for row_index in range(last_row, -1, -1):
        respaced_string = ""
        special_cell = table.get(row_index, last_col)
        print("Special cell.....")
        print(special_cell)
        if (not special_cell.value):
            continue
        else:
            jump_to_col = last_col - (special_cell.index + 1)
            recurse_through(table, row_index, jump_to_col)
    
    
    final_sentence = ""
            
    # start at (last_row - 1), last_col
        #if curCell.value is TRUE (if there is a word that STARTS with the letter corresponding with this row)
            # check if last_col - (curCell.index + 1) is true
                # if it's false, snap back
                # if it's true, keep going    
               
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
