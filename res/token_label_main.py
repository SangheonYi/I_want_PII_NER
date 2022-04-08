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
        
with open(project_path + token_label, "r", encoding="utf-8") as file, open(project_path + out_file, "w", encoding="utf-8") as edited_file:
    total_cnt = 0
    edit_cnt = 0
    changed = ''
    [   
    #   done
    '##각', '##가', '##강',  '##가요', '##게', '##생', '##고', '##계', '##광', '##교', '##나', '##네', '##다', '##니', '##도', '##드', '##라',  '##라는', '##러', '##렌', '##로',  '##리', '##모',
    '##만', '##보', '##번', '##서', '##사', '##센터',  '##소', '##시', '##안',  '##아', '##아이',  '##신', '##양','##어',  '##언', '##여', '##에', '##예', '##영', '##원',
    # check
    #  '##이', '##음', '##접',  '##장', '##인', '##종', '##주', '##지', '##창', 
    # '##트', '##한', '##포',  '##하', '로', '만','문경', '미', '분당', '사', '성산',  '신', '연제', '오산',  '은', '이', '전북', '중랑',
    # 시, 도, 구, 군
    # '##구', '##군',  '##면','대구', '광주', '남원', '내', '도봉',  '덕', 
     # age
]
    check_chars =[
     #   done
    # '##각', '##가', '##강',  
    # '##가요', '##게', '##생', '##고', '##계', '##광', '##교', '##나', '##네', '##다', '##니', '##도', '##드', '##라',  '##라는', '##러', '##렌', '##로',  '##리', '##모',
    # '##만', '##보', '##번', '##서', '##사', '##센터',  '##소', '##시', '##안',  '##아', '##아이',  '##신', '##양','##어',  '##언', '##여', '##에', '##예', '##영', '##원',
    
    # check
    #  '##이', '##음', '##접',  '##장', '##인', '##종', '##주', '##지', '##창', 
    # '##트', '##한', '##포',  '##하', '로', '만','문경', '미', '분당', '사', '성산',  '신', '연제', '오산',  '은', '이', '전북', '중랑',
    # 시, 도, 구, 군
    # '##구', '##군',  '##면','대구', '광주', '남원', '내', '도봉',  '덕', 
     # age
     ]
    print_set = set()
    found_label = ''
    found_line_idx = set()
    check_label =['s', 'd', 'd']
    for line_idx, line in enumerate(file):
        if total_cnt > 1000:
            break
        tokens, labels = splitTokenAndLable(line)
        tmp = []
        

        # if line_idx in [10, 38, 127, 476, 480, 493]:
        #     continue
        for i, token in enumerate(tokens):
            # and not ( 'NAME'  in labels[i] or 'BRAND'  in labels[i] or 'AGE'  in labels[i] )\
            # if token in others  and 'AD_ADDRESS-I' in labels and 'AD_CITY-B' not in labels and not ( 's'  in labels[i] or 's'  in labels[i] or 's'  in labels[i]):
            if token in other_city and 'AD_CITY-B' not in labels:
                found_line_idx.add(line_idx)
                # if labels[i] in ['ID_PHONE-I', 'ID_INUM-I']:
                total_cnt += 1
                print_set.add(token)
                if line_idx in [  ]:
                # if check_label[0] in labels[i] :
                # if '확' in tokens[i + 1]:
                    edit_cnt+=1
                    labels[i] = 'AD_CITY-B'
                token = '🤴' + token + '🤴'
                found_label = labels[i]
            tmp.append(token + ' ' + labels[i])
            # tmp.append(token)
        tmp = ' '.join(tmp)
        if '🤴' in tmp:
            tmp += f'🕵️‍♀️\n{line_idx}, {found_label} 🕵️‍♀️\n'
            print(tmp)
        line = ' '.join(tokens) + '\t' + ' '.join(labels) + '\n'
        edited_file.write(line)
    print(check_chars, check_label)
    print(f'found cnt: {edit_cnt} / {total_cnt} line_cnt: {len(found_line_idx)} idx: {found_line_idx}')
    print(other_city)