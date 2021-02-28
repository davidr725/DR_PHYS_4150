# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:38:22 2021

@author: david
"""
import numpy as np

#create the matrix
node1 = [4,-1,-1,-1,5]
node2 = [-1,3,0,-1,5]
node3 = [-1,0,3,-1,0]
node4 = [-1,-1,-1,4,0]
matrix = np.array([node1,node2,node3,node4], dtype = float)


#This function does not work with misbehaving 0s.
#n = number of rows in the matrix
def gaussian_elimination(n):

#Loop Counters    
    a = 0    
    b = 1
    x = 0

#Top level Loop: Repeats Loop 1 and 2 and the loop counter increases until the entire matrix is an upper triangle.
    for i in range(a,n):

#Nested Loop 1: Takes the first non-zero element of every row and divides all the subsequent elements in the row by it
#Example: for a 1x4 matrix [0,5,10,15] it would divide 5/5, 15/5, 20,5 and change the matrix row to [0,1,2,3]. 
#The objective of this loop is to make the first non-zero element of the row 1
        for j in range(a,n):
            matrix[j,a:n+1] /= matrix[j,x]
            
#Nested Loop 2: Builds the upper triangle by subtracting a row from the following row
#Example: for a 2x4 matrix [[1,2,3],[1,4,6]] where Loop 1 already made all the first non-zero elements of each row 1
#we subtract the row row0 from row1: [1,4,6] - [1,2,3] = [0,2,3]. Row1 is now [0,2,3]
        for k in range(b,n):
            matrix[k] -= matrix[x]
        
        a += 1
        b += 1
        x += 1

#Split the Answer Vector from the System of Equations Matrix
    vector = np.copy(matrix[:,n])
    final_matrix = np.delete(matrix, n, axis=1)
    v4 = vector[3] 
    v3 = vector[2] + (-matrix[2,3]*v4)
    v2 = vector[1] + (-matrix[1,3]*v4 -matrix[1,2]*v3)
    v1 = vector[0] + (-matrix[0,3]*v4 -matrix[0,2]*v3 -matrix[0,1]*v2)
    
    print("The matrix in reduced row form is: ")
    print(str(final_matrix))
    print("")
    print("The final answer vector is: ")
    print(str(vector))
    print("")
    print("The values of the voltages are: ")
    print(f'v1 is {v1:.2f} ', f' v2 is {v2:.2f} ', f' v3 is {v3:.2f} ', f' v4 is {v4:.2f} ')

gaussian_elimination(4)






            
