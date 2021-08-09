import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_BM = pd.read_csv(r"C:\Users\vasudevan.gopalan\OneDrive - GAVS Technologies Private Limited\Knowledge Repository\Python\bigmart_data.csv")
#drop null values. Removes rows that has any columns as null
data_BM = data_BM.dropna(how='any')
print(data_BM.head())
#line chart for item type wise mean MRP. Default chart type of matplotlib is line char
#mean price based on item type
price_by_item = data_BM.groupby('Item_Type').Item_MRP.mean()[:10]
print(price_by_item)
#index here refers to item_type grouping, and values here refers to the mean value of item mrp
x = price_by_item.index.tolist()
y = price_by_item.values.tolist()
#set figure size
plt.figure(figsize=(14,8))
#set title
plt.title('Mean price for each item type')
#set axis labels
plt.xlabel('Item Type')
plt.ylabel('Mean Price')
#set xticks
plt.xticks(labels=x,ticks=np.arange(len(x)))
plt.plot(x,y)#gives line chart
#plt.show()
plt.bar(x,y)#gives bar chart
#plt.show()

#histograms
plt.title('Item MRP Price Distribution')
plt.xlabel('Item MRP')
plt.ylabel('Frequency')
plt.hist(data_BM['Item_MRP'],bins=20, color='lightblue')
#plt.show()

#box plots
data = data_BM['Item_Outlet_Sales']
#create outlier point shape
red_diamond = dict(markerfacecolor='r',marker='D')
#set title
plt.title('Item Sales Distribution')
#make the boxplot
plt.boxplot(data.values, labels=['Item Sales'],flierprops=red_diamond)
#plt.show()

#multiple box plots
data = data_BM[['Item_Weight','Item_MRP']]
#create outlier point shape
red_diamond = dict(markerfacecolor='r',marker='D')
#generate subplots
fig, ax = plt.subplots()
plt.boxplot(data.values, labels=['Item Weight', 'Item MRP Price'])
#plt.show()

#voilin plots - for density distribution of item weights and item price
data = data_BM[['Item_Weight','Item_MRP']]
fig, ax = plt.subplots()
#add labels to x axis
plt.xticks(ticks=[1,2],labels=['Item Weight','Item MRP'])
#make violinplot
plt.violinplot(data.values)
#plt.show()

#scatter plots - for depicting cloud of observations
plt.xlabel('Item Weight')
plt.ylabel('Item Visibility')
plt.scatter(data_BM['Item_Weight'][:200], data_BM['Item_Visibility'][:200])
#plt.show()

#Bubble plots - useful to understand interdependant relations amongst 3 variables
plt.xlabel('Item MRP')
plt.ylabel('Item Outlet Sales')
#item_visibility will be depicted as dots. larger the dot, higher this value
plt.scatter(data_BM['Item_MRP'][:100], data_BM['Item_Outlet_Sales'][:100],s=data_BM['Item_Visibility'][:100]*1000)
plt.show()
