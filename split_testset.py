from lib2to3.pgen2 import token
import sys
sys.path.append('C:\\Exception\\I_want_PII_NER\\res')

import csv
from sklearn.model_selection import train_test_split
from res.labling_tool import *

file_path = 'res/intergrated_sangheon.tsv'
file_path = "res/filling.kt"
test_path = 'res/test.tsv'
train_path = 'res/train.tsv'
remain_lables = ['SS_AGE-B', 'SS_BRAND-B', 'SS_WEIGHT-B', 'SS_BIRTH-B', 'SS_LENGTH-B', 'SS_NAME-B', 'ID_PHONE-B', 'ID_INUM-B', 'ID_ACCOUNT-B', 'ID_CARD-B']

def preprocess_lables(matrix_tokens, matrix_lables):
    lable_set = set()
    raw_lable_set = set()
    for i, lables in enumerate(matrix_lables):
        lables = lables.split()
        tokens = matrix_tokens[i].split()
        raw_lable_set.update(lables)
        is_valid_lable(lables, tokens)
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
    
with open(file_path, 'r', encoding='UTF-8') as res_file, open(train_path, 'w', newline='', encoding='UTF-8') as train, open(test_path, 'w', newline='', encoding='UTF-8') as test:
    ttrain = csv.writer(train, delimiter='\t')
    ttest = csv.writer(test, delimiter='\t')
    tokens, lables = preprocess(res_file)
    preprocess_lables(tokens, lables)
    train_token, test_token, train_lable, test_lable = train_test_split(tokens, lables, test_size=0.2, shuffle=True, random_state=42)
    for a in range(len(train_token)):
        ttrain.writerow([train_token[a], train_lable[a].replace('\n',"")])
    for a in range(len(test_token)):
        ttest.writerow([test_token[a], test_lable[a].replace('\n',"")])