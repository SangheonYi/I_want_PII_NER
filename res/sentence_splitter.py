from labling_tool import *

insurance_lable = "res/insurance_labled"
intergrated = "res/intergrated_sangheon.tsv"
all_intergrated = "C:/Exception/new_one.tsv"
result = "C:/Exception/I_want_PII_NER/res/result"
qa_lable = "res/QAlable"
out_file = "res/kssed.tsv"


with open(all_intergrated, "r", encoding="utf-8") as file, open(out_file, "w", encoding="utf-8") as edited_file:
    cnt = 0
    i = 0
    changed = ''
    lable_set = set()
    while True:
        line = file.readline()
        if not line : break
        i += 1

        if old:
            line = reg_fill_labling(line, lable, pattern, new)
            cnt += 1
            log = f"line idx: {i} changed idx:{cnt} " + line
            print(log[:-1])
            changed += log
        edited_file.write(line)
        edited_file.write(insertTab(line))
    print(list(lable_set))
    print(cnt)