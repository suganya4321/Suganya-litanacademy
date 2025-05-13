import unittest
import io
import sys
from list_employee import Employee, EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.emp1 = Employee("S000001", "Alice", "alice@mail.com", "IT201", "Information Technology", "98650001")
        self.emp2 = Employee("S000002", "Bob", "bob@mail.com", "HR204", "Human Resource", "98650002")
        self.manager.employees.append(self.emp1)
        self.manager.employees.append(self.emp2)

    def test_list_employees(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.manager.list_employees()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Alice", output)
        self.assertIn("Bob", output)
        self.assertIn("IT201", output)
        self.assertIn("HR204", output)

    def test_list_employees_empty(self):
        self.manager.employees.clear()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.manager.list_employees()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("No employee records available.", output)
        

if __name__ == "__main__":
    unittest.main()