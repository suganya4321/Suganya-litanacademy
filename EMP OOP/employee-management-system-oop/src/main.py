import os
from services.employee_service import EmployeeService  # Fixed typo in import statement

def main():
    """
    Entry point of the Employee Management System application.
    Initializes services, loads data, and provides a menu for user interactions.
    """
    csv_path = os.path.join(os.path.dirname(__file__), "Employee.csv")
    employee_service = EmployeeService(csv_path)  # Fixed variable name and removed unnecessary employee_list argument

    # Load existing employee data
    employee_service.load_employees()

    while True:
        print("\n--- Employee Management System Menu ---")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")  # Fixed typo in print statement
        print("4. Delete Employee")
        print("5. List Employees")
        print("6. Department Wise Report")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            employee_service.add_employee()
        elif choice == '2':
            employee_service.view_employee()  # Fixed typo in variable name
        elif choice == '3':
            employee_service.update_employee()
        elif choice == '4':
            employee_service.delete_employee()
        elif choice == '5':
            employee_service.list_employees()
        elif choice == '6':
            employee_service.department_wise_report()  # Fixed incomplete function call
        elif choice == '7':
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()