class Employee:
    def __init__(self, employee_id, name, email, department_id, department_name, contact_details):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department_id = department_id
        self.department_name = department_name
        self.contact_details = contact_details

    def __str__(self):
        return (f"Employee ID: {self.employee_id}, Name: {self.name}, Email: {self.email}, "
                f"Department ID: {self.department_id}, Department Name: {self.department_name}, "
                f"Contact: {self.contact_details}")

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def validate_employee_id(self, employee_id):
        if not employee_id:
            print("Validation failed: Employee ID cannot be empty.")
            return False
        if not employee_id.isalnum():
            print("Validation failed: Employee ID must be alphanumeric.")
            return False
        return True

    def validate_name(self, name):
        if not name:
            print("Validation failed: Name cannot be empty.")
            return False
        if not all(x.isalpha() or x.isspace() for x in name):
            print("Validation failed: Name must contain only letters and spaces.")
            return False
        return True

    def validate_email(self, email):
        if not email:
            print("Validation failed: Email cannot be empty.")
            return False
        if "@" not in email or "." not in email:
            print("Validation failed: Invalid email format.")
            return False
        return True

    def validate_department_id(self, department_id):
        if not department_id:
            print("Validation failed: Department Id cannot be empty.")
            return False
        if not department_id.isalnum():
            print("Validation failed: Department Id must be alphanumeric.")
            return False
        return True

    def validate_department_name(self, department_name):
        if not department_name:
            print("Validation failed: Department Name cannot be empty.")
            return False
        if not all(x.isalpha() or x.isspace() for x in department_name):
            print("Validation failed: Department Name must contain only letters and spaces.")
            return False
        return True

    def validate_contact_details(self, contact_details):
        if not contact_details:
            print("Validation failed: Contact Details cannot be empty.")
            return False
        if not contact_details.isdigit():
            print("Validation failed: Contact Details must be numeric.")
            return False
        if len(contact_details) < 8:
            print("Validation failed: Contact Details must be at least 8 digits.")
            return False
        return True

    def add_employee(self):
        print("\n--- Add Employee ---")
        employee_id = input("Enter Employee ID: ")
        if not self.validate_employee_id(employee_id):
            return

        name = input("Enter Employee Name: ")
        if not self.validate_name(name):
            return

        email = input("Enter Email: ")
        if not self.validate_email(email):
            return

        department_id = input("Enter Department ID: ")
        if not self.validate_department_id(department_id):
            return

        department_name = input("Enter Department Name: ")
        if not self.validate_department_name(department_name):
            return

        contact_details = input("Enter Contact Details: ")
        if not self.validate_contact_details(contact_details):
            return

        employee = Employee(employee_id, name, email, department_id, department_name, contact_details)
        self.employees.append(employee)
        print(f"\nEmployee {name} has been successfully added.")
        print(f"(Simulation) Confirmation email sent to {email}.")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    import csv
    file_path = "C:\\Users\\Suganya\\OneDrive\\Documents\\Employee management system OOPS\\tools\\Employee.csv"
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            # Save to CSV on exit
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["Employee ID", "Name", "Email", "Department Id", "Department Name", "Contact Details"]
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for emp in manager.employees:
                    csv_writer.writerow({
                        "Employee ID": emp.employee_id,
                        "Name": emp.name,
                        "Email": emp.email,
                        "Department Id": emp.department_id,
                        "Department Name": emp.department_name,
                        "Contact Details": emp.contact_details
                    })
            print("Exiting the system. Employee data saved to CSV.")
            break
        else:
            print("Invalid choice. Please try again.")