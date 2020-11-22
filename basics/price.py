# Функции. Задание 2 
def format_price(price):
    try:
        res = int(float(price))
    except (ValueError, TypeError):
        res = 'ERROR'
        
    return f"Цена: {res} руб."


fprice = format_price(56.24)
print(fprice)

fprice = format_price('56.24')
print(fprice)

fprice = format_price('hi')
print(fprice)
