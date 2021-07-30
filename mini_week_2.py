# #open PRODUCT_LIST.TXT file 
# #open COURIER.TXT file

with open('product_list.txt','r') as file:
    product_list = (file.read())

with open ('courier_list.txt','r') as file:
    courier_list= (file.read())
    
product_list = ["Latte", "Americano", "Espresso", "Cappuccino", "Mocha", "Water"]
courier_list = ["James","Sam","Ben","Flisss","Deco","Hannah"]


print("Welcome to Nay's Diner")

operation = ("main_menu")
main_menu = input(" press 1 for product list \n press 2 for courier list \n press 0 to exit the app\n")
print(main_menu)
while True:
    if main_menu == "0":
        print("exit app")
        break
    elif main_menu == "1":
    #elif main_menu == 2
        while True:
            product_menu = input(" Press 1 to view your product list \n Press 2 to view your courier list \n Press 3 to create a product list and add it to your list \n Press 4 to create a courier list and add to your list \n Press 5 to update your product list \n Press 6 to update your courier list \n Press 7 to delete item from product list \n Press 8 to delete courier \n Press 0 for Exit \n")
            if product_menu == "1":
                print(product_list)
                break
            if product_menu == "2":
                print(courier_list)
                break
            elif product_menu == "3":
                new_item = input("Would you like to create and add to your product list?")
                product_list.append(new_item)
                print(product_list)
                break
            elif product_menu == "4":
                new_item = input ("Would you like to create and add to your courier?")
                courier_list.append(new_item)
                print(courier_list)
                break
            elif product_menu == "5":
                for (i,j) in enumerate(product_list, start = 0):
                    print(i,j)
                new_index = int(input("Would you like to update your product list?"))
                new_value= input("what would you like it to be?")
                    
                product_list[new_index] = new_value
                print(product_list)
                break
            elif product_menu == "6":
                for (i,j) in enumerate(courier_list, start = 0):
                    print(i,j)
                new_index = int(input("Would you like to update your courier?"))
                new_value= input("what would you like it to be?")
                    
                product_list[new_index] = new_value
                print(product_list)
                break
            elif product_menu == "7":
                delete_index = int(input("What would you like to delete from your product list?"))
                del product_list[delete_index]
                print(product_list)
                break
            elif product_menu == "8":
                delete_index = int(input("What courier would you like to delete?"))
                del courier_list[delete_index]
                print(courier_list)
                break

