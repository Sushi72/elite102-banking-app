from database import sql_connection

def create_account(name, initial_deposit):
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, initial_deposit))
    conn.commit()
    print(f"Account has been created for {name} with a balance of ${initial_deposit}!")
    cursor.close()
    conn.close()

def deposit(account_id, amount):
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, account_id))
    cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'deposit', %s)", (account_id, amount))
    conn.commit()
    print(f"${amount} has been deposited into account {account_id}!")
    cursor.close()
    conn.close()

def withdraw(account_id, amount):
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    account = cursor.fetchone()
    if not account:
        print("Account was not found! Please try again.")
    elif account[0] < amount:
        print("Insufficient funds! Please re-enter a different amount or try again.")
    else:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, account_id))
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'withdrawal', %s)", (account_id, amount))
        conn.commit()
        print(f"${amount} has been withdrawn from account {account_id}!")
    cursor.close()
    conn.close()

def check_balance(account_id):
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, balance FROM accounts WHERE id = %s", (account_id,))
    account = cursor.fetchone()
    if not account:
        print("The account was not found! Please try again.")
    else:
        print(f"Account: {account[0]} | Balance: ${account[1]}")
    cursor.close()
    conn.close()

def list_accounts():
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, balance FROM accounts")
    accounts = cursor.fetchall()
    if not accounts:
        print("No accounts found.")
    else:
        print("\n--- All Accounts ---")
        for account in accounts:
            print(f"ID: {account[0]} || Name: {account[1]} || Balance: ${account[2]}")
    cursor.close()
    conn.close()