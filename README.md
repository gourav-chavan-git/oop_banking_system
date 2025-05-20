# 🏦 Bank Management System

This is a simple Python-based **Bank Management System** that allows you to manage customers, employees, and loans in a simulated environment. The system supports core banking functionalities such as deposits, withdrawals, transfers, and loan repayments.

---

## Project Structure

The project includes the following classes:

- `Bank`: Main interface to manage customers, employees, and loans.
- `Customer`: Inherits from `Person`, handles customer-related data and transactions.
- `Employee`: Inherits from `Person`, handles employee data.
- `Loan`: Represents a loan taken by a customer and includes logic to repay it.
- `Person (ABC)`: Abstract base class to unify common attributes between `Customer` and `Employee`.

---

## ✅ Features

- Create customer and employee profiles.
- Authenticate users using passwords.
- Deposit, withdraw, and transfer money between accounts.
- Create and repay loans.
- Display all customers, employees, and loans.

---

## How It Works
- Each customer and employee has a unique identifier (acc_number or emp_id).
- All authentication is password-based.
- Loans are assigned unique IDs and can be partially or fully repaid.
- All objects (customers, employees, loans) are stored in class-level lists in Bank.

## Requirements
- Python 3.x
- No external libraries required (pure Python)

## Notes
- Data is stored in memory and not persisted between runs.
- This is a basic simulation intended for educational purposes.
- Can be extended for database integration, GUI, or API development.

## Author
- Made by Gourav Ashok Chavan as part of a Python OOP exercise.


