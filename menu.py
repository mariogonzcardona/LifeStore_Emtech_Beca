from processes import *
# Menu interactivo por consola 

# Preparacion de metodos para login y register
def register(user_email,password):
    return True

def login(user_email,password):
    
    return True

def show_login_register_menu():
    while True:
        print("-"*50)
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("-"*50)
        try:
            option = int(input("Select an option: "))
            if option == 1:
                user_email = input("Enter your email: ")
                password = input("Enter your password: ")
                if login(user_email,password):
                    print("Login successful")
                    show_options_menu()
                else:
                    print("Login failed")
            elif option == 2:
                user_email = input("Enter your email: ")
                password = input("Enter your password: ")
                if register(user_email,password):
                    print("Register successful please login")
                else:
                    print("Register failed")
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")

def show_options_menu():
    while True:
        print("-"*50)
        print("1. Show report 1")
        print("2. Show report 2")
        print("3. Show report 3")
        print("4. Exit")
        print("-"*50)
        try:
            option = int(input("Select an option: "))
            if option == 1:
                show_process_report_1()
            elif option == 2:
                show_process_report_2()
            elif option == 3:
                show_process_report_3()
            elif option == 4:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")

def show_process_report_1():
    while True:
        print("-"*50)
        print("1. Show products with the highest sales and searches")
        print("2. Show products with lower sales and searches by category")
        print("3. Exit")
        try:
            option = int(input("Select an option: "))
            if option == 1:
                process_report_1(1)
            elif option == 2:
                process_report_1(2)
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")

def show_process_report_2():
    while True:
        print("-"*50)
        print("1. Show Top Reviewed Products")
        print("2. Show Worst Reviewed Products")
        print("3. Exit")
        try:
            option = int(input("Select an option: "))
            if option == 1:
                process_report_2(1)
            elif option == 2:
                process_report_2(2)
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")

def show_process_report_3():
    while True:
        print("-"*50)
        print("1. Show Total Revenues")
        print("2. Show Total Annual Sales")
        print("3. Months With Higher Sales")
        print("4. Exit")
        try:
            option = int(input("Select an option: "))
            if option == 1:
                process_report_3(1)
            elif option == 2:
                process_report_3(2)
            elif option == 3:
                process_report_3(3)
            elif option == 4:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
    

