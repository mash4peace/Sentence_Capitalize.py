import csv
from HangmanGame import Cart
from HangmanGame.Cart.bussiness import  Product
FILENAME = "products.csv"

def get_product():
    products = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            product = Product(row[0], float(row[1]), int(row[2]))
            products.append(product)
    return products
