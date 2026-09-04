def read_employees():
    employee_info = []

    with open("employees.txt", "r") as file:
        for line in file:
            line = line.strip()
            words = line.split(",")

            name = words[0]
            salary = int(words[1])

            employee = {
                "name": name,
                "salary": salary
            }

            employee_info.append(employee)

    return employee_info


def calculate_total_salary(employees):
    total_salary = 0

    for employee in employees:
        total_salary += employee["salary"]

    return total_salary


def find_highest_paid(employees):
    highest = employees[0]

    for employee in employees:
        if employee["salary"] > highest["salary"]:
            highest = employee

    return highest


def find_filtered(employees, threshold):
    filtered = []

    for employee in employees:
        if employee["salary"] > threshold:
            filtered.append(employee)

    return filtered

def main():

    employees = read_employees()

    while True:
        print("\nEmployee Salary Analyzer")
        print("1. Show employees")
        print("2. Show total salary")
        print("3. Show highest paid")
        print("4. Show employees above threshold")
        print("5. Exit")

        choice = input("Enter an option from 1-5: ")

        if choice == "1":
        	print(employees)

        elif choice == "2":
        	employees_total_salary = calculate_total_salary(employees)
        	print("Total salary:", employees_total_salary)

        elif choice == "3":
        	highest_paid_employee = find_highest_paid(employees)
        	print("Highest paid employee:", highest_paid_employee)

        elif choice == "4":
        	try:
            		threshold = int(input("Enter threshold: "))
            		filtered_employees = find_filtered(employees, threshold)
            		print("Employees above threshold:", filtered_employees)

        	except ValueError:
            		print("Please enter a valid input")

        elif choice == "5":
        	print("Exiting...")
        	break

        else:
        	print("Invalid choice")


main()