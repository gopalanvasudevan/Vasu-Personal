import pandas as pd
import numpy as np
data_BM = pd.read_csv(r"C:\Users\vasudevan.gopalan\OneDrive - GAVS Technologies Private Limited\Knowledge Repository\Python\bigmart_data.csv")
print("top 5 rows")
print(data_BM.head())
#drop null values. Removes rows that has any columns as null
data_BM = data_BM.dropna(how='any')
print("top 5 rows")
print(data_BM.head())
sorted_data = data_BM.sort_values(by='Outlet_Establishment_Year')
print(sorted_data[:5])
#sort in place and descending order
data_BM.sort_values(by='Outlet_Establishment_Year',inplace=True, ascending=False)
print(data_BM[:5])
#sort by multiple columns. Use a list as input
print(data_BM.sort_values(by=['Outlet_Establishment_Year','Item_Outlet_Sales'],ascending=False)[:5])
#sort by row index
data_BM.sort_index(inplace=True)
print(data_BM[:5])

# #merging data frames
# df1 = pd.DataFrame({'A':['A0, A1, A2, A3'],
#                     'B':['B0, B1, B2, B3'],
#                     'C':['C0, C1, C2, C3'],
#                     'D':['D0, D1, D2, D3']},
#                     index=[0,1,2,3])
# df2 = pd.DataFrame({'A':['A4, A5, A6, A7'],
#                     'B':['B4, B5, B6, B7'],
#                     'C':['C4, C5, C6, C7'],
#                     'D':['D4, D5, D6, D7']},
#                     index=[4,5,6,7])
# df3 = pd.DataFrame({'A':['A8, A9, A10, A11'],
#                     'B':['B8, B9, B10, B11'],
#                     'C':['C8, C9, C10, C11'],
#                     'D':['D8, D9, D10, D11']},
#                     index=[8,9,10,11])
# #combine the data frames
# result = pd.concat([df1, df2, df3])
# print(result)

# #combine the data frames with labels
# result = pd.concat([df1, df2, df3], keys=['x','y','z'])
# print(result)
# #get second data frame
# print(result.loc['y'])

#apply function
print(data_BM.head())
print("about to apply")
data_BM.apply(lambda x :x )
print(data_BM.head())
#access first row
print(data_BM.apply(lambda x : x[0]))
#access first column
print(data_BM.apply(lambda x : x[0], axis=1))
#access by column name
print(data_BM.apply(lambda x : x['Item_Fat_Content'], axis=1))

#clip the price if greater than 200
def clip_price(price):
    if price > 200:
        price = 200
    return price

print("before clipping")
print(data_BM["Item_MRP"][:5])
print("after clipping")
print(data_BM["Item_MRP"].apply(lambda x: clip_price(x))[:5])

#Encoding the outlet column
def label_encode(city):
    if city == 'Tier 1':
        label = 0
    elif city == 'Tier 2':
        label = 1
    else:
        label = 2
    return label

print("before encoding")
print(data_BM['Outlet_Location_Type'][:5])
print("after encoding")
print(data_BM['Outlet_Location_Type'].apply(lambda x: label_encode(x))[:5])