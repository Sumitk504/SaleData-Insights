#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# file path
excel_file_path = 'SaleData.xlsx'

# Load the SaleData from excel
df = pd.read_excel(excel_file_path)

# Display the first few rows of the SaleData
print("SaleData Overview:")
print(df.head())

# Basic statistics about numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Insights about sales by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sale_amt', data=df, ci=None)
plt.title('Total Sale Amount by Region')
plt.xlabel('Region')
plt.ylabel('Total Sale Amount')
plt.show()

# Insights about sales by manager
plt.figure(figsize=(10, 6))
sns.barplot(x='Manager', y='Sale_amt', data=df, ci=None)
plt.title('Total Sale Amount by Manager')
plt.xlabel('Manager')
plt.ylabel('Total Sale Amount')
plt.xticks(rotation=45)
plt.show()

# Relationship between Units and Sale Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units', y='Sale_amt', data=df)
plt.title('Relationship between Units and Sale Amount')
plt.xlabel('Units')
plt.ylabel('Sale Amount')
plt.show()


# In[ ]:




