import mysql.connector
from config import db_config

# Function to connect to the MySQL database
def connect_to_database():
    connection = mysql.connector.connect(**db_config)
    return connection

# Function to create the table
def create_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS company_strike_off (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state_name VARCHAR(100),
        date DATE,
        work_item VARCHAR(50),
        cin VARCHAR(21),
        company_name VARCHAR(255)
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def insert_into_database(data):
    connection = connect_to_database()
    cursor = connection.cursor()
    
    insert_query = '''
    INSERT INTO company_strike_off (state_name, date, work_item, cin, company_name)
    VALUES (%s, %s, %s, %s, %s)
    '''
    
    try:
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"{cursor.rowcount} records inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

