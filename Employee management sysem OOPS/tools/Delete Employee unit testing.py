import unittest
from delete_employee import Employee, EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.emp1 = Employee("101", "Alice", "IT")
        self.emp2 = Employee("102", "Bob", "HR")
        self.manager.add_employee(self.emp1)
        self.manager.add_employee(self.emp2)

    def test_add_employee(self):
        self.assertEqual(len(self.manager.employees), 2)
        self.assertEqual(self.manager.employees[0].name, "Alice")
        self.assertEqual(self.manager.employees[1].department_name, "HR")

    def test_delete_existing_employee(self):
        # Simulate user input for deleting employee "101"
        inputs = iter(["101", "yes"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        self.manager.delete_employee()
        __builtins__.input = original_input
        self.assertEqual(len(self.manager.employees), 1)
        self.assertEqual(self.manager.employees[0].employee_id, "102")

    def test_delete_nonexistent_employee(self):
        # Simulate user input for non-existent employee
        inputs = iter(["999"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        self.manager.delete_employee()
        __builtins__.input = original_input
        self.assertEqual(len(self.manager.employees), 2)  # No deletion

if __name__ == "__main__":
    unittest.main()