# Выбрал процедурный и структурный подход, так как считаю его более читаемым для всех пользователей.
def mult(number):
    for i in range(1, 10):
        print(f'{number} * {i} = {number * i}')


mult(5)
