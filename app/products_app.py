import csv


# READ PRODUCTS CSV

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        #print(dict(row))
        products.append(row)

menu = """
    Hi.

    Welcome to the products app.

    There are {0} products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))

crud_operation = input(menu)
crud_operation = crud_operation.title()

def list_products():
    print("LISTING PRODUCTS")

def show_product():
    print("SHOWING PRODUCT")

def create_product():
    print("CREATING PRODUCT")

def update_product():
    print("UPDATING PRODUCT")

def destroy_product():
    print("DESTROYING PRODUCT")

if crud_operation == "List": list_products()
elif crud_operation == "Show": show_product()
elif crud_operation == "Create": create_product()
elif crud_operation == "Update": update_product()
elif crud_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE OF THE RECOGNIZED OPERATIONS.")
