def input_product():
    products = {}
    while True:
        name = input("Введіть назву товару або 'stop' щоб закінчити: ")
        if name.lower() == 'stop':
            break
        price = float(input("Введіть ціну товару: "))
        stock = int(input("Введіть залишок товару на складі: "))
        products[name] = {'Ціна': price, 'Кількість': stock}

    return products

products = input_product()
print(products)