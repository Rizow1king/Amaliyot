import psycopg2

db = psycopg2.connect(
    database="test",
    user="postgres",
    host="localhost",
    password="1"
)
cursor = db.cursor()

# ------------------1-----------------
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars(
        car_id SERIAL PRIMARY KEY,
        car_name VARCHAR(100) NOT NULL,
        car_model TEXT,
        car_year INTEGER,
        car_prise NUMERIC(12, 2),
        car_exists BOOL DEFAULT TRUE
    );
    CREATE TABLE IF NOT EXISTS clients(
        client_id SERIAL PRIMARY KEY,
        client_name VARCHAR(50) NOT NULL,
        client_lastname VARCHAR(50),
        client_number CHAR(13),
        client_address TEXT
    );
    CREATE TABLE IF NOT EXISTS orders(
        order_id SERIAL PRIMARY KEY,
        car_id INTEGER REFERENCES cars(car_id),
        client_id INTEGER REFERENCES clients(client_id),
        order_date DATE NOT NULL,
        order_prise NUMERIC(12, 2)
    );
    CREATE TABLE IF NOT EXISTS employee(
        emp_id SERIAL PRIMARY KEY,
        emp_name VARCHAR(50) NOT NULL,
        emp_status VARCHAR(50),
        emp_salary NUMERIC(10, 2)
    );
''')

# -----------------2----------------------
cursor.execute('''
    ALTER TABLE clients ADD COLUMN IF NOT EXISTS email VARCHAR(100);
    ALTER TABLE clients RENAME COLUMN client_name TO name;
    ALTER TABLE clients RENAME TO mijozlar;
''')

# -----------------3----------------------
cursor.execute('''
    INSERT INTO cars (car_name, car_model, car_year, car_prise, car_exists) VALUES
    ('BMW', 'Sedan', 2024, 50000.00, TRUE);
''')

cursor.execute('''
    INSERT INTO mijozlar (name, client_lastname, client_number, client_address, email) VALUES
    ('Safobek', 'Sirojiddin ogli', '910481223', 'Altariq', 'Safobek@gmail.com');
''')

cursor.execute('''
    INSERT INTO orders (car_id, client_id, order_date, order_prise) VALUES
    (1, 1, '2024-11-13', 300.00);
''')

cursor.execute('''
    INSERT INTO employee (emp_name, emp_status, emp_salary) VALUES
    ('Azizbek', 'manager', 1000.00),
    ('Abdulvosit', 'programmer', 1200.00);
''')

# -----------------4----------------------
cursor.execute('''
    UPDATE employee SET emp_name = 'Sherdorbek' WHERE emp_id = 1;
    UPDATE employee SET emp_name = 'Umarbek' WHERE emp_id = 2;
''')

# -----------------5----------------------
cursor.execute('''
    DELETE FROM employee WHERE emp_id = 2;
''')

# -----------------6----------------------
cursor.execute("SELECT * FROM cars;")
cars = cursor.fetchall()

cursor.execute("SELECT * FROM mijozlar;")
mijozlar = cursor.fetchall()

cursor.execute("SELECT * FROM orders;")
deliverities = cursor.fetchall()

cursor.execute("SELECT * FROM employee;")
staff = cursor.fetchall()

print(f"Avtomobillar: {cars}\n"
      f"Mijozlar: {mijozlar}\n"
      f"Buyurtmalar: {deliverities}\n"
      f"Xodimlar: {staff}")

db.commit()
cursor.close()
db.close()
