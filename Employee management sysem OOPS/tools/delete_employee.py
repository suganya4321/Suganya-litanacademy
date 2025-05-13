class Employee:
    def __init__(self, employee_id, name, department_name):
        self.employee_id = employee_id
        self.name = name
        self.department_name = department_name

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department_name}"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def delete_employee(self):
        print("\n--- Delete Employee ---")
        if not self.employees:
            print("No employee records available to delete.")
            return

        employee_id = input("Enter Employee ID to delete: ").strip()
        found_index = next((i for i, emp in enumerate(self.employees) if emp.employee_id == employee_id), None)

        if found_index is not None:
            found_employee = self.employees[found_index]
            print(f"\nEmployee Details to Delete:\n  {found_employee}")
            confirmation = input("\nAre you sure you want to delete this employee? (yes/no): ").strip().lower()
            if confirmation in ['yes', 'y']:
                del self.employees[found_index]
                print(f"Employee with ID '{employee_id}' has been successfully deleted.")
            elif confirmation in ['no', 'n']:
                print(f"Employee with ID '{employee_id}' has not been deleted.")
        else:
            print(f"Error: Employee not found with ID '{employee_id}'.")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    # Add sample employees for demonstration
    manager.add_employee(Employee("101", "Alice", "IT"))
    manager.add_employee(Employee("102", "Bob", "HR"))
    manager.delete_employee()