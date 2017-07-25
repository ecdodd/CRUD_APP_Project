import csv


# READ PRODUCTS CSV

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

menu = """
------------------------------------------------------
    PRODUCTS APPLICATION
------------------------------------------------------
    Welcome to the products app.

    There are {0} products. Please select an operation:

    Operation | Description
    --------- |-------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show inofrmation about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

    Please choose an operation:

""".format(len(products))

crud_operation = input(menu)
crud_operation = crud_operation.title()

def list_products():
   print("There are " + str(len(products)) + " product(s):")
   for product in products:
       print("+ ID: " + product["id"] + "; Name: " +product["name"]+ "; Aisle: " +product["aisle"]+ "; Dept: " + product["department"]+ "; Price: " + product["price"])

def show_product():
    product_id = input("Please specify the product's identifier:")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Showing a product here:", dict(product))
    else:
        print("Couldn't find a product with identifier", product)

def create_product():
    print("Create a product")
    product_name = input("Product name is:")
    product_aisle = input("Product aisle is:")
    product_department = input("Product department is:")
    product_price = input("Product price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
        }
    print("New product is", new_product)
    products.append(new_product)

def update_product():

   id_entry = input("Please specify the product's identifier:")
   chg_item = next((item for item in products if item['id'] == id_entry), None)
   index_num = products.index(chg_item)

   show_name = products[index_num]["name"]
   new_name = input("Change name from {} to:".format(show_name))
   products[index_num]["name"] = new_name

   show_aisle = products[index_num]["aisle"]
   new_aisle = input("Change aisle from {} to:".format(show_aisle))
   products[index_num]["aisle"] = new_aisle

   show_dept = products[index_num]["department"]
   new_dept = input("Change department from {} to:".format(show_dept))
   products[index_num]["department"] = new_dept

   show_price = products[index_num]["price"]
   new_price = input("Change price from {} to:".format(show_price))
   products[index_num]["price"] = new_price

def destroy_product():
   id_entry = input("Please specify the product's identifier:")
   del_item = next((item for item in products if item['id'] == id_entry), None)
   index_num = products.index(del_item)
   products.pop(index_num)

if crud_operation == "List": list_products()
elif crud_operation == "Show": show_product()
elif crud_operation == "Create": create_product()
elif crud_operation == "Update": update_product()
elif crud_operation == "Destroy": destroy_product()
else: print("Oops. Please choose one of the recognized operations.")

#OVERWRITING INVENTORY CSV FILE
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
