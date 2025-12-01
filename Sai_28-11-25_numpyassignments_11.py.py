#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment 1: Array Creation and Manipulation
# Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
# Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
print('==array of shape (5, 5) filled with random integers between 1 and 20==')
import numpy as np
import random 
a=np.random.randint(1,20,[5,5])
print(a)
print('==Replacing all the elements in the third column with 1.==')
a[:,2]=1
print(a)
# Create a NumPy array of shape (4, 4) with values from 1 to 16. 
print('==array of shape (4,4) filled with values from 1 and 16 ')
b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(b)
#Replace the diagonal elements with 0.
print('==Replacing the diagonal elements with 0.==')
for i in range(0,4):
    for j in range(0,4):
        if i==j:
            b[i][j]=0
print(b)


# In[2]:


# Assignment 2: Array Indexing and Slicing
# Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
# Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
import numpy as np
a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]])
print(a)
for i in range(0,6):
    for j in range(0,6):
        print(a(3:5))


# In[3]:


# Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
a=np.random.randint(1,10,[5,5])
print(a)
print(a[0],a[3])


# In[4]:


# ### Assignment 3: Array Operations
# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, and division.
print("==First numpy array==")
a=np.random.randint(1,10,[3,4])
print(a)
print("==Second numpy array==")
b=np.random.randint(1,10,[3,4])
print(b)
print("Addition of two numpy arrays are:")
print(a+b)
print("Subtraction of two numpy arrays are:")
print(a-b)
print("multiplication of two numpy arrays are:")
print(a*b)
print("division of two numpy arrays are:")
print(a//b)


# In[5]:


# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(b)
sum1=0
sum2=0
for i in range(0,4):
    for j in range(0,4):
        sum1+=b[i]
    print(sum1)
    sum2+=b[j]
print(sum2)


# In[ ]:




