from labling_tool import *
import sys
sys.path.append('/home/sayi/workspace/pii/I_want_PII_NER/res')

root_path = '/home/sayi/workspace/pii/'
project_path = 'I_want_PII_NER/'

insurance_lable = "res/insurance_labled"
intergrated = "res/intergrated_sangheon.tsv"
test = "res/test.tsv"
train = "res/train.tsv"
all_intergrated = "C:/Exception/new_one.tsv"
result = "C:/Exception/I_want_PII_NER/res/result"
qa_lable = "res/QAlable"
out_file = "res/filling.kt"
file_path = project_path + "res/duplabeld.tsv"

def init_paramater():
    # lable = 'ID_ACCOUNT-B'
    # new = f'{make_random_number("", 6)}번'
    # new = f'{make_random_number("", 4)}에 {make_random_number("", 6)}'

    # lable = 'ID_PHONE-B'
    # new = f'{random_phone_head_number()[0]}-{make_random_number("", 3)}-{make_random_number("", 4)}'
    # new = f'{make_random_number("", 2)}-{make_random_number("", 4)}'

    # lable = 'ID_INUM-B'
    # new = f'{random_inum()[0]}'
    # new = random_inum()[2]
    # inum_birth = random_inum()[2].split()
    # new = f'{inum_birth[0] + inum_birth[1]},{inum_birth[2]}'
    # new = f'{"".join(inum_birth)}'
    # new = f'{random_inum()[-1]}'
    # new = f'{random_inum()[0]}{random_inum()[-1]}'

    # lable = 'SS_NAME-B'
    # new = f'{random.choice(names)}이구요,'

    # lable = 'AD_DETAIL-B'
    # new = f'{random.choice(aparts)}아파트'
    # new = f'{make_random_number("", 3)}동{make_random_number("", 4)}호'
    # new = f'{random.randint(1, 9)}{make_random_number("", 2)}호요'

    lable = 'AD_ADDRESS-B'
    address_randomed = make_random_data(4)
    # new = f'{address_randomed[1]} {address_randomed[3]} {address_randomed[5]}' # 시 구 동
    new = f'{address_randomed[5]}' # 동
    # new = f'{address_randomed[3]} {address_randomed[5]}' # 구 동
    # new = f'{address_randomed[3]} {address_randomed[4]}' # 구 로
    # new = f'{address_randomed[1]} {address_randomed[5]}' # 시 동

    # pattern = '[0Ooㅇ]{6}'
    pattern = '[0Ooㅇ]{3,}동'
    return lable, new, pattern

with open(train, "r", encoding="utf-8") as file, open(out_file, "w", encoding="utf-8") as edited_file:
    cnt = 0
    i = 0
    changed = ''

    for line in file:
        i += 1
        # lable, new, pattern = init_paramater()
        # old = re.compile(pattern).search(line)
        # if old:
        #     line = reg_fill_labling(line, lable, pattern, new)
        #     cnt += 1
        #     log = f"line idx: {i} changed idx:{cnt} " + line
        #     print(log[:-1])
        #     changed += log
        # edited_file.write(line)
        # edited_file.write(insertTab(line))
    print(cnt)