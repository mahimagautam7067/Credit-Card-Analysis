#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing all required libraries
import pandas as pd                                 # Importing pandas
import numpy as np                                  # Importing numpy
import matplotlib.pyplot as plt                     # Importing matplotlib for visualization
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns                               # Importing seaborn for visualization
plt.rcParams["figure.figsize"] = (14,8)
sns.set_style('darkgrid')
import matplotlib.patches as patches


# In[2]:


cc = pd.read_csv('/Users/jit/Downloads/credit_card1.csv') 


# In[3]:


cc.head()


# In[4]:


cc.shape


# In[5]:


cc.describe()


# In[6]:


cc.info()


# In[82]:


palette = sns.color_palette("husl", len(cc['Marital_Status'].unique()))

# Create countplot with custom colors and styles
sns.set(rc={'figure.figsize':(7,5)})
ax = sns.countplot(x='Marital_Status', data=cc, palette=palette, hatch='//')

# Set title
plt.title("Marital Status Distribution", fontsize=12)

# Add labels to bars
for container in ax.containers:
    ax.bar_label(container, fmt='%d', fontsize=12, color='black')

# Show plot
plt.show()


# In[9]:


cc.info()


# In[86]:


palette = sns.color_palette("husl", len(cc['Gender'].unique()))

# Create countplot with custom colors and styles
sns.set(rc={'figure.figsize':(6,4)})
ax = sns.countplot(x='Gender', data=cc, palette=palette, hatch='//')

# Set title
plt.title("Gender Distribution", fontsize=12)

# Add labels to bars
for container in ax.containers:
    ax.bar_label(container, fmt='%d', fontsize=12, color='black')

# Show plot
plt.show()


# In[79]:


palette = sns.color_palette("husl", len(cc['Gender'].unique()))
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = cc, x = 'Customer_Age', hue = 'Gender', palette=palette, hatch='/')

for bars in ax.containers:
    ax.bar_label(bars)


# In[67]:


alette = sns.color_palette("husl", len(cc['Customer_Job'].unique()))

# Set figure size
sns.set(rc={'figure.figsize': (8, 5)})

# Create countplot with custom colors and styles
ax = sns.countplot(x='Customer_Job', data=cc, palette=palette, hatch='//')

# Set title
plt.title("Customer_Job", fontsize=12)

# Add labels to bars
for container in ax.containers:
    ax.bar_label(container, fmt='%d', fontsize=12, color='black')

# Show plot
plt.show()


# In[66]:


alette = sns.color_palette("husl", len(cc['Education_Level'].unique()))

# Set figure size
sns.set(rc={'figure.figsize': (8, 5)})

# Create countplot with custom colors and styles
ax = sns.countplot(x='Education_Level', data=cc, palette=palette, hatch='//')

# Set title
plt.title("Education_Level", fontsize=12)

# Add labels to bars
for container in ax.containers:
    ax.bar_label(container, fmt='%d', fontsize=12, color='black')

# Show plot
plt.show()


# In[77]:


palette = sns.color_palette("husl", len(cc['Card_Category'].unique()))

# Set figure size
sns.set(rc={'figure.figsize': (8, 5)})   

# Create countplot with custom colors and styles
ax = sns.countplot(x='Card_Category', data=cc, palette=palette, hatch='//')

# Set title
plt.title("Card_Category", fontsize=12)

# Add labels to bars
for container in ax.containers:
    ax.bar_label(container, fmt='%d', fontsize=12, color='black')

# Show plot
plt.show()


# In[ ]:




