from torch import true_divide
from labling_tool import *
import sys
sys.path.append('/home/sayi/workspace/pii/I_want_PII_NER/res')
from token_base import dont_care, should_check, others
from random_base import vast_cities, cities, do, gun, gu

root_path = '/home/sayi/workspace/pii/'
project_path = root_path + 'I_want_PII_NER/'

insurance_lable = "res/insurance_labled"
intergrated = "res/intergrated_sangheon.tsv"
test = "res/test.tsv"
train = "res/train.tsv"
all_intergrated = "C:/Exception/new_one.tsv"
result = "C:/Exception/I_want_PII_NER/res/result"
qa_lable = "res/QAlable"
out_file = "res/filling.kt"
token_label = "res/token_label_origin.tsv"
token_label = "res/token_label.tsv"
kssed = "res/kssed.tsv"
file_path = project_path + "res/duplabeld.tsv"

def is_city(token):
    city_base = vast_cities + cities + do + gun + gu
    for city_part in city_base:
        if token in city_part:
            return True
    return False
other_city = set()

for other in others:
    stripped_other = other
    if "##" in other:
        stripped_other = other.strip('##')
    if is_city(stripped_other):
        other_city.add(other)
        
with open(project_path + token_label, "r", encoding="utf-8") as file, open(project_path + kssed, "r", encoding="utf-8") as kssed_file, open(project_path + out_file, "w", encoding="utf-8") as edited_file:
    total_cnt = 0
    edit_cnt = 0
    changed = ''
    kssed_file_lines = [kss_line for kss_line in kssed_file]
    for line_idx, line in enumerate(file):
        tokens, labels = splitTokenAndLable(line)
        total_cnt += 1
        tmp = [token + ' ' + labels[i] for i, token in enumerate(tokens)]
            # tmp.append(token)
        tmp = ' '.join(tmp)
        # if total_cnt == 0:
        if 0 < total_cnt < 10:
            print(tmp)
            print(line_idx, kssed_file_lines[line_idx])
        # line = ' '.join(tokens) + '\t' + ' '.join(labels) + '\n'
        # edited_file.write(line)
    # print(print_set)