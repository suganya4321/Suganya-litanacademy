import unittest
import io
import sys
from Departmentwise_report import Employee, EmployeeManager

class TestDepartmentWiseReport(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.emp1 = Employee("S000001", "Alice", "alice@gmail.com", "IT201", "Information Technology", "98650001")
        self.emp2 = Employee("S000002", "Bob", "bob@gmail.com", "HR204", "Human Resource", "98650002")
        self.emp3 = Employee("S000003", "Charlie", "charlie@gmail.com", "IT201", "Information Technology", "98650003")
        self.manager.employees.append(self.emp1)
        self.manager.employees.append(self.emp2)
        self.manager.employees.append(self.emp3)

    def test_department_wise_report_found(self):
        # Simulate user input for department name "Information Technology"
        inputs = iter(["Information Technology"])
        original_input = __builtins__.input
        captured_output = io.StringIO()
        try:
            __builtins__.input = lambda _: next(inputs)
            sys_stdout = sys.stdout
            sys.stdout = captured_output
            self.manager.department_wise_report()
        finally:
            sys.stdout = sys_stdout
            __builtins__.input = original_input
        output = captured_output.getvalue()
        self.assertIn("Alice", output)
        self.assertIn("Charlie", output)
        self.assertIn("Total Employees: 2", output)

    def test_department_wise_report_not_found(self):
        # Simulate user input for a non-existent department
        inputs = iter(["NonExistentDept", "Information Technology"])
        original_input = __builtins__.input
        captured_output = io.StringIO()
        try:
            __builtins__.input = lambda _: next(inputs)
            sys_stdout = sys.stdout
            sys.stdout = captured_output
            self.manager.department_wise_report()
        finally:
            sys.stdout = sys_stdout
            __builtins__.input = original_input
        output = captured_output.getvalue()
        self.assertIn("Validation failed: Department not found", output)
        self.assertIn("Alice", output)  # Eventually finds the correct department

if __name__ == "__main__":
    unittest.main()