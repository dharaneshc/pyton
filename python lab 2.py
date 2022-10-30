#!/usr/bin/env python
# coding: utf-8

# In[18]:


a=int(input('enter the number'))
if(a%2==0):
 print("the number is even")
else:
 print("the number is odd")


# In[61]:


a=int(input('enter the number'))
if(a>0):
 print('number is positive')
elif(a<0):
    print('number is negetive')
else:
    print("number is zero")


# In[40]:


a=int(input('enter the number'))

if(a>=0):
    if(a>0):
        print('number is positive' )
    else:
        print('zero')
else:
    print('number is negative')


# In[54]:


a=int(input('enter the number'))
b=int(input('enter the number2'))
c=int(input('enter the number3'))
if a>b and a>c:
    if b>a and b>c:
        print("a is bigger")
    else:   
        print("b is bigger")
else:
    print("c is bigger")
        


# In[1]:


i=0
while i<=100:
    if (i%4!=0) and (i%7!=0):
        print(i)
    i+=1


# In[2]:


n=int(input("enter the n value"))
sum1 = 0
while(n>0):
    sum1=sum1+n
    n=n-1
print("the sum of n number is",sum1)    


# In[9]:


i=0
while i<=100:
    print(i)
    i=i+2


# In[17]:


i=1
while i<=100:
    print(i)
    i=i+2


# In[18]:


lower = 0
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[25]:


rows = 4
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')


# In[20]:


rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')


# In[ ]:




