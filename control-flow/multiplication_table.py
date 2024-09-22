number = int(input("enter a number to see its multiplication table: "))
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
