import unittest
from update_employee import Employee, EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager("test_employees.csv")  # Added file_path argument
        self.emp = Employee("101", "Alice", "alicia@gmail.com", "D02", "IT", "98650001")
        self.manager.employees.append(self.emp)

    def test_update_employee_success(self):
        # Simulate user input for updating employee "101"
        inputs = iter([
            "101",        # Employee ID to update
            "Alice",      # New Name
            "D02",        # New Department Id (fixed to match expected value)
            "IT",         # New Department Name
            "alice@gmail.com", # New Email
            "98650001",   # New Contact
            "yes"         # Confirm save
        ])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        self.manager.update_employee()
        __builtins__.input = original_input

        updated_emp = self.manager.employees[0]
        self.assertEqual(updated_emp.name, "Alice")
        self.assertEqual(updated_emp.department_id, "D02")
        self.assertEqual(updated_emp.department_name, "IT")
        self.assertEqual(updated_emp.email, "alice@gmail.com")
        self.assertEqual(updated_emp.contact_details, "98650001")

    def test_update_employee_cancel(self):
        # Simulate user input for updating employee "101" but cancel at the end
        inputs = iter([
            "101",        # Employee ID to update
            "Alice",      # New Name
            "D02",        # New Department Id
            "IT",         # New Department Name
            "alice@mail.com", # New Email
            "98650001",   # New Contact
            "no"          # Cancel save
        ])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        self.manager.update_employee()
        __builtins__.input = original_input

        # Should remain unchanged
        updated_emp = self.manager.employees[0]
        self.assertEqual(updated_emp.name, "Alice")
        self.assertEqual(updated_emp.department_id, "D02")
        self.assertEqual(updated_emp.department_name, "IT")
        self.assertEqual(updated_emp.email, "alicia@gmail.com")  # Verify original email remains unchanged
        self.assertEqual(updated_emp.contact_details, "98650001")

    def test_update_employee_not_found(self):
        # Simulate user input for non-existent employee
        inputs = iter(["999"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        self.manager.update_employee()
        __builtins__.input = original_input

        # Verify no changes were made
        self.assertEqual(len(self.manager.employees), 1)
        self.assertEqual(self.manager.employees[0].employee_id, "101")

if __name__ == "__main__":
    unittest.main()