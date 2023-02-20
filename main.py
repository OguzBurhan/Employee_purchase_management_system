
employee_list = []
item_list = []
# Print Menu Function
def printMenu():
    print("""
—————————————————————————————
|   1. Create Employee       |
|   2. Create Item           |
|   3. Make Purchase         |
|   4. All Employee Summary  |
|   5. Exit                  |
—————————————————————————————
        """)


# Function to create employee
def add_employee():
    # Input validation functions
    def is_valid_id(id):
        if not id.isdigit():
            print("Invalid input. Employee ID must be a number.")
            return False
        elif int(id) in [emp["employee_id"] for emp in employee_list]:
            print("Invalid input. Employee ID already exists.")
            return False
        return True

    def is_valid_name(name):
        if not name.replace(" ", "").isalpha():
            print("Invalid input. Name must be a string of alphabetic characters only.")
            return False
        return True

    def is_valid_contract_type(contract_type):
        if contract_type.lower() not in ["hourly", "manager"]:
            print("Invalid input. Contract type must be 'hourly' or 'manager'.")
            return False
        return True

    def is_valid_years(years):
        if not years.isdigit():
            print("Invalid input. Years worked must be a number.")
            return False
        return True

    def is_valid_employee_discount(employee_discount):
        if not employee_discount.isdigit():
            print("Invalid input. Employee discount number must be a number.")
            return False
        elif int(employee_discount) in [emp["employee_discount"] for emp in employee_list]:
            print("Invalid input. Employee discount number already exists.")
            return False
        return True

    # Get employee information
    employee_info = {
        "employee_id": 0,
        "employee_name": "",
        "contract_type": "",
        "year": 0,
        "total_purchased": 0,
        "total_discounts": 0,
        "employee_discount": 0
    }
# While loop to get the input from user and append it to the list
    while True:
        employee_id = input("Enter the employee ID: ")
        if not is_valid_id(employee_id):
            continue
        employee_info["employee_id"] = int(employee_id)

        name = input("Enter the employee name: ")
        if not is_valid_name(name):
            continue
        employee_info["employee_name"] = name

        contract_type = input("Enter the contract type (hourly or manager): ")
        if not is_valid_contract_type(contract_type):
            continue
        employee_info["contract_type"] = contract_type.lower()

        years = input("Enter the years worked: ")
        if not is_valid_years(years):
            continue
        employee_info["year"] = int(years)

        employee_discount = input("Enter the employee discount number: ")
        if not is_valid_employee_discount(employee_discount):
            continue
        employee_info["employee_discount"] =  int(employee_discount)

        employee_list.append(employee_info.copy())

        cont = input("Would you like to continue? (yes/no) ")
        if cont.lower() in ['no', 'n']:
            break

    print(employee_list)
    return True

# function to create the items
def create_item():
    # validation functions for item inputs
    def is_valid_number(item):
        if not item.isdigit():
            print("Invalid input. Item number must be an integer.")
            return False
        elif int(item) in [itm["item_number"] for itm in item_list]:
            print("Invalid input. Item number already exists.")
            return False
        return True

    def is_valid_itemName(itemName):
        if not itemName.replace(" ", "").isalpha():
            print("Invalid input. Name must be a string of alphabetic characters only.")
            return False
        return True

    def is_valid_itemInput(iteminput):
        if not iteminput.replace(" ", "").isdigit():
            print("Invalid input. Item input must be an integer")
            return False
        return True
# dictionary for item info
    item_info = {
        "item_number": 0,
        "item_name": "",
        "item_cost": 0,
    }
# while loop to get the value of the items
    while True:
        item_number = input("Enter the item number: ")
        if not is_valid_number(item_number):
            continue
        item_info["item_number"] = int(item_number)

        item_name = input("Enter the item name: ")
        if not is_valid_itemName(item_name):
            continue
        item_info["item_name"] = item_name

        item_cost = input("Enter the item cost: ")
        if not is_valid_itemInput(item_cost):
            continue
        item_info["item_cost"] = int(item_cost)

        item_list.append(item_info.copy())

        cont = input("Would you like to continue? (yes/no) ")
        if cont.lower() in ['no', 'n']:
            break

    print(item_list)

    return True

# function to make the purchase
def make_purchase():
    print("Item number  |  Item Name  |  Item Cost")

    for item in item_list:
        itemNumber = item["item_number"]
        itemName = item["item_name"]
        itemCost = item["item_cost"]

        print(f"{itemNumber:<13} | {itemName:<13} | {itemCost:<13} ")

# validation functions
    def is_valid_employee_discount(employee_discount):
        if not employee_discount.isdigit():
            print("Invalid input. Employee discount number must be a number.")
            return False
        elif int(employee_discount) in [emp["employee_discount"] for emp in employee_list]:
            return True
        else:
            print("Invalid input. Employee discount number does not match any employee in the system.")
            return False

    def is_valid_number(item_number):
        if not item_number.isdigit():
            print("Invalid input. Item number must be an integer.")
            return False
        elif int(item_number) in [item["item_number"] for item in item_list]:
            return True
        else:
            print("Invalid input. Item number does not match any item in the system.")
            return False
# function to get the employee discount number
    def get_employee(employee_discount):
        for employee in employee_list:
            if employee["employee_discount"] == int(employee_discount):
                return employee
# function to calculate the discount amount based on the employee inputs
    def get_employee_discount_rate(employee):
        # Discounts are based on the number of years worked (2% for each year, maximum 10%)
        years_worked_discount = 0.02 * employee["year"]
        if years_worked_discount > 0.1:
            years_worked_discount = 0.1

        # If the employee is a manager (10% more discount on top of the worked year discount), or hourly employee (2% discount)
        if employee["contract_type"] == 'manager':
            years_worked_discount += 0.1
        elif employee["contract_type"] == 'hourly':
            years_worked_discount += 0.02

        return years_worked_discount
# function to update the total purchase value
    def update_total_purchase(employee, newPurchaseAmount):
        employee["total_purchased"] += newPurchaseAmount
# function to update the total discounts value
    def update_total_discounts(employee, newDiscountAmount):
        employee["total_discounts"] += newDiscountAmount

    discount_number = input("Enter the employee discount number: ")
    if not is_valid_employee_discount(discount_number):
        return False

    employee = get_employee(discount_number)

    total_discount_rate = get_employee_discount_rate(employee)

    check_item = input("Enter the item number: ")
    if not is_valid_number(check_item):
        return False


    itemNumber = 0
    itemName = ""
    itemCost = 0
# loop through the item_list to get the current item value
    for currentItem in item_list:
        if currentItem["item_number"] == int(check_item):
            itemNumber = currentItem["item_number"]
            itemName = currentItem["item_name"]
            itemCost = currentItem["item_cost"]


    print(employee)

    # make sure that the maximum discount is not over $200 of the employees life time
    final_discount = 0

# if statement to limit the total discount amount to 200 in total.
    if(employee["total_discounts"] >= 200):
        final_discount = 0
    elif (itemCost * total_discount_rate > 200):
        final_discount = 200
    else:
        final_discount = itemCost * total_discount_rate

    final_cost = itemCost - final_discount

    print("You are trying to purchase the following item:")
    print(f" {itemNumber:<13} | {itemName:<13} | {itemCost:<13} ")
    print(f"Your final cost is: {final_cost:.2f}")
    print(f"Your final discount is: {final_discount:.2f}")

    confirm = input("Confirm purchase? (yes or no): ")
    if confirm == "yes":
        update_total_purchase(employee, final_cost)
        update_total_discounts(employee, final_discount)

        return True

    return False

# function to display the summary
def display_summary():
    print \
        ("Employee ID | Employee Name | Employee Type | Years Worked | Total Purchased | Total Discount | Employee Discount Number")
    for emp in employee_list:
        employee_id = emp["employee_id"]
        employee_name = emp["employee_name"]
        contract_type = emp["contract_type"]
        year = emp["year"]
        total_purchased = emp["total_purchased"]
        total_discounts = emp["total_discounts"]
        employee_discount = emp["employee_discount"]

        print \
            (f"{employee_id:<11} |  {employee_name:<11}  | {contract_type:<11}  | {year:<11} |  ${total_purchased:<14.2f}  |  ${total_discounts:<14.2f} | {employee_discount:<11}")
# menu options
while True:
    printMenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        create_item()
    elif choice == "3":
        make_purchase()
    elif choice == "4":
        display_summary()
    elif choice == "5":
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
