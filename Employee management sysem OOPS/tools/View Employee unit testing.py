import unittest
from view_employee import Employee, EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.emp1 = Employee("S000001", "Alice", "alice@mail.com", "IT201", "Information Technology", "98650001")
        self.emp2 = Employee("S000002", "Bob", "bob@mail.com", "HR204", "Human Resource", "98650002")
        self.manager.employees.append(self.emp1)
        self.manager.employees.append(self.emp2)

    def test_view_existing_employee(self):
        # Simulate user input for viewing employee S000001
        inputs = iter(["S000001"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        # Capture print output
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.manager.view_employee()
        sys.stdout = sys.__stdout__
        __builtins__.input = original_input
        self.assertIn("Alice", captured_output.getvalue())

    def test_view_nonexistent_employee(self):
        # Simulate user input for non-existent employee
        inputs = iter(["S999999"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.manager.view_employee()
        sys.stdout = sys.__stdout__
        __builtins__.input = original_input
        self.assertIn("not found", captured_output.getvalue().lower())

if __name__ == "__main__":
    unittest.main()