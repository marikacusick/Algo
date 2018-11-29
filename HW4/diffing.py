# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, cost, s_char, t_char):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
  
    # YOUR CODE HERE
    if i==0 and j== 0:
        this_cost = 0
        cell_i = '-'
        cell_j = '-'

    elif i == 0:
        
        cell_i = '-'
        cell_j =t[j-1]
        prev = table.get(0,j-1).cost
        this_cost = prev + cost(cell_i, cell_j)

    #this_cost = 0
    elif j == 0:
        cell_i = s[i-1]
        cell_j = '-'
        prev = table.get(i-1,0).cost
        this_cost = prev + cost(cell_i, cell_j)
    #this_cost = 0
    else:
       
        prev_match = table.get(i-1,j-1).cost
        match = prev_match + cost(s[i-1], t[j-1])
        prev_delete = table.get(i-1,j).cost
        

        delete = prev_delete + cost(s[i-1], '-')
        prev_insert = table.get(i, j-1).cost

        insert = prev_insert + cost('-', t[j-1])

        this_cost = min(match, delete, insert)
       
        if match == min(match, delete, insert):
        
            cell_i =s[i-1]
            cell_j =t[j-1]
        elif delete == min(match, delete, insert):
            cell_i = s[i-1]
            cell_j = '-'
        else:
            cell_i = '-'
            cell_j = t[j-1]

    

    return DiffingCell(this_cost, cell_i, cell_j)

# Input: n and m, the sizes of s and t, respectively.
# Should return a list of (i,j) tuples, the order you would like us to call fill_cell
def cell_ordering(n,m):
    index_list = []
    for i in range(n+1):
        for j in range(m+1):
            this_index = (i,j)
            index_list.append(this_index)

    return index_list

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    align_s = ''
    align_t = ''
    
    
    i = len(s)
    j = len(t)
    fin_cost = table.get(i,j).cost
    go_diag = False
    go_left = False
    go_up = False
    
    while i>0 and j> 0:
    
        current_s = table.get(i,j).s_char
        current_t = table.get(i,j).t_char
        
        if current_s != '-' and current_t != '-':
            align_s = s[i-1]+ align_s
            align_t = t[j-1] + align_t
            i = i-1
            j = j-1
        
        elif current_s == '-' and current_t !='-':
            align_s = '-' + align_s
            align_t = t[j-1] + align_t
            j = j-1
            
        elif current_s != '-' and current_t == '-':
            align_s = s[i-1] + align_s
            align_t = '-' + align_t
            i = i-1
                   

    while j>0:
        align_s = '-' + align_s
        align_t = t[j-1] + align_t
        j= j-1

    while i>0:
        align_s = s[i-1]+ align_s
        align_t = '-' + align_t
        i = i - 1

    print (align_s)
    print (align_t)
    return (fin_cost, align_s, align_t)

# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
