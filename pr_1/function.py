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
        stock_value = details['Ціна'] * details['Кількість']
        print(f"Вартість залишку для {product} : {stock_value}")

calculate_stock_value(products)

def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Кількість'] < 10:
            discount = details['Ціна'] * 0.95   # 5% знижка
            print(f"Знижка для {product}: {discount} ({details['Ціна']} - 5%)")
        else:
            print(f"Для {product} знижка не застосовується, оскільки залишок становить {details['Кількість']} одиниць.")

calculate_discount(products)

def print_product_names(product_names, index=0):
    # Перевіряємо, чи індекс не виходить за межі списку
    if index < len(product_names):
        # Виводимо назву товару за поточним індексом
        print(product_names[index])
        # Рекурсивно викликаємо функцію з наступним індексом
        print_product_names(product_names, index + 1)


# Отримуємо список назв товарів
product_names = list(products.keys())
# Викликаємо рекурсивну функцію для виведення назв товарів
print_product_names(product_names)


