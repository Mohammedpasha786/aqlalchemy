from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Product

# Create SQLite database
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Populate data if empty
if session.query(Category).count() == 0:
    electronics = Category(category_name='Electronics')
    groceries = Category(category_name='Groceries')
    fashion = Category(category_name='Fashion')

    session.add_all([electronics, groceries, fashion])
    session.commit()

    products = [
        Product(product_name='Smartphone', price=699.99, category=electronics),
        Product(product_name='Laptop', price=1299.49, category=electronics),
        Product(product_name='Rice Bag', price=39.99, category=groceries),
        Product(product_name='Jeans', price=49.99, category=fashion),
        Product(product_name='T-shirt', price=19.99, category=fashion)
    ]

    session.add_all(products)
    session.commit()

# Retrieve and print data
products = session.query(Product).all()

print("📦 Products and Categories:\n")
for product in products:
    print(f"Product: {product.product_name}, Price: ₹{product.price}, Category: {product.category.category_name}")
