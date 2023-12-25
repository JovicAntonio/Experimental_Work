from faker import Faker
import psycopg2

def establish_conn():
    try:
        conn = psycopg2.connect(
            dbname = "postgres",
            user = "pgsqladmin",
            password = "pgsqladminpass",
            host = "127.0.0.0",
            port = "5432",
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")


def generate_fake_user():
    fake = Faker()
    fake_user = {
        'name': fake.first_name(),
        'surname': fake.last_name(),
        'phone': fake.msisdn(),
        'date_of_birth': fake.date_of_birth(),
        'gender': fake.random_element(elements=('Male', 'Female')),
    }
    return fake_user

def generate_fake_category():
    fake = Faker()
    fake_category = {
        'category_name': fake.word(),
        'description': fake.text(),
    }
    return fake_category

def generate_fake_product(category_id):
    fake = Faker()
    fake_product = {
        'product_name': fake.word(),
        'description': fake.text(),
        'price': round(fake.random.uniform(10, 1000), 2),
        'quantity_in_stock': fake.random.randint(1, 100),
        'manufacturer': fake.company(),
        'category_id': fake.random.choice(category_id)
    }
    return fake_product

def generate_fake_order(user_ids):
    fake = Faker()
    fake_order = {
        'total_amount': round(fake.random.uniform(10, 500), 2),
        'payment_status': fake.random_element(elements=('Paid', 'Pending', 'Failed')),
        'shipping_address': fake.address(),
        'user_id': fake.random.choice(user_ids)

    }
    return fake_order

def insert_fake_data(conn):
    try:
        cursor = conn.cursor()

        for _ in range(100):
            fake_category = generate_fake_category()
            cursor.execute("""
                INSERT INTO \"CategoryTable\" (CategoryName, Description)
                VALUES (%s, %s);
            """, (
                fake_category['category_name'],
                fake_category['description']
            ))
        conn.commit()

        for _ in range(10000):
            fake_user = generate_fake_user()
            cursor.execute("""
               INSERT INTO \"Users\" (Name, Surname, PhoneNumber, DateOfBirth, Gender)
                VALUES (%s, %s, %s, %s, %s);
            """, (
                fake_user['name'],
                fake_user['surname'],
                fake_user['phone'],
                fake_user['date_of_birth'],
                fake_user['gender']
            ))

        conn.commit()

        cursor.execute("SELECT CategoryID FROM \"CategoryTable\";")
        category_id = [row[0] for row in cursor.fetchall()]
        
        for _ in range(10000):
            fake_product = generate_fake_product(category_id)
            cursor.execute("""
                INSERT INTO \"ProductTable\" (ProductName, Description, Price, QuantityInStock, Manufacturer, CategoryID)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                fake_product['product_name'],
                fake_product['description'],
                fake_product['price'],
                fake_product['quantity_in_stock'],
                fake_product['manufacturer'],
                fake_product['category_id']
            ))

        conn.commit()

        cursor.execute("SELECT UserID FROM \"Users\";")
        user_ids = [row[0] for row in cursor.fetchall()]

        for _ in range(10000):
            fake_order = generate_fake_order(user_ids)
            cursor.execute("""
                INSERT INTO \"OrderTable\" (TotalAmount, PaymentStatus, ShippingAddress, UserID)
                VALUES (%s, %s, %s, %s);
            """, (
                fake_order['total_amount'],
                fake_order['payment_status'],
                fake_order['shipping_address'],
                fake_order['user_id']
            ))

        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error: {e}")


conn = establish_conn()
insert_fake_data(conn)
conn.close()
