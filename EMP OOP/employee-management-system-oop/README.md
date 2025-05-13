# Employee Management System (OOP)

This project is an Employee Management System implemented using Object-Oriented Programming principles. It allows for the management of employee and department records, providing functionalities to add, update, delete, and view employee details.

## Project Structure

```
employee-management-system-oop
├── src
│   ├── main.py               # Entry point of the application
│   ├── models                # Contains data models
│   │   ├── __init__.py       # Initializes the models package
│   │   ├── employee.py        # Employee model definition
│   │   └── department.py      # Department model definition
│   ├── services              # Contains service classes for business logic
│   │   ├── __init__.py       # Initializes the services package
│   │   ├── employee_service.py # Employee service for managing employee data
│   │   └── department_service.py # Department service for managing department data
│   ├── utils                 # Utility functions
│   │   └── __init__.py       # Initializes the utils package
│   └── data                  # Data handling
│       └── __init__.py       # Initializes the data package
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd employee-management-system-oop
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to manage employee and department records. You can add, update, delete, and view employee details, as well as manage departments.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.