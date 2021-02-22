#####################################################################
# Course: Basics of database systems
# Student: Aino Solin
# Date: 22.2.2021
# Collaboration and references, name and type:
# Manipulating SQL DB with Python: https://www.freecodecamp.org/news/connect-python-with-sql/
# Inserting Rows to SQL DB from PD Dataframe: https://www.dataquest.io/blog/sql-insert-tutorial/

# Final Project: Restaurant Database Management

import mysql.connector
import pandas as pd
import sys

# Connect to database

def MenuApp():
    print("What would you like to do?")
    print("1) Establish SQL Connection to a specific DB")
    print("2) Insert data into SQL table from CSV")
    print("3) Query Data from SQL table")
    print("4) List all tables in DB")
    print("5) Display Menu and prices")
    print("6) Display Opening Hours")
    print("7) Display recent orders")
    print("0) Exit")
    print("####################################")
    choice = int(input("Your selection: "))
    return choice

def ExQuery(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Query successful")
    return None

def SQLDBConnection():
    host = input("Host: ")
    user = input("User: ")
    psw = input("Enter SQL password: ")
    db_name = input("Enter database name: ")
    connection = mysql.connector.connect(
      host=host,
      user=user,
      password=psw,
      database = db_name
    )
    cur = connection.cursor()
    print("Connection establised.")
    return connection

def LoadData(filename):
    path = input("Give path for folder: ")
    data = pd.read_csv(path+filename, sep=",", error_bad_lines=False)
    dataframename = str(filename[:-4])
    df = pd.DataFrame(data)
    print("Data loaded: ")
    print(df)
    return df, dataframename

def QueryData(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def InsertDataFrame(df, dfname, connection):
    cursor = connection.cursor()
    lista = list(df.itertuples(index=False, name=None))
    if dfname == "customers":
        for i, row in df.iterrows():
            query = "INSERT INTO customers(cust_id, cust_name, cust_email) VALUES(" + "%s,"*(len(row)-1) + "%s);"
            cursor.execute(query, tuple(row))
            connection.commit()
    elif dfname == "branch":
        for i, row in df.iterrows():
            query = "INSERT INTO branch(branch_id, address, city, postcode, state, country) \
                    VALUES(" + "%s," * (len(row)-1) + "%s);"
            cursor.execute(query, tuple(row))
            connection.commit()
    elif dfname == "bushours":
        for i, row in df.iterrows():
            query = "INSERT INTO bushours(bh_id, open, close, weekday, branch_id) \
                    VALUES(" + "%s," * (len(row)-1) + "%s);"
            cursor.execute(query, tuple(row))
            connection.commit()
    elif dfname == "orders":
        for i, row in df.iterrows():
            query = "INSERT INTO orders(order_id, order_placed, order_total, customer_id, branch_id) \
                    VALUES(" + "%s," * (len(row)-1) + "%s);"
            cursor.execute(query, tuple(row))
            connection.commit()
    elif dfname == "menuitem":
        for i, row in df.iterrows():
            query = "INSERT INTO menuitem(item_id, item_name, price, size) \
                    VALUES(" + "%s," * (len(row)-1) + "%s);"
            cursor.execute(query, tuple(row))
            connection.commit()
    elif dfname == "orderline":
        for i, row in df.iterrows():
            query = "INSERT INTO orderline(order_id, menu_item, price, qty) \
                    VALUES(" + "%s," * (len(row)-1) + "%s);"
            cursor.execute(query, tuple(row))
            connection.commit()
    cursor.close()
    return None
        
def MainProgram():
    print("𝑹𝒆𝒔𝒕𝒂𝒖𝒓𝒂𝒏𝒕 𝑫𝒂𝒕𝒂𝒃𝒂𝒔𝒆 𝑺𝒚𝒔𝒕𝒆𝒎")
    print("####################")
    while(True):    
        choice = MenuApp()
        if (choice == 1):
            print("ESTABLISH CONNECTION")
            connection = SQLDBConnection()
        elif (choice == 2):
            print("INSERT DATA")
            filename = input("Give filename as 'filename.csv': ")
            dfdata = LoadData(filename)
            dfname = dfdata[1]
            df = dfdata[0]
            InsertDataFrame(df, dfname, connection)
        elif (choice == 3):
            print("CUSTOM QUERY")
            query = input("Enter SQL Query: ")
            results = QueryData(connection, str(query))
            for result in results:
                print(result)
        elif (choice == 4):
            print("LIST ALL TABLES:")
            results = QueryData(connection, "SHOW TABLES")
            for result in results:
              print(result)
        elif (choice == 5):
            print("MENU AND PRICES:")
            query = "SELECT item_name, size, price FROM menuitem;" 
            results = QueryData(connection, str(query))
            for result in results:
                print(result)
        elif (choice == 6):
            print("OPENING HOURS")
            branch = input("Which branch (1-5)?: ")
            query = "SELECT weekday, open, close FROM bushours where branch_id = {};".format(branch)
            print(query)
            results = QueryData(connection, str(query))
            for result in results:
                print(result)
        elif (choice == 7):
            print("RECENT ORDERS")
            query = "SELECT orderline.order_id, menuitem.item_name, orderline.qty, menuitem.size, orderline.price, \
                                        customers.cust_name, orders.order_placed FROM orderline INNER JOIN orders ON \
                                        orders.order_id = orderline.order_id \
                        INNER JOIN menuitem ON orderline.menu_item = menuitem.item_id \
                        INNER JOIN customers ON orders.customer_id = customers.cust_id \
                        ORDER BY order_placed \
                        DESC LIMIT 10;"
            results = QueryData(connection, str(query))
            for result in results:
                print(result)
        elif (choice == 0):
            print("Closing the application and breaking connection to database.")
            sys.exit(0)
            break
        else:
            print("Could not recognize selection, please try again.")
    connection.close()
    return None

MainProgram()
