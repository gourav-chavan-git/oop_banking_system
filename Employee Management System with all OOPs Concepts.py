#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      91932
#
# Created:     10-01-2025
# Copyright:   (c) 91932 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Bank Class
class Bank:
    customers = []
    employees = []
    loans = []


    def create_customer(self, acc_number, name, balance, password, phone=None, address=None):
            if not self.find_customer(acc_number):
                customer = Customer(acc_number, name, balance, password, phone, address)
                Bank.customers.append(customer)
                return f'Customer {name} with account no. {acc_number} created!:)'

            return f"Account already exists!"


    def deposit(self, acc_number, amount, password):
        customer =self.authenticate_customer(acc_number, password)
        if customer:
            return customer.deposit(amount)

        return f"account {acc_number} not found! :("

    def withdraw(self, acc_number, amount, password):
        customer = self.authenticate_customer(acc_number, password)
        if customer:
            return customer.withdraw(amount)
        return f"account {acc_number} not found! :("

    def transfer(self, from_acc_number, to_acc_number, amount, password):
        customer_from = self.authenticate_customer(from_acc_number, password)
        if customer_from:
            customer_to = self.find_customer(to_acc_number)
            if customer_to:
                return customer_from.transfer(customer_to, amount)
            return f'Receiver account {to_acc_number} not found! :('
        return f"Sender account {acc_number} not found! :("


    def create_employee(self, emp_id, name, role, salary, password, phone=None, address=None):
        if not self.find_employee(emp_id):
            employee = Employee(emp_id, name, role, salary, password, phone, address)
            Bank.employees.append(employee)
            return f'employee {name} with employee id {emp_id} created.'
        return f'employee {emp_id} already exists.'


#logic for finding employees and customers form db

    @staticmethod
    def find_customer(acc_number):
        for customer in Bank.customers:
            if customer.acc_number == acc_number:
                return customer
        return None

    @staticmethod
    def find_employee(emp_id):
        for employee in Bank.employees:
            if employee.emp_id == emp_id:
                return employee
        return None

    @staticmethod
    def find_loan(loan_id):
        for loan in Bank.loans:
            if loan.loan_id == loan_id:
                return loan
        return None


#logic for authenticating employees and customers
    @staticmethod
    def authenticate_customer(acc_number, password):
        customer = Bank.find_customer(acc_number)
        if customer and customer.password == password:
            return customer
        return None

    @staticmethod
    def authenticate_employee(emp_id, password):
        employee = Bank.find_employee(emp_id)
        if employee and employee.password == password:
            return employee
        return None


#here comes logic to create and repay loan amount taken

    def create_loan(self, acc_number, amount, password):
        customer = self.authenticate_customer(acc_number, password)
        if customer:
            loan = Loan.create_loan(acc_number, amount)
            Bank.loans.append(loan)
            return f'Loan of Rs. {amount} granted to account no. {acc_number}. Here is loan id {loan.loan_id}.'
        return f'Unable to authenticate {acc_number}.'



    def repay_loan(self, loan_id, amount, acc_number, password):
        customer = self.authenticate_customer(acc_number, password)
        if customer:
            loan = self.find_loan(loan_id)
            if loan:
                if loan.acc_number == acc_number:
                    return loan.repay(amount)
                else:
                    return f'Loan id => {loan_id} does not match with account no. {acc_number}'
            return f"Loan id => {loan_id} not found :("
        return f'Unable to authenticate {acc_number}.'


#logic for displaying all employees and cutomers from db

    def display_customers(self):
        return [customer.display_info() for customer in Bank.customers]

    def display_employees(self):
        return [employee.display_info() for employee in Bank.employees]

    def display_loans(self):
        return [loan.display_info() for loan in Bank.loans]




# Abstract Base Class for a Person
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, phone=None, address=None):
        self.name = name
        self.phone = phone
        self.address = address

    @abstractmethod
    def display_info(self):
        pass

# Customer Class inheriting Person
class Customer(Person):
    def __init__(self, acc_number, name, balance, password, phone=None, address=None):
        super().__init__(name, phone, address)
        self.acc_number = acc_number
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Rs. {amount}. Current balance is: {self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn Rs. {amount}. Current balance is: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds!"

    def transfer(self, target_customer, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_customer.balance += amount
            return f'Transferred Rs. {amount} to account no. {target_customer.acc_number}. Current balance is: {self.balance}'
        return "Sorry! insufficient funds! :("

    def display_info(self):
        return {'Customer': self.name, 'Account Number': self.acc_number, 'Balance': self.balance}

# Employee Class inheriting Person
class Employee(Person):
    def __init__(self, emp_id, name, role, salary, password, phone=None, address=None):
        super().__init__(name, phone, address)
        self.emp_id = emp_id
        self.role = role
        self.salary = salary
        self.password = password

    def display_info(self):
        return {'Employee': self.name, 'Employee ID': self.emp_id, 'Role': self.role, 'Salary': self.salary}

# Loan Class
class Loan:
    loan_number = 0  # Class-level attribute

    def __init__(self, loan_id, acc_number, amount):
        self.loan_id = loan_id
        self.acc_number = acc_number
        self.amount = amount
        self.is_repaid = False

    def repay(self, amount):
        if amount >= self.amount:
            self.is_repaid = True
            self.amount = 0
            return f'Loan id {self.loan_id} fully repaid! :)'
        else:
            self.amount -= amount
            return f"Repaid Rs. {amount}. Remaining loan amount is: {self.amount}"

    @classmethod
    def create_loan(cls, acc_number, amount):
        cls.loan_number += 1
        return cls(cls.loan_number, acc_number, amount)

    def display_info(self):
        return {'Loan ID': self.loan_id, 'Account Number': self.acc_number, 'Amount': self.amount, 'Repaid': self.is_repaid}




b1 = Bank()

print(b1.create_customer("001", "Sunil Narayan", 5000, "pass123", phone="8309325119", address="Army colony"))
print(b1.create_customer("002", "priya savare", 3000, "pass456"))
print(b1.create_employee("E001", "sam thakur", "Manager", 60000, "emp_pass123"))
print(b1.create_employee("E002", "kunal", "Clerk", 30000, "emp_pass456"))
print(b1.deposit("001", 2000, "pass123"))
print(b1.withdraw("001", 1000, "pass123"))
print(b1.create_loan("001", 5000, "pass123"))
print(b1.create_loan("002", 3000, "pass456"))
print(b1.repay_loan(1, 2000, "001", "pass123"))
print(b1.repay_loan(1, 3000, "001", "pass123"))

print(b1.transfer("001", "002", 1000, "pass123"))

print(b1.display_customers())
print(b1.display_employees())
print(b1.display_loans())
