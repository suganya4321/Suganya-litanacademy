class Employee:
    def __init__(self, employee_id, name, email, department_id, department_name, contact_details):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department_id = department_id
        self.department_name = department_name  # Fixed assignment
        self.contact_details = contact_details  # Fixed assignment

    def update(self, name=None, email=None, department_id=None, department_name=None, contact_details=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if department_id:
            self.department_id = department_id
        if department_name:  # Fixed variable name
            self.department_name = department_name
        if contact_details:
            self.contact_details = contact_details

    def __str__(self):
        return (f"Employee ID: {self.employee_id}, Name: {self.name}, Email: {self.email}, "
                f"Department ID: {self.department_id}, Department Name: {self.department_name}, "
                f"Contact: {self.contact_details}")

class EmployeeManager:
    def __init__(self, file_path=None):
        self.file_path = file_path  # Store the file path
        self.employees = []  # Initialize the employees list

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def update_employee(self):
        print("\n--- Update Employee Details ---")
        employee_id = input("Enter Employee ID to update: ")
        employee = self.find_employee(employee_id)
        if not employee:
            print(f"Error: Employee with ID '{employee_id}' not found.")
            return

        print("\nCurrent Details:")
        print(employee)

        print("\nEnter new details (leave blank to keep current value):")
        new_name = input(f"New Name (current: {employee.name}): ") or employee.name
        new_department_id = input(f"New Department Id (current: {employee.department_id}): ") or employee.department_id
        new_department_name = input(f"New Department Name (current: {employee.department_name}): ") or employee.department_name
        new_email = input(f"New Email (current: {employee.email}): ") or employee.email
        new_contact = input(f"New Contact Details (current: {employee.contact_details}): ") or employee.contact_details

        print("\nReview updated details:")
        print(f"  Name: {new_name}")
        print(f"  Department Id: {new_department_id}")
        print(f"  Department Name: {new_department_name}")
        print(f"  Email: {new_email}")
        print(f"  Contact Details: {new_contact}")

        confirm = input("Save changes? (yes/no): ").strip().lower()
        if confirm == "yes":
            employee.update(
                name=new_name,
                email=new_email,
                department_id=new_department_id,
                department_name=new_department_name,
                contact_details=new_contact
            )
            print(f"\nEmployee ID '{employee_id}' has been updated successfully.")
        else:
            print("\nUpdate cancelled. No changes were made.")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    # Add sample employees for demonstration
    manager.add_employee(Employee("101", "Alice", "alice@mail.com", "D01", "IT", "12345678"))
    manager.add_employee(Employee("102", "Bob", "bob@mail.com", "D02", "HR", "87654321"))
    manager.update_employee()