import unittest
from add_employee import Employee, EmployeeManager  # Adjust the import if your file name is different

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee_valid(self):
        emp = Employee("S000011", "Test User", "test@mail.com", "IT201", "Information Technology", "12345678")
        self.manager.employees.append(emp)
        self.assertEqual(len(self.manager.employees), 1)
        self.assertEqual(self.manager.employees[0].name, "Test User")

    def test_validate_employee_id(self):
        self.assertTrue(self.manager.validate_employee_id("S000012"))
        self.assertFalse(self.manager.validate_employee_id(""))

    def test_validate_name(self):
        self.assertTrue(self.manager.validate_name("Alice"))
        self.assertFalse(self.manager.validate_name("Alice123"))

    def test_validate_email(self):
        self.assertTrue(self.manager.validate_email("alice@mail.com"))
        self.assertFalse(self.manager.validate_email("alicemail.com"))

    def test_validate_contact_details(self):
        self.assertTrue(self.manager.validate_contact_details("12345678"))
        self.assertFalse(self.manager.validate_contact_details("abc123"))

if __name__ == '__main__':
    unittest.main()