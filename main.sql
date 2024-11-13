DROP TABLE IF EXISTS categories;

CREATE TABLE IF NOT EXISTS categories(
    cat_id SERIAL PRIMARY KEY,
    cat_name VARCHAR(150) NOT NULL UNIQUE 
);

DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS products(
    pro_name VARCHAR(20) NOT NULL,
    pro_description VARCHAR(100),
    pro_prise REAL NOT NULL,
    pro_quantity NUMERIC DEFAULT 0,
    pro_added DATE DEFAULT CURRENT_DATE,
    category INTEGER REFERENCES categories(cat_id)
);

DROP TABLE IF EXISTS comments;

CREATE TABLE IF NOT EXISTS comments(
    com_text TEXT NOT NULL,
    com_user TEXT NOT NULL,
    com_product CHAR(20) REFERENCES products(pro_name),
    com_created DATE DEFAULT CURRENT_DATE
);

INSERT INTO categories(cat_name) VALUES
    ('Dairy'),
    ('Electronics'),
    ('Clothes'),
    ('Cosmetic'),
    ('Health');

INSERT INTO products(pro_name, pro_description, pro_prise, pro_quantity, category) VALUES
    ('sut 1.6', 'Yangi sut mahsuloti', 10.000, 100, 1),
    ('headphone', 'Sifatli Apple mahsuloti', 1.000, 2),
    ('thermometer', 'Qishgi sifatli buyum', 500.000, 3),
    ('Pamada', 'Ayollarga chiroyli turadigan narsa', 50.000, 4),
    ('Metrogil', 'yuzdagi ortiqcha yomon narsalarni olib toshlaydi', 75.000, 5);



INSERT INTO comments(com_text, com_user, com_product) VALUES
    ('Juda yaxshi mahsulot', 'User1', 'sut 1.6');
	('Mahsulot juda sifatli ekan', 'User2', 'headphone'),
    ('Foydali va kerakli buyum', 'User3', 'thermometer'),
    ('Juda chiroyli mahsulot', 'User4', 'Pamada'),
    ('Yuzni tozalash uchun juda yaxshi', 'User5', 'Metrogil');

SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM comments;
