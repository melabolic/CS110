
# **Question 1: Write python code to give the length of the longest common subsequence for two strings.**

dna = [[0,'TTCTACGGGGGGAGACCTTTACGAATCACACCGGTCTTCTTTGTTCTAGCCGCTCTTTTTCATCAGTTGCAGCTAGTGCATAATTGCTCACAAACGTATC'], 
       [1,'TCTACGGGGGGCGTCATTACGGAATCCACACAGGTCGTTATGTTCATCTGTCTCTTTTCACAGTTGCGGCTTGTGCATAATGCTCACGAACGTATC'], 
       [2,'TCTACGGGGGGCGTCTATTACGTCGCCAACAGGTCGTATGTTCATTGTCATCATTTTCATAGTTGCGGCCTGTGCGTGCTTACGAACGTATTCC'], 
       [3,'TCCTAACGGGTAGTGTCATACGGAATCGACACGAGGTCGTATCTTCAATTGTCTCTTCACAGTTGCGGCTGTCCATAAACGCGTCCCGAACGTTATG'],
       [4,'TATCAGTAGGGCATACTTGTACGACATTCCCCGGATAGCCACTTTTTTCCTACCCGTCTCTTTTTCTGACCCGTTCCAGCTGATAAGTCTGATGACTC'], 
       [5,'TAATCTATAGCATACTTTACGAACTACCCCGGTCCACGTTTTTCCTCGTCTTCTTTCGCTCGATAGCCATGGTAACTTCTACAAAGTTC'], 
       [6,'TATCATAGGGCATACTTTTACGAACTCCCCGGTGCACTTTTTTCCTACCGCTCTTTTTCGACTCGTTGCAGCCATGATAACTGCTACAAACTTC']]

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # initializing the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    #building the bottom-up table 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                #sets the first index as 0
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                #adds 1 to the sum of the previous row and column and stores
                #it to the current element if X and Y have 
                #the same alphabets at the same position
                L[i][j] = L[i-1][j-1]+1 
            else:
                #checks the row/column before the current elem. and store the max
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]

# **Question 2: Generate the table of the lengths of the longest common subsequences for every pair of strings.**

import tabulate
table = [[0 for i in range(7)]for i in range(7)]

for i in range(len(dna)):
    for j in range(len(dna)):
        #iterates through each pair and stores the lcs
        table[i][j] = lcs(dna[i][1],dna[j][1])
        
print"Longest Common Subsequence for every pair of strings:"
print(tabulate.tabulate(table, headers=('0','1','2','3','4','5','6'), tablefmt='fancy_grid', showindex="always"))


def editDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    # table to store results of subproblems
    dp_table = [[0 for x in range(n+1)] for x in range(m+1)]
    
    #filling in the table
    for i in range(m+1):
        for j in range(n+1):
            # If either string is empty, our edit distance =  
            # length of non-empty string
            if i == 0:
                dp_table[i][j] = j #when str1 has length 0
            elif j == 0:
                dp_table[i][j] = i #when str2 has length 0
 
            # If the last characters are same, look at the
            # previous characters instead
            elif str1[i-1] == str2[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
 
            # If last characters are different, consider all
            # possibilities and find minimum
            else:
                dp_table[i][j] = 1 + min(dp_table[i][j-1],    # Insert
                                         dp_table[i-1][j],    # Remove
                                         dp_table[i-1][j-1])  # Change 
    return dp_table[m][n]

#prints the editDistance values if LCS > 75:
def iterate(dna):
    for i in range(len(dna)):
        for j in range(i,len(dna)):
            if i == j:
                continue
            elif table[i][j] > 75:
                print "table[{}][{}] = {}".format(i, j, editDistance(dna[i][1], dna[j][1]))

iterate(dna)


# added here to make the reading experience a little more
# fluid for you, professor
table = [[0 for i in range(7)]for i in range(7)]

for i in range(len(dna)):
    for j in range(len(dna)):
        #iterates through each pair and stores the lcs
        table[i][j] = lcs(dna[i][1],dna[j][1])
        
def build_tree(table):
    parent = []
    children = []
    arr = []
    # appending the plausible parent-child relationships
    # into a new array
    for i in range(len(table)):
        for j in range(i,len(table)):
            if table[i][j] > 75:
                if i == j: continue
                else: arr.append([i,j])
                
    # checking for parent nodes
    for i in range(0,len(arr),2):
        for j in range(i+1, len(arr)):
            '''Checks the first value of an element in the 2-D array
            against another element. If it's the same, add
            the same value to the parent array, and the 
            extra elements into the children array.'''
            if arr[i][0] == arr[j][0]:
                parent.append(arr[j][0]) 
                children.append(arr[i][1]) 
                children.append(arr[j][1])
            '''Checks the second value of an element in the 2-D array
            against another element. If it's the same, add
            the same value to the parent array, and the 
            extra elements into the children array.'''
            if arr[i][1] == arr[j][1]:
                parent.append(arr[j][1])
                children.append(arr[i][0])
                children.append(arr[j][0])
           
    # combining the two list to form one ordered list
    for i in children:
        if i not in parent:
            parent.append(i)
    return parent
    
def print_tree(arr):
    i = 0
    check =[]
    while i < len(arr)//2:
        print "Parent: {}".format(arr[i])
        print "Children: {}, {}".format(arr[2*i+1], arr[2*i+2])
        i += 1

print_tree(build_tree(table))                

