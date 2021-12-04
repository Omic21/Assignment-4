#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Square the elements of the list


def square(num1):
    return num1**2

sample_list = [4, 5, 2, 9]

result = list(map(square,sample_list))
print("Output = ", result)


# In[2]:


# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

input = lambda x : x+25
print('Output = ', input(10))


# In[4]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map.

def fun(n):
    return (n*3)

list(map(fun,[1,3,4,5,6,9]))


# In[ ]:




