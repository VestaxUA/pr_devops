from pr_1.data_input import products


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


def find_product_by_name(products, product_name, index=0):
    # Перетворюємо ключі словника у список для рекурсивного пошуку
    product_keys = list(products.keys())

    # Умова завершення рекурсії
    if index >= len(product_keys):
        print("Товар не знайдено.")
        return

    # Перевіряємо, чи поточний ключ відповідає шуканому товару
    if product_keys[index] == product_name:
        product_info = products[product_name]
        print(f"Товар знайдено: {product_name}, Ціна: {product_info['Ціна']}, Кількість: {product_info['Кількість']}")
        return

    # Рекурсивний виклик функції з наступним індексом
    find_product_by_name(products, product_name, index + 1)


find_product_by_name(products, "Товар2")



