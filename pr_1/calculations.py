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