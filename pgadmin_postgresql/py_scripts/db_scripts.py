import psycopg2
from psycopg2 import sql

dbname = "postgres"
user = "pgsqladmin"
password = "pgsqladminpass"
host = "127.0.0.0"
port = "5432"

conn = psycopg2.connect(dbname=dbname, user=user, 
        password=password, host=host, port=port)

cursor = conn.cursor()

table_name = "Users"

create_users_table = sql.SQL("""
    create table if not exists{}(
        UserID SERIAL PRIMARY KEY,
        Name VARCHAR(40),
        Surname VARCHAR(40),
        PhoneNumber VARCHAR(13),
        DateOfBirth DATE,
        Gender VARCHAR(6)
    )""").format(sql.Identifier(table_name))


cursor.execute(create_users_table)
conn.commit()

table_name = "CategoryTable"

create_category_table = sql.SQL("""
    create table if not exists{}(
        CategoryID SERIAL PRIMARY KEY,
        CategoryName VARCHAR(50) NOT NULL,
        Description TEXT
    )""").format(sql.Identifier(table_name))


cursor.execute(create_category_table)
conn.commit()

table_name = "ProductTable"

create_product_table = sql.SQL("""
    create table if not exists{}(
        ProductID SERIAL PRIMARY KEY,
        ProductName VARCHAR(100),
        Description TEXT,
        Price DECIMAL(10, 2),
        QuantityInStock INT,
        Manufacturer VARCHAR(50),
        CategoryID INT,
        FOREIGN KEY (CategoryID) REFERENCES \"CategoryTable\"(CategoryID)
    )""").format(sql.Identifier(table_name))


cursor.execute(create_product_table)
conn.commit()

table_name = "OrderTable"

create_order_table = sql.SQL("""
    create table if not exists{}(
        OrderID SERIAL PRIMARY KEY,
        UserID INT,
        OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        TotalAmount DECIMAL(10, 2) NOT NULL,
        PaymentStatus VARCHAR(20),
        ShippingAddress TEXT,
        FOREIGN KEY (UserID) REFERENCES \"Users\"(UserID)
    )""").format(sql.Identifier(table_name))


cursor.execute(create_order_table)
conn.commit()

cursor.close()
conn.close()