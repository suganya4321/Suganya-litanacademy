class Employee:  # Fixed class name
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

    def add_employee(self, employee):
        self.employees.append(employee)

    def validate_employee_id(self, employee_id):
        if not employee_id:
            print("Validation failed: Employee ID cannot be empty.")
            return False
        if not employee_id.isalnum():
            print("Validation failed: Employee ID must be alphanumeric.")
            return False
        return True

    def view_employee(self):
        print("\n--- View Employee Details ---")
        if not self.employees:
            print("No employee records available to view.")
            return

        employee_id = input("Enter Employee ID to view: ").strip()
        if not self.validate_employee_id(employee_id):
            return

        found_employee = None
        for employee in self.employees:
            if employee.employee_id == employee_id:
                found_employee = employee
                break

        if found_employee:
            print("\nEmployee Details:")
            print(found_employee)
        else:
            print(f"Error: Employee not found with ID '{employee_id}'.")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    # Add sample employees for demonstration
    manager.add_employee(Employee("101", "Alice", "alice@mail.com", "D01", "IT", "12345678"))
    manager.add_employee(Employee("102", "Bob", "bob@mail.com", "D02", "HR", "87654321"))
    manager.view_employee()