#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install matplotlib


# In[5]:


import matplotlib.pyplot as plt


# In[23]:


sales_data = {
    "January": [12000, 15000],
    "February": [13000, 16000],
    "March": [14000, 17000],
    "April": [15000, 27000],
    "May": [12000, 19000],
    "June": [17000, 16000],
    "July": [18000, 21000],
    "August": [16000, 22000],
    "September": [12000, 20000],
    "October": [21000, 24000],
    "November": [22000, 25000],
    "December": [23000, 26000]

}


# In[24]:


months = list(sales_data.keys())
product_a_sales = [sale[0] for sale in sales_data.values()]
product_b_sales = [sale[1] for sale in sales_data.values()]


# In[25]:


width = 0.35
x = range(len(months))


# In[26]:


fig, ax = plt.subplots()
bar1 = ax.bar(x, product_a_sales, width, label='Product A')
bar2 = ax.bar([i + width for i in x], product_b_sales,width, label='Product B')
ax.set_title('Monthly Sale Comparison')

ax.legend()
plt.show()


# In[27]:


total_sales = [sum(sales) for sales in zip(product_a_sales, product_b_sales)] 

fig, ax2 = plt.subplots() 
ax2.plot(months, total_sales, marker='o', linestyle='-', color='purple', label='Total Sales')

ax2.set_title('Total Sales Trend')
ax2.set_xlabel('Months') 
ax2.set_ylabel('Total Sales in Dollars') 
               
ax2.legend() 

plt.xticks(rotation=45) 
               
plt.show()               


# In[ ]:





# In[ ]:




