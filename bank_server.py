import mysql.connector
import socket

mydb = mysql.connector.connect(host='localhost', user='root', password='Vikash04', database='bank_management')

def handle_open_account(client_socket):
    n = client_socket.recv(1024).decode()
    n, ac, db, add, cn, ob = n.split(',')
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = 'INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)'
    sql2 = 'INSERT INTO amount VALUES (%s, %s, %s)'
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data Entered successfully")

def handle_deposit_amount(client_socket):
    amount_info = client_socket.recv(1024).decode()
    amount, ac = amount_info.split(',')
    a = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    updated_balance = result[0] + int(amount)
    sql = 'UPDATE amount SET balance = %s WHERE AccNo = %s'
    d = (updated_balance, ac)
    x.execute(sql, d)
    mydb.commit()
    client_socket.send(str(updated_balance).encode())  

def handle_withdraw_amount(client_socket):
    amount_info = client_socket.recv(1024).decode()
    amount, ac = amount_info.split(',')
    a = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    updated_balance = result[0] - int(amount)
    sql = 'UPDATE amount SET balance = %s WHERE AccNo = %s'
    d = (updated_balance, ac)
    x.execute(sql, d)
    mydb.commit()
    client_socket.send(str(updated_balance).encode())  


def handle_check_balance(client_socket):
    ac = client_socket.recv(1024).decode()
    a = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    client_socket.send(str(result[0]).encode()) 

def handle_display_details(client_socket):
    ac = client_socket.recv(1024).decode()
    a = 'SELECT * FROM amount WHERE AccNo = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    if result:
        formatted_details = f"Name: {result[0]}, Account No: {result[1]}, Balance: {result[2]}"
        client_socket.send(formatted_details.encode())
    else:
        client_socket.send("Invalid account number".encode()) 

def handle_close_account(client_socket):
    ac = client_socket.recv(1024).decode()
    sql1 = 'DELETE FROM account WHERE AccNo = %s'
    sql2 = 'DELETE FROM amount WHERE AccNo = %s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()

def process_request(data):
    if data.lower().strip() == '1':
        return "OpenAcc"
    elif data.lower().strip() == '2':
        return "DepositAmount"
    elif data.lower().strip() == '3':
        return "WithdrawAmount"
    elif data.lower().strip() == '4':
        return "Balcheck"
    elif data.lower().strip() == '5':
        return "Disdetails"
    elif data.lower().strip() == '6':
        return "CloseAcc"
    else:
        return "Invalid request"

def bank_server():
    host = socket.gethostname()
    port = 5002
    
    server_socket = socket.socket()
    server_socket.bind((host, port))
  
    server_socket.listen(1)

    print("Bank server started...")

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        
        if not data or data.lower().strip() == 'exit':
            break
        
        response = process_request(data)

        if response == 'OpenAcc':
            handle_open_account(conn)
        elif response == 'DepositAmount':
            handle_deposit_amount(conn)
        elif response == 'WithdrawAmount':
            handle_withdraw_amount(conn)
        elif response == 'Balcheck':
            handle_check_balance(conn)
        elif response == 'Disdetails':
            handle_display_details(conn)
        elif response == 'CloseAcc':
            handle_close_account(conn)
        else:
            conn.send("Invalid request".encode())

    conn.close()

if __name__ == '__main__':
    bank_server()