# OOP-Python
# ATM Management System


This project is an ATM Management System implemented in Python. It allows users to perform various banking operations like checking balance, withdrawing money, depositing money, and creating a PIN. The system is created using the concept of classes and objects in Python.

## Features

- **Create PIN**: Users can create a secure PIN to access their account.

- **Check Balance**: Users can check their account balance.

- **Withdraw Money**: Users can withdraw a specific amount from their account, provided they have sufficient funds.

- **Deposit Money**: Users can deposit money into their account.

## How to Use

1. Run the Python script to start the ATM Management System.

2. Enter the desired option from the menu to perform the respective operation.

3. To create a PIN, choose option 1 and enter the desired PIN.

4. To check the account balance, choose option 2, and enter the correct PIN when prompted.

5. To withdraw money, choose option 3, and provide the correct PIN and the amount to be withdrawn.

6. To deposit money, choose option 4, and enter the correct PIN and the amount to be deposited.

7. To exit the system, choose option 5.

## Python Concepts Used

The project incorporates several fundamental Python concepts:

1. **Classes and Objects**: The entire system is implemented using classes and objects. The `Atm` class acts as a blueprint to create individual ATM objects representing specific accounts.

2. **Instance Variables**: The class contains instance variables `__pin` and `__balance`, which are specific to each instance (account) and are hidden from direct access.

3. **Constructor**: The `__init__` method serves as a constructor that initializes the instance variables when a new ATM object is created.

4. **Methods**: The class includes various methods like `menu`, `create_pin`, `check_balance`, `withdraw_money`, and `deposit`, representing different ATM operations.

5. **User Input and Control Flow**: The program uses `input()` to take user input and `if-elif-else` statements to control the flow of execution based on the user's choice.

6. **String Formatting**: String formatting is used in the `__str__` method to represent account details as a formatted string.

7. **Encapsulation**: By using the `__` prefix for instance variables, they are encapsulated, making them private and inaccessible from outside the class.

8. **Inheritance and Method Overriding**: Although not explicitly demonstrated in this code, classes in Python support inheritance, allowing a child class to inherit attributes and methods from a parent class. If required, method overriding can be used to modify the behavior of inherited methods in the child class.

The ATM Management System showcases the versatility of Python and how it can be used to create practical and user-friendly applications. Feel free to explore and modify the code to suit your requirements.

---

Hope you find this Readme file comprehensive and helpful! If you have any questions or need further assistance, don't hesitate to reach out. Happy coding! 🚀🐍
