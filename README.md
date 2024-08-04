
# MAVY - Bank Management System

This project is a simple bank management system that consists of a client-server architecture. The client-side is built using Flask and allows users to interact with the server to perform various banking operations such as opening an account, depositing money, withdrawing money, checking balance, and more. The server-side is implemented in Python and uses MySQL as the backend database to store and manage the bank data.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- **Open Account**: Create a new bank account.
- **Deposit Money**: Deposit money into an existing account.
- **Withdraw Money**: Withdraw money from an existing account.
- **Check Balance**: Check the balance of an existing account.
- **Display Account Details**: View the details of an account.
- **Close Account**: Close an existing account.

## Requirements

- Python 3.x
- Flask
- MySQL
- MySQL Connector for Python
- HTML templates for Flask

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/YeshwanthBalaji2022/MAVY.git
   cd your-repository-name
   ```  

2. **Set up the virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL Database**:

   - Create a database named `bank_management`.
   - Create two tables: `account` and `amount`.
   - Use the following schema:

     ```sql
     CREATE TABLE account (
         Name VARCHAR(255),
         AccNo VARCHAR(255) PRIMARY KEY,
         DOB DATE,
         Address VARCHAR(255),
         Contact VARCHAR(255),
         OpeningBalance DECIMAL(10, 2)
     );

     CREATE TABLE amount (
         Name VARCHAR(255),
         AccNo VARCHAR(255) PRIMARY KEY,
         Balance DECIMAL(10, 2)
     );
     ```

5. **Update MySQL connection details**:

   - In the `bank_server.py` file, update the `host`, `user`, `password`, and `database` fields in the MySQL connection section with your MySQL credentials.

6. **Run the server**:

   ```bash
   python bank_server.py
   ```

7. **Run the client (Flask app)**:

   ```bash
   python bank_client.py
   ```

8. **Access the web application**:

   - Open a web browser and navigate to `http://localhost:5000`.

## Usage

Once the client and server are running, you can interact with the bank management system through the web interface. The operations available include opening an account, depositing and withdrawing money, checking balances, displaying account details, and closing an account.

## Database Schema

- **account**: Stores user account details such as name, account number, date of birth, address, contact number, and opening balance.
- **amount**: Stores the account balance associated with each account number.

## Project Structure

```bash
.
├── bank_client.py        # Flask client application
├── bank_server.py        # Python server application
├── templates             # HTML templates for the Flask app
│   ├── index.html
│   ├── openacc.html
│   ├── depo.html
│   ├── withd.html
│   ├── balance.html
│   ├── Details.html
│   ├── deleteAccount.html
│   ├── transfer.html
│   └── error.html
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
