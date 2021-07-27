#WEEK ONE

product_list = ["latte", "americano", "espresso", "cappacino", "mocha", "water"]
print("Welcome to Nays Diner")
#press 1 to go to main menu 


operation = ("main_menu")
main_menu = input(" Press 1 to see the menu \n Press 2 to create and add to your list \n Press 3 to replace item on list \n Press 4 to delete items \n Press 0 for Exit \n")
print(main_menu)

if main_menu == "1":
    print(product_list)
        
elif main_menu == "2":
    print ("add to my list")
    
elif main_menu == "3":
    print("I am now updating")
    
