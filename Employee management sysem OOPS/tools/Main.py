import csv
import os
from list_employee import Employee, EmployeeManager

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees_list = self.load_employees_from_csv()  # Fixed method call

    def load_employees_from_csv(self):
        employees_list = []
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    employees_list.append(row)
        return employees_list

    def save_employees_to_csv(self):
        if self.employees_list:
            with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = self.employees_list[0].keys()
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(self.employees_list)

    def add_employee(self):
        from add_employee import add_employee
        add_employee(self.employees_list)

    def view_employee(self):
        from view_employee import view_employee
        view_employee(self.employees_list)

    def update_employee(self):
        from update_employee import update_employee
        update_employee(self.employees_list)

    def delete_employee(self):
        from delete_employee import delete_employee
        delete_employee(self.employees_list)

    def department_wise_report(self):
        from Departmentwise_report import department_wise_report
        department_wise_report(self.employees_list)

    def list_employees(self):
        from list_employee import EmployeeManager as ListEmployeeManager
        from list_employee import Employee
        temp_manager = ListEmployeeManager()
        # Convert dicts to Employee objects if needed
        temp_manager.employees = [
            Employee(
                emp.get("Employee ID", ""),
                emp.get("Name", ""),
                emp.get("Email", ""),
                emp.get("Department Id", ""),
                emp.get("Department Name", ""),
                emp.get("Contact Details", "")
            ) for emp in self.employees_list
            if emp.get("Employee ID", "")  # Only add if there is an Employee ID
        ]
        temp_manager.list_employees()

    def run(self):
        while True:
            print("\n--- Employee Management System Menu ---")
            print("1. Add Employee")
            print("2. View Employee")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Department-wise Report")
            print("6. List Employees")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ").strip()

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employee()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.delete_employee()
            elif choice == '5':
                self.department_wise_report()
            elif choice == '6':
                self.list_employees()
            elif choice == '7':
                self.save_employees_to_csv()
                print("Employee data saved to CSV. Exiting Employee Management System.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    file_path = "C:\\Users\\Suganya\\OneDrive\\Documents\\Employee management system OOPS\\Employee.csv"
    manager = EmployeeManager(file_path)
    manager.run()