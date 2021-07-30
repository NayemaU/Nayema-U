#WEEK ONE

product_list = ["latte", "americano", "espresso", "cappacino", "mocha", "water"] 
print("Welcome to Nays Diner \n")
#press 1 to go to main menu 


operation = ("main_menu")
main_menu = input(" press 1 for order menu \n press 2 for courier \n press 0 to exit the app\n")
print(main_menu)
while True:
    if main_menu == "0":
        print("exit app")
        break
    elif main_menu == "1":
        while True:
            product_menu = input(" Press 1 to see the menu \n Press 2 to create and add to your list \n Press 3 to replace or delete item on list \n Press 4 to view basket \n Press 0 for Exit \n")
            if product_menu == "1":
                print(product_list)
                break
            elif product_menu == "2":
                new_item = input("what would you like to add?")
                product_list.append(new_item)
                print(product_list)
                break
            elif product_menu == "3":
                for (i,j) in enumerate(product_list,start = 0):
                    print(i,j)
                new_index = int(input("what number would you like?"))
                new_value= input("what would you like it to be?")
                    
                product_list[new_index] = new_value
                print(product_list)
                break
            elif product_menu == "4":
                delete_index = int(input("what would you like to  delete?"))
                
                del product_list[delete_index]
                print(product_list)
                break

