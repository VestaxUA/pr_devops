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

def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = product.price * product.stock;
        print(f"Вартість залишку для {product.name} : {stock_value}")

calculate_stock_value(products)
