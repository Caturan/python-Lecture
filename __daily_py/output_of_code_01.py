class Product:
    pass 

prods = []

for i in range(1, 4):
    obj = Product()
    obj.price = i * 6 
    prods.append(obj)

for prod in prods:
    if prod.price > 10:
        print(prod.price)