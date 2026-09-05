a = input("Enter customers name: ");

print("Please enter 3 products name and price: ")

product1 = input("Product 1 name: ")
price1 = float(input("Product 1 price: "))

product2 = input("Product 2 name: ");
price2 = float(input("Product 2 price: "))

product3 = input("Product 3 name: ")
price3 = float(input("Product 3 price: "))

subtotal = round(float(price1+ price2+ price3), 2)

def discount():
    if subtotal>=5000:
        return  subtotal*(20/100)
    elif subtotal>=3000:
        return subtotal*(10/100)
    elif subtotal>=1000:
        return subtotal*(5/100)
    else:
        return 0;

print(f"\nCustomer name: {a}\n")
print(f"Product 1: {product1} \nPrice: {price1}\n")
print(f"Product 2: {product2} \nPrice: {price2}\n")
print(f"Product 3: {product3} \nPrice: {price3}\n")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount()}")
print(f"Final Total: {subtotal - discount()}")