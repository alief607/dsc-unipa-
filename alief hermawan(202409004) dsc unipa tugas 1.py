#!/usr/bin/env python
# coding: utf-8

# In[1]:


var1=[1,2,3,4]


# In[2]:


type(var1)


# In[3]:


len(var1)


# In[4]:


first=[11.25,18.0,20]
second=[10.75,9.50]


# In[5]:


full=first+second


# In[6]:


print(full)


# In[7]:


sorted(full)


# In[8]:


full_sorted=sorted(full, reverse=True)


# In[9]:


print(full_sorted)


# In[10]:


area=[11.25,18.00,20.00,10.75,9.50]


# In[11]:


print(area.index(20.00))


# In[12]:


print(area[2])


# In[13]:


print(area.count(14.5))


# In[14]:


area.append(24.5)


# In[15]:


area.append(15.45)


# In[16]:


print(area)


# In[17]:


sorted(area, reverse=True)


# In[18]:


print(area)


# In[26]:


r = float(input("Masukkan panjang jari-jari lingkaran: "))


# In[27]:


phi=3.14


# In[28]:


keliling=2*phi*r


# In[29]:


keliling


# In[30]:


luas=phi*(r*r)


# In[31]:


print(luas)


# In[34]:


area_3=["hallaw",11.25,"kitchen",18.0,"chill zone",20.0,"bathroom",10.50,"poolhouse",24.5,"garage",15.45]


# In[36]:


del area_3[9:12]


# In[39]:


print(area_3)


# In[40]:


area_4=["hallway",11.25,"kitchen",18.0,"living room",20.0,"badroom",10.75,"bathroom",9.50]


# In[42]:


print(area_4.index("bathroom"))


# In[43]:


print(area_4[8])


# In[44]:


area_4[8]=10.8


# In[45]:


print(area_4)


# In[46]:


print(area_4.index("living room"))


# In[48]:


print(area_4[4])


# In[49]:


area_4[4]="ruang tamu"


# In[50]:


print(area_4)


# In[ ]:




