import random
from random_base import *

NEED_CHECK = "NEED_CHECK"

def str_random(start, end):
    return str(random.randint(start, end))

def fit_date_format(date):
    if len(date) < 2:
        return '0' + date
    return date

def make_random_number(start, random_size):
    result = start
    for i in range(random_size):
        result += str_random(0, 9)
    return result

def random_phone_head_number():
    head_numbers = [random.choice(cell_phone_heads), random.choice(local_numbers), "02", make_random_number("", 4), ""]
    if random.randint(0, 10) < 8:
        head_numbers[0] = cell_phone_heads[0]
    return head_numbers

def random_inum():
    inum = []
    year = str_random(1930, 2022)
    month = fit_date_format(str_random(1, 12))
    day = fit_date_format(str_random(1, 31))
    birth = year + month + day
    inum.append(birth[2:])
    inum.append(birth)
    inum.append(year + '년 ' + month + '월 ' + day + '일')
    inum.append(str_random(1800000, 4999999))
    return inum

def make_random_data(task):
    output = []
    if task == 0:
        output.append(random_inum())
    if task == 1:
        for i in range(1, 10):
            output.append(f'{i}   ' + make_random_number('', i))
    elif task == 2:
        output.append(random_phone_head_number())
    elif task == 3:
        output.append(random.choice(banks))
        output.append(random.choice(insurances))
        output.append(random.choice(cards))
    elif task == 4:
        output.append(random.choice(vast_cities))
        output.append(random.choice(cities))
        output.append(random.choice(gun))
        output.append(random.choice(gu))
        output.append(random.choice(ro))
        output.append(random.choice(dong))
        output.append(random.choice(do))
    return output
for i in range(15):
    print(make_random_data(i % 5))