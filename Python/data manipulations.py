#data manipulation
import pandas as pd
import numpy as np
data_BM = pd.read_csv(r"C:\Users\vasudevan.gopalan\OneDrive - GAVS Technologies Private Limited\Knowledge Repository\Python\bigmart_data.csv")
#drop null values. Removes rows that has any columns as null
data_BM = data_BM.dropna(how='any')
#use group by to find out mean price of each item type
price_by_item = data_BM.groupby('Item_Type')
print(data_BM.head())
print(price_by_item.first())
#get mean price
print(price_by_item.Item_MRP.mean())
print(price_by_item['Item_MRP'].mean())
#above 2 statements return the same result

#group on multiple columns
multiple_groups = data_BM.groupby(['Item_Type','Item_Fat_Content'])
print(multiple_groups.first())

# cross-tabulation view can be established using crosstab feature.
#e.g. - frequency of outlet size for outlet location type
print(pd.crosstab(data_BM['Outlet_Size'],data_BM['Outlet_Location_Type']))
#create pivot table, uses the mean function by default for the values field
print(pd.pivot_table(data_BM, index=['Outlet_Establishment_Year'], values='Item_Outlet_Sales'))
#create pivot with multiple columns
print(pd.pivot_table(data_BM, index=['Outlet_Establishment_Year','Outlet_Location_Type','Outlet_Size'], values='Item_Outlet_Sales'))
#do multiple aggregation functions in pivot table
print(pd.pivot_table(data_BM, index=['Outlet_Establishment_Year','Outlet_Location_Type','Outlet_Size'], values='Item_Outlet_Sales', aggfunc=[np.mean, np.median, min, max,np.std]))
