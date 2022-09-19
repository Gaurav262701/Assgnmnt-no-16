#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Answer no 1
def stutters(word):
    for i in word:
        print(word[:2],"..",word[:2],"..",word)
word = input(":")
print(stutters(word))


# In[5]:


#Answer no 2
def radians_to_degrees(num):
    while(num==0):
        deg=num*57.2758
        print(deg)
        break
num = float(input())
print(radians_to_degrees(1))


# In[ ]:


#Answer no 3
def is_curzon(num):
    while(num!=0):
        cal=2**num+1
        cal1=2*num+1
        if(cal%cal1==0):
            print("multiple")
            break
num = int(input(":"))
print(is_curzon(num))


# In[2]:


#Answer no 4
def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A')+10
def toDeci(str,base):
    llen = len(str)
    power = 1 
    num = 0
    for i in range(llen-1,-1,-1):
        if val(str[i]) >= base:
            print('Invalid number')
            return -1
        num += val(str[i])*power
        power = power * base
    return num 
strr = "11A"
base = 16
print("Decimal equivalent of",strr,'in base',base,'is',toDeci(strr,base))


# In[ ]:




