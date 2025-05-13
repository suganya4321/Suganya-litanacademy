class Employee:
    def __init__(self, employee_id, name, email, department_id, department_name, contact_details):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department_id = department_id
        self.department_name = department_name
        self.contact_details = contact_details

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        print("\n--- List of Employees ---")
        if not self.employees:
            print("No employee records available.")
            return

        # Group employees by Department Name
        departments = {}
        for employee in self.employees:
            dept_name = employee.department_name
            if dept_name not in departments:
                departments[dept_name] = []
            departments[dept_name].append(employee)

        for dept_name, dept_employees in departments.items():
            print(f"\nDepartment: {dept_name}")
            print(f"{'Employee ID':<15}{'Name':<20}{'Email':<30}{'Department ID':<15}{'Contact Details':<15}")
            print("-" * 95)
            for employee in dept_employees:
                print(f"{employee.employee_id:<15}{employee.name:<20}{employee.email:<30}{employee.department_id:<15}{employee.contact_details:<15}")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employee(Employee("101", "Alice", "alice@mail.com", "D01", "IT", "12345678"))
    manager.add_employee(Employee("102", "Bob", "bob@mail.com", "D02", "HR", "87654321"))
    manager.add_employee(Employee("103", "Charlie", "charlie@mail.com", "D01", "IT", "23456789"))
    manager.list_employees()