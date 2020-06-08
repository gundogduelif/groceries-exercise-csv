# groceries.py

#from print import pprint
import operator

import pandas 

csv_filepath = "products.csv"
df = pandas.read_csv(csv_filepath)
print(type(df))
 
#approach 1 
#products = []
#for row in :
#    products.append({})
#
#breakpoint()    


#approach 2
products = df.to_dict("records")






# PART - 1 

products = sorted(products, key=operator.itemgetter("name") )
products_count = len(products)
print("--------------")
print("THERE ARE " + str(products_count) + " PRODUCTS:")
print("--------------")

# {"id":1,
#  "name": "Chocolate Sandwich Cookies", 
# "department": "snacks", 
# "aisle": "cookies cakes", 
# "price": 3.50}
# person["first_name"]

for x in products:
    usd = "${0:.2f}".format(x["price"])
    print(" + " + x["name"] + " (" +str(usd) + ")")

# --------------
# THERE ARE 20 PRODUCTS:
# --------------
 # + All-Seasons Salt ($4.99)
 # + Chocolate Fudge Layer Cake ($18.50)
 # + Chocolate Sandwich Cookies ($3.50)
 # + Cut Russet Potatoes Steam N' Mash ($4.25)
 # + Dry Nose Oil ($21.99)
 # + Fresh Scent Dishwasher Cleaner ($4.99)
 # + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
 # + Green Chile Anytime Sauce ($7.99)
 # + Light Strawberry Blueberry Yogurt ($6.50)
 # + Mint Chocolate Flavored Syrup ($4.50)
 # + Overnight Diapers Size 6 ($25.50)
 # + Peach Mango Juice ($1.99)
 # + Pizza For One Suprema Frozen Pizza ($12.50)
 # + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
 # + Pure Coconut Water With Orange ($3.50)
 # + Rendered Duck Fat ($9.99)
 # + Robust Golden Unsweetened Oolong Tea ($2.49)
 # + Saline Nasal Mist ($16.00)
 # + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
 # + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)


# PART - 2

departments = []
for x in products:
    departments.append(x["department"])
    # if x["departments"] not in departments:
    #    departments.append(x["department"])
unique_departments = list(set(departments))
department_count = len(unique_departments)
# department_count = len(departments)
print("--------------")
print("THERE ARE " + str(department_count) + " DEPARTMENTS:")
print("--------------")
unique_departments.sort()
for d in unique_departments:
    matching_products = [x for x in products if x["department"] == d]
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"    
    print(" + " + d.title() + " (" + str(matching_products_count) + " " + label + ")") 



# --------------
# THERE ARE 10 DEPARTMENTS:
# --------------
# + Babies (1 product)
# + Beverages (5 products)
# + Dairy Eggs (1 product)
# + Dry Goods Pasta (1 product)
# + Frozen (4 products)
# + Household (1 product)
# + Meat Seafood (1 product)
# + Pantry (2 products)
# + Personal Care (2 products)
# + Snacks (2 products)