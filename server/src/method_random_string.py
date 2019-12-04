import random

# функция генератор строки заданнй длинны из заданных символов
def random_string(long, symbol):
    return ''.join([random.choice(symbol) for index in range(0, long)])
