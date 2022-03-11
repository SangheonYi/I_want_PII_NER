import re
import random
import json

seperators = "[-| |.|]"
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
            if sep is not '-':
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

file = open("민원(콜센터) 질의응답_금융보험_사고 및 보상 문의_Training.json", "r")
edited_file = open("filled_phone_numbers.json", "w")
phone_pattern = re.compile('[O|0]{0,4}' + seperators + "[O|0]{3,4}" + seperators + "[O|0]{4}")
json_data = json.load(file)
for e in json_data:
    print(e)
while True:
    line = file.readline()
    if not line : break
    searched = phone_pattern.search(line)
    if searched:
        stripped = searched.group().strip()
        replaced_phone_numbers = replace_phone_number(stripped)
        if replaced_phone_numbers == NEED_CHECK:
            replaced_phone_numbers += stripped
            print(line)
        line.replace(stripped, replaced_phone_numbers)
        print(type(line))
        edited_file.write(line)
        
# file.close()
# edited_file.close()