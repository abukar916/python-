import csv

#define each logic gate in its own function

def buffer_func (A):
   return A
    
def not_func (A):
    if A != 1 : 
        return 1
    else :
        return 0
    
def and_func (A,B):
    if A == 1 and B== 1 :
        return 1
    else :
        return 0

def or_func (A,B):
    if A== 1:
        return 1
    elif B == 1:
        return 1
    else :
        return 0
    
def nand_func (A,B):
    if A == 1 and B==1 :
        return 0
    else :
        return 1

def nor_func (A,B):
   if A== 1:
       return 0
   elif B == 1:
       return 0
   else :
       return 1
   
    
def xor_func (A,B):
    return and_func (or_func(A, B), nand_func(A, B))

#define the xnor function without using conditionals
    
def xnor_func (A,B) :
    return or_func (and_func(A, B), nor_func(A, B))
   
 #Read the values in the csv file   
with open ('truth_table.csv', newline= '') as csvfile:
    csv_reader = csv.reader(csvfile)
    next (csv_reader)
    
#convert the string values in the the csv file to integers using list comprehension
    
    convert_int = [[int(digit) for digit in row] for row in csv_reader] 
    for row in convert_int:
        A, B = (row[0]), (row[1])
# Get expected output values from truth table
        real_and = (row[2])
        real_or = (row[3])
        real_nand = (row[4])
        real_nor = (row[5])
        real_xor = (row[6])
        real_xnor = (row[7])
#Test each logic gate function against the values in the csv file


        assert and_func(A, B) ==  real_and
        assert or_func(A, B) == real_or
        assert nand_func(A, B) == real_nand
        assert nor_func(A, B) == real_nor
        assert xor_func(A, B) == real_xor
        assert xnor_func(A, B) == real_xnor
        assert buffer_func(A) == A
        assert not_func(A) == (not A)
        
        
print('correct logic functions')        
        
        
      
        

