with open('product_list.txt','r') as file:
    product_list = (file.read())

with open ('courier_list.txt','r') as file:
    courier_list= (file.read())

with open ('order_list.txt','r') as file:
    order_list = (file.read())


order = {"customer_name":"", "customer_address":"",  "customer_number":"","courier_name":"" }
order_list = []
#orders_list = [{key_1: value1}, {key2_value2}]
#Dict = {customer_name: name, customer  qA_number:999}
#orders_list.append(Dict)

print("Welcome to Nay's Diner")

operation = ("main_menu")
main_menu = input("press 1 for product_list \n press 2 for courier_list \n press 3 for order_list \n press 0 to exit the app \n")
print(main_menu)
while True:
    if main_menu == "0":
        print(" You've exited the app")
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
    
# def add_order_list():
#     while True:
#         add_order = input("would you like to add an order? Yes/No")
#         if "Yes" in add_order_list:
#             current_order = dict(order)
#             current_order = ["customer_name"] = input("Enter full name")
#             current_order = ["customer_address"] = input("Enter full address")
#             current_order = ["customer_number"] = str(input("Enter mobile number"))
#             print("")
            
            
def add_order(order):  
    
    
    customer_name = input('Please enter the customers name')
    customer_address = input('Please enter the customers address') 
    
    
    
    order = {                            
        'customer_name':customer_name,                
        'customer_address':customer_address                 
    }
    
    order.append(order) 
    print(order)

add_order(order)