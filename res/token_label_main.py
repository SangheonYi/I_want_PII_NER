from labling_tool import *
import sys
sys.path.append('/home/sayi/workspace/pii/I_want_PII_NER/res')
from token_base import dont_care, should_check, others

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
token_label = "res/token_label.tsv"
file_path = project_path + "res/duplabeld.tsv"
    
with open(project_path + token_label, "r", encoding="utf-8") as file, open(project_path + out_file, "w", encoding="utf-8") as edited_file:
    cnt = 0
    changed = ''
    
    check_label =['d', 'd', 'd']
    [   
    #   other
    
    # doncare

    # check
      
]
    check_chars =[
    # '##각',
     '##가',
    #  '##강', 
    #  '##가요', '##게', '##고', '##계', '##광', '##교', '##나', '##네', '##다',  '##니', '##도', '##드', '##라', '##라는', '##러', '##렌', '##로', '##리', '##만', '##모', '##보', '##번',
    # '##서', '##사',  '##센터', '##소', '##시', '##안', '##아', '##아이', '##신', '##양', '##어',  '##언', '##여',  '##에', '##예', '##영', '##원', '##이', '##음', '##접',  '##장', '##인', '##종', '##주', '##지', '##창',
    # '##트', '##한', '##포',  '##하', '로', '만','문경', '미', '분당', '사', '성산',  '신', '연제', '오산',  '은', '이', '전북', '중랑',
    # # 시, 도, 구, 군
    # '##구', '##군',  '##면','대구', '광주', '남원', '내', '도봉',  '덕', 
    #  # age
    #  '##생', 
     ]
    check_dict = {e:0 for e in check_chars}
    print_set = set()
    cnt2 = 0
    for line_idx, line in enumerate(file):
        if cnt > 1000:
            break
        tokens, labels = splitTokenAndLable(line)
        tmp = []
        for i, token in enumerate(tokens):
            # and not ( 'NAME'  in labels[i] or 'BRAND'  in labels[i] or 'AGE'  in labels[i] )\
            if token in check_chars and labels[i] != 'O' and not (check_label[0] in labels[i] or check_label[1] in labels[i] or check_label[2] in labels[i]):
                check_dict[token] = check_dict[token] + 1
                # if labels[i] in ['ID_PHONE-I', 'ID_INUM-I']:
                if line_idx in [573, 1112, 2013, ]:
                    labels[i] = 'O'
                token = '🤴' + token + '🤴'
                print_set.update(set(tokens))
                cnt += 1
            tmp.append(token + ' ' + labels[i])
            # tmp.append(token)
        tmp = ' '.join(tmp)
        if '🤴' in tmp:
            tmp += f'🕵️‍♀️ {line_idx} 🕵️‍♀️ '
            print(tmp)
        line = ' '.join(tokens) + '\t' + ' '.join(labels) + '\n'
        edited_file.write(line)
    for_print = sorted(list(print_set))
    print(check_chars, cnt, check_label)