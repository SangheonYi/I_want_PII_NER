import sys
sys.path.append('/home/sayi/workspace/pii/I_want_PII_NER/res')
# print(sys.path)
import csv
from sklearn.model_selection import train_test_split
from res.labling_tool import *

root_path = '/home/sayi/workspace/pii/'
project_path = 'I_want_PII_NER/'
file_path = project_path + 'res/intergrated_sangheon.tsv'
file_path = project_path + "res/filling.kt"
file_path = "new_one.tsv"
file_path = project_path + "res/kssed.tsv"
file_path = "new_tagged_complete_20220411.tsv"
test_path = project_path + 'res/test.tsv'
train_path = project_path + 'res/train.tsv'
remain_lables = ['SS_AGE-B', 'SS_WEIGHT-B', 'SS_LENGTH-B', 'SS_BIRTH-B', 'SS_NAME-B', 'SS_BRAND-B',
    'AD_CITY-B', 'AD_ADDRESS-B', 'AD_DETAIL-B',
    'ID_PHONE-B', 'ID_INUM-B', 'ID_ACCOUNT-B', 'ID_CARD-B', 
    '-100']

def preprocess_lables(matrix_tokens, matrix_lables):
    lable_set = set()
    raw_lable_set = set()
    for i, lables in enumerate(matrix_lables):
        lables = lables.split()
        tokens = matrix_tokens[i].split()
        raw_lable_set.update(lables)
        if not is_valid_lable(lables, tokens):
            print(i + 1, "th sentence is invalid")
        lableExclude(lables, remain_lables)
        matrix_lables[i] = ' '.join(lables)
        lable_set.update(lables)
    print(sorted(list(lable_set)))
    print('excluded lables: ', sorted(list(raw_lable_set - lable_set)))

def preprocess(file):
    tokens, lables = [], []
    for data in file:
        data_token, data_lables = data.split('\t')
        tokens.append(data_token)
        lables.append(data_lables)
    return tokens, lables

with open(root_path + file_path, 'r', encoding='UTF-8') as res_file, open(root_path + train_path, 'w', newline='', encoding='UTF-8') as train, open(root_path + test_path, 'w', newline='', encoding='UTF-8') as test:
    tokens, lables = preprocess(res_file)
    preprocess_lables(tokens, lables)
    train_token, test_token, train_lable, test_lable = train_test_split(tokens, lables, test_size=0.2, shuffle=True, random_state=42)
    for a in range(len(train_token)):
        train.write(f'{train_token[a]}\t{train_lable[a]}\n')
    for a in range(len(test_token)):
        test.write(f'{test_token[a]}\t{test_lable[a]}\n')