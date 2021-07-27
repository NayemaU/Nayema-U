couriers = []
productlist = []

with open ("courier.txt", "r", ) as courier_file:
    for item in courier_file. readline():
        couriers.append(item.replace("\n",""))
        
print(couriers)