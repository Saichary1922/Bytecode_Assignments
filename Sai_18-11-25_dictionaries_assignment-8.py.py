#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1:Creating and Accessing Dictionaries
#Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
d1={x:x*x for x in range(1,11)}
print(d1)


# In[2]:


#2: Accessing Dictionary Elements
#Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
print("value of the key 5 is:",d1[5])
print("keys of the dictionary are:")
for k in d1:
    print(k)


# In[3]:


#Qno 3: Dictionary Methods
#Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
d1.update({11:121})
d1.pop(1)
d1


# In[4]:


#Qno 4: Iterating Over Dictionaries
#Iterate over the dictionary created in Assignment 1 and print each key-value pair.
d1={x:x*x for x in range(1,11)}
for k in d1:
    print(k,"=",d1.get(k))


# In[5]:


#Qno 5: Dictionary Comprehensions
#Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
d2={x:x*x*x for x in range(1,11)}
print(d2)


# In[6]:


#Qno 6: Merging Dictionaries
#Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
d1={x:x*x for x in range(1,6)}
d2={x:x*x for x in range(6,11)}
d1.update(d2)
print(d1)


# In[7]:


#Qno 7: Nested Dictionaries
#Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.
d1={"name":"Sai","age":22,"grades":{"math":"A","science":"B","english":"A"}}
d1["grades"]


# In[8]:


#Qno 8: Dictionary of Lists
#Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary
d1={x:[x*i for i in range(1,6)] for x in range(1,6)}
print(d1)


# In[10]:


#Qno 9: Dictionary of Tuples
#Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
d1={x:tuple(x*i for i in range(1,6)) for x in range(1,6)}
print(d1)


# In[11]:


#Qno 10: Dictionary and List Conversion
#Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
d1={x:x*x for x in range(1,6)}
d2=list(d1.items())
d2


# In[13]:


#Qno 11: Dictionary Filtering
#Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
d1={x:x*x for x in range(1,11) if x%2==0}
d1


# In[14]:


#Qno 12: Dictionary Key and Value Transformation
#Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.
d1={x:x*x for x in range(1,6)}
d2={x*x:x for x in d1.items()}
print(d2)


# In[15]:


#Qno 13: Default Dictionary
#Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.
keys={1,2,3}
values=[]
d1=dict.fromkeys(keys,values)
print(d1)
d1[1]=10
d1[2]="hello"
d1[3]=15
print(d1)


# In[22]:


#Qno 14: Counting with Dictionaries
#Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
s=input("enter a string")
def deffun(s):
    d=dict()
    for i in s:
        d.update({i:s.count(i)})
    return d


# In[23]:


#Qno 15: Dictionary and JSON
#Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.
d1={"title":"python","author":"van","year":1990,"genre":"Technical"}
d1


# In[ ]:




