from asyncio.windows_events import NULL
import re
import random

mask = "[O0]"
seperators = "- ."
cell_phone_heads = [
        "010", "011", "016", "017", "018", "019"        
]
local_numbers = [
        "020", "030", "040", "090",
        "050", "0505",
        "060", "070", "080",

        "031", "032", "033",
        "041", "042", "043", "044",    
        "051", "052", "053", "054", "055",
        "061", "062", "063", "064",]
# four_digits = [
#       "1566", "1600", "1670",
#       "1577", "1588", "1899",
#       "1522", "1544", "1644", "1661",
#       "1599",
#       "1688", "1666",
#       "1855",
#       "1811", "1877",]
NEED_CHECK = "NEED_CHECK"

def make_random_number(start, random_size):
    result = start
    for i in range(random_size):
        result += str(random.randint(0, 9))
    return result

def random_phone_head_number(head, splited_len, cellphone_probability):
    head_len = len(head)

    if head_len == 3 and splited_len == 3:
    # 휴대폰 맨 앞 번호
        if random.randint(0, 9) < cellphone_probability: # 무작위로 휴대폰 여부 결정
            return random.choice(cell_phone_heads)
    # 지역번호
        return random.choice(local_numbers)
    elif head_len == 2:
        return "02"
    # 기업 지점 통합번호
    elif len(head) == 4:
        return make_random_number("", 4)
    # 기타
    else:
        return ""

def replace_phone_number(target):
    splited = []
    result = []
    seperator = "-"

    for sep in seperators:
        if sep in target:
            seperator = sep
            if sep != '-':
                return NEED_CHECK
            splited = target.split(sep)
    for i, e in enumerate(splited):
        numbers = ""
        if i == 0:
            numbers = random_phone_head_number(e, len(splited), 8)
        if not numbers or i > 0:
            numbers = make_random_number("", len(e))
        result.append(numbers)
    return seperator.join(result)

def get_phone(line):
    phone_regs = []
    for i in range(2, 0, -1):
        for j in range(4, 2, -1):
            phone_regs.append(f"[0O].{{{i}}}-.{{{j}}}-.{{3}}[0O]")
    for phone_reg in phone_regs:
        phone_pattern = re.compile(phone_reg)
        searched = phone_pattern.search(line)
        if searched:
            start = searched.start()
            end = searched.end()
            if start > 0 and line[start - 1] in ['0', 'O', '-'] :
                return NULL
            elif end < len(line) - 1 and line[end + 1] in ['0', 'O', '-'] :
                return NULL
            return searched.group().strip()
    return NULL

with open("res/phone_numbers_converted2.tsv", "w", encoding="utf-8") as edited_file, open("res/output.tsv", "r", encoding="utf-8") as file:
    i = 0
    while True:
        line = file.readline()
        if '0' in line or 'O' in line :
            searched = get_phone(line)
            if searched:
                new_phone_number = replace_phone_number(searched)
                if new_phone_number == NEED_CHECK:
                    new_phone_number += searched
                i += 1
                print(i, searched, new_phone_number)
                line = line.replace(searched, new_phone_number)
        elif not line : break
        edited_file.write(line)