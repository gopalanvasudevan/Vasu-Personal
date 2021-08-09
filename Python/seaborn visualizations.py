#seaborn visualizations. helps visualizations / chart creations in fewer lines as compared to matplotlib
import seaborn as sns
sns.set(style='darkgrid')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
data_BM = pd.read_csv(r"C:\Users\vasudevan.gopalan\OneDrive - GAVS Technologies Private Limited\Knowledge Repository\Python\bigmart_data.csv")
#drop null values. Removes rows that has any columns as null
data_BM = data_BM.dropna(how='any')
#multiply by 100 to increase the size, to look better in chart
data_BM['Visibility_Scaled']=data_BM['Item_Visibility']*100
print(data_BM.head())

#line chart
sns.lineplot(x='Item_Weight',y='Item_MRP',data=data_BM[:50])
#use plt show command to display the chart in VS editor itself. 
#Since seaborn is built on top of plt, it works this way
plt.show()

#bar chart
sns.barplot(x='Item_Type',y='Item_MRP',data=data_BM[:10])
plt.show()

#histogram
sns.distplot(data_BM['Item_MRP'])
plt.show()

#box plot
sns.boxplot(data_BM['Item_Outlet_Sales'], orient='vertical')
plt.show()

#violin plot
sns.violinplot(data_BM['Item_Outlet_Sales'], orient='vertical', color='magenta')
plt.show()

#scatter plot
sns.relplot(x='Item_MRP',y='Item_Outlet_Sales',data=data_BM[:200],kind='scatter')
plt.show()

#scatter plot with hue semantic. hue gives the 3rd dimension
sns.relplot(x='Item_MRP',y='Item_Outlet_Sales',data=data_BM[:200], hue='Item_Type')
plt.show()

#line plot for different categories of the outlet size. use hue
sns.lineplot(x='Item_Weight',y='Item_MRP',hue='Outlet_Size',data=data_BM[:150])
plt.show()

#bubble plot
sns.relplot(x='Item_MRP',y='Item_Outlet_Sales',data=data_BM[:200], kind='scatter', size='Visibility_Scaled', hue='Visibility_Scaled')
plt.show()

#subplots
sns.relplot(x='Item_Weight',y='Item_Visibility',hue='Outlet_Size', style='Outlet_Size', col='Outlet_Size', data=data_BM[:150])
plt.show()