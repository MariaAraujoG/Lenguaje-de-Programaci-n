    #Alumna Araujo González María Fernanda

Inventory=[]

Invntry={
    "id": 0,
    "Name": "Pencil",
    "Price": 0.5,
    "Quantity": 50
}

Inventory.append(Invntry)
print(Invntry.values())


#ADD PRODUCT FUNCTION
def Add_Product(id_product, Name, Price, Quantity):
    Inventory.append({"id": id_product, "Name": Name, "Price": Price, "Quantity": Quantity})
    return Inventory

Add_Product(1, "Notebook", 1.5, 90)
Add_Product(2, "Glue", 1.0, 80)
print(Inventory)


#UPDATE STOCK FUNCTION
def Update_Stock(id_product, New_Quantity):
    for dict_aux in Inventory:
        if "id" in dict_aux:
            Inventory[id_product]["Quantity"]=New_Quantity
    return Inventory[id_product]["Quantity"]

Update_Stock(1, 30)
Update_Stock(2, 100)
print(Inventory)


#UPDATE PRICES FUNCTION
def Update_Prices(id_product, New_Price):
    for dict_aux in Inventory:
        if "id" in dict_aux:
            Inventory[id_product]["Price"]=New_Price
    return Inventory[id_product]["Price"]
Update_Prices(1, 1.8)
Update_Prices(2, 1.2)
print(Inventory)


#REMOVE PRODUCT FUNCTION
def Remove_Product(id_product):
    for dict_aux in Inventory:
        if "id" in dict_aux:
            del Inventory[id_product]
Remove_Product(0)
print(Inventory)
