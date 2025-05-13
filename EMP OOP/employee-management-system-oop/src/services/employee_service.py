import csv
import os

class Employee:  # Fixed typo in class declaration
    def __init__(self, employee_id, name, email, department_id, department_name, contact_details):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department_id = department_id
        self.department_name = department_name
        self.contact_details = contact_details

    def __str__(self):
        return (f"ID: {self.employee_id}, Name: {self.name}, Email: {self.email}, "
                f"Department ID: {self.department_id}, Department Name: {self.department_name}, "
                f"Contact: {self.contact_details}")  # Fixed formatting issue in f-string

    def to_dict(self):
        return {
            "Employee ID": self.employee_id,
            "Name": self.name,
            "Email": self.email,
            "Department Id": self.department_id,
            "Department Name": self.department_name,
            "Contact Details": self.contact_details
        }

class EmployeeService:  # Added missing class declaration for EmployeeService
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.employee_list = []  # Added initialization for employee_list

    def load_employees(self):
        if not os.path.exists(self.csv_path):
            return
        with open(self.csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee = Employee(
                    row["Employee ID"],
                    row["Name"],
                    row["Email"],
                    row["Department Id"],
                    row["Department Name"],
                    row["Contact Details"]
                )
                self.employee_list.append(employee)

    def save_employees(self):
        with open(self.csv_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Employee ID", "Name", "Email", "Department Id", "Department Name", "Contact Details"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in self.employee_list:
                writer.writerow(emp.to_dict())

    def add_employee(self):
        print("\n--- Add Employee ---")
        
        # Employee ID validation (already handled if needed)
        employee_id = input("Enter Employee ID: ").strip()
        if not employee_id:
            print("Employee ID cannot be empty.")
            return
        if any(emp.employee_id == employee_id for emp in self.employee_list):
            print("Employee ID already exists.")
            return

        # Name validation
        name = input("Enter Name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters and spaces.")
            return

        # Email validation
        email = input("Enter Email: ").strip()
        if "@" not in email or "." not in email.split("@")[-1]:
            print("Invalid email format.")
            return

        # Department ID validation
        department_id = input("Enter Department ID: ").strip()
        if not department_id.isalnum():
            print("Department ID must be alphanumeric.")
            return

        # Department Name validation
        department_name = input("Enter Department Name: ").strip()
        if not department_name.replace(" ", "").isalpha():
            print("Department Name must contain only letters and spaces.")
            return

        # Contact Details validation
        contact_details = input("Enter Contact Details: ").strip()
        if not contact_details.isdigit() or len(contact_details) < 7:
            print("Contact Details must be a valid number with at least 7 digits.")
            return

        employee = Employee(employee_id, name, email, department_id, department_name, contact_details)
        self.employee_list.append(employee)
        self.save_employees()
        print(f"Employee {name} has been added.")
        print(f"Simulating sending welcome email to {email}...")
        

    def view_employee(self):
        print("\n--- View Employee ---")
        employee_id = input("Enter Employee ID to view: ").strip()
        if not employee_id:
            print("Employee ID cannot be empty.")
            return
        found = False
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                print(employee)
                found = True
                break
        if not found:
            print(f"Employee with ID {employee_id} not found.")

    def update_employee(self):
        print("\n--- Update Employee ---")
        employee_id = input("Enter Employee ID to update: ").strip()
        if not employee_id:
            print("Employee ID cannot be empty.")
            return
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                print("Leave blank to keep current value.")

                # Name validation
                name = input(f"New Name (current: {employee.name}): ").strip()
                if name and not name.replace(" ", "").isalpha():
                    print("Name must contain only letters and spaces.")
                    return
                name = name or employee.name

                # Email validation
                email = input(f"New Email (current: {employee.email}): ").strip()
                if email and ("@" not in email or "." not in email.split("@")[-1]):
                    print("Invalid email format.")
                    return
                email = email or employee.email

                # Department ID validation
                department_id = input(f"New Department ID (current: {employee.department_id}): ").strip()
                if department_id and not department_id.isalnum():
                    print("Department ID must be alphanumeric.")
                    return
                department_id = department_id or employee.department_id

                # Department Name validation
                department_name = input(f"New Department Name (current: {employee.department_name}): ").strip()
                if department_name and not department_name.replace(" ", "").isalpha():
                    print("Department Name must contain only letters and spaces.")
                    return
                department_name = department_name or employee.department_name

                # Contact Details validation
                contact_details = input(f"New Contact Details (current: {employee.contact_details}): ").strip()
                if contact_details and (not contact_details.isdigit() or len(contact_details) < 7):
                    print("Contact Details must be a valid number with at least 7 digits.")
                    return
                contact_details = contact_details or employee.contact_details

                # Confirmation before saving
                confirm = input("Save changes? (yes/no): ").strip().lower()
                if confirm == "yes":
                    employee.name = name
                    employee.email = email
                    employee.department_id = department_id
                    employee.department_name = department_name
                    employee.contact_details = contact_details
                    self.save_employees()
                    print(f"Employee {employee_id} has been updated.")
                else:
                    print("Update cancelled.")
                return
        print(f"Employee with ID {employee_id} not found.")

    def delete_employee(self):
        print("\n--- Delete Employee ---")
        employee_id = input("Enter Employee ID to delete: ").strip()
        if not employee_id:
            print("Employee ID cannot be empty.")
            return
        for i, employee in enumerate(self.employee_list):
            if employee.employee_id == employee_id:
                print("Employee found:")
                print(employee)
                confirm = input("Are you sure you want to delete this employee? (yes/no): ").strip().lower()
                if confirm == "yes":
                    del self.employee_list[i]
                    self.save_employees()
                    print(f"Employee {employee_id} has been deleted.")
                else:
                    print("Deletion cancelled.")
                return
        print(f"Employee with ID {employee_id} not found.")

    def list_employees(self):
        print("\n--- List of Employees by Department ---")
        if not self.employee_list:
            print("No employees found.")
            return
        dept_dict = {}
        for employee in self.employee_list:
            dept = employee.department_name
            if dept not in dept_dict:
                dept_dict[dept] = []
            dept_dict[dept].append(employee)
        if not dept_dict:
            print("No employees found in any department.")
            return
        for dept, employees in dept_dict.items():
            print(f"\nDepartment: {dept}")
            for emp in employees:
                print(f"  ID: {emp.employee_id}, Name: {emp.name}, Email: {emp.email}, "
                      f"Department ID: {emp.department_id}, Department Name: {emp.department_name}, "
                      f"Contact: {emp.contact_details}")    

    def department_wise_report(self):
        print("\n--- Department Wise Employee Report ---")
        if not self.employee_list:
            print("No employees found.")
            return
        department_name = input("Enter Department Name to generate report: ").strip()
        if not department_name:
            print("Department Name cannot be empty.")
            return
        # Case-insensitive match for department name
        employees_in_dept = [
            emp for emp in self.employee_list
            if emp.department_name.lower() == department_name.lower()
        ]
        if not employees_in_dept:
            print(f"No employees found in department '{department_name}'.")
            return
        print(f"\nEmployees in Department: {department_name}")
        for emp in employees_in_dept:
            print(f"  ID: {emp.employee_id}, Name: {emp.name}, Email: {emp.email}")   