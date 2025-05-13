class Employee:
    def __init__(self, employee_id, name, email, department_id, department_name, contact_details):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department_id = department_id
        self.department_name = department_name
        self.contact_details = contact_details

    def __str__(self):
        return (f"{self.name} ({self.email})")

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def department_wise_report(self):
        while True:
            department_name = input("Enter the Department Name to view the report: ").strip()
            if not department_name:
                print("Validation failed: Department Name cannot be empty.")
                continue
            filtered_employees = [emp for emp in self.employees if emp.department_name.strip().lower() == department_name.lower()]
            if not filtered_employees:
                print(f"Validation failed: Department not found with name '{department_name}'.")
                continue
            break

        print(f"\n--- Department-wise Report for Department Name '{department_name}' ---")
        print(f"Total Employees: {len(filtered_employees)}")
        print("Employees:")
        for emp in filtered_employees:
            print(f"  - {emp}")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employee(Employee("101", "Alice", "alice@mail.com", "D01", "IT", "12345678"))
    manager.add_employee(Employee("102", "Bob", "bob@mail.com", "D02", "HR", "87654321"))
    manager.add_employee(Employee("103", "Charlie", "charlie@mail.com", "D01", "IT", "23456789"))
    manager.department_wise_report()