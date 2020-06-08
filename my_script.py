# groceries.py

#from print import pprint
import os
import pandas 

#csv_filepath = "data/products.csv"
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
df = pandas.read_csv(csv_filepath)
print(type(df))  #class 'panda.core.frame.dataframe
print(df.head())  # print first few rows
 #approach 2
products = df.to_dict("records")


breakpoint()
