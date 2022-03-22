import re
from random_data import *

def splitTokenAndLable(line):
    tokens, lables = line.split('\t')
    return tokens.split(), lables.split()

def labling(line, lable, old, new):
    tokens, lables = splitTokenAndLable(line)
    mid = len(tokens)

    if old in line:
        for j in range(mid):
            if old in tokens[j]:
                tokens[j] = tokens[j].replace(old, new)
                lables[j] = lable
        return ' '.join(tokens) + '\t' + ' '.join(lables) + '\n'
    return line

def is_valid_lable(lables, tokens):
    b_lables = ['SS_AGE-B', 'SS_BIRTH-B', 'SS_NAME-B', 'SS_BRAND-B',
    'AD_ADDRESS-B', 'AD_DETAIL-B',
    'ID_PHONE-B', 'ID_INUM-B', 'ID_ACCOUNT-B', 'ID_CARD-B']
    i_lables = [b_lable[:-1] + 'I' for b_lable in b_lables]
    line = ' '.join(tokens)
    if len(lables) != len(lables):
            print(f"different length tokens {len(lables)} lables {len(lables)} at {line}")
    for lable in lables:
        if not (lable in i_lables or lable in b_lables or lable == 'O'):
            print(f"invalid lable: {lable} at {line}")
    
def reg_labling(tokens, lables, searched, lable):
    is_begin = True
    searched_splited = searched.group().split()
    for i in range(len(tokens)):
        if searched_splited[0] in tokens[i]:
            for _ in searched_splited:
                lables[i] = lable
                if is_begin:
                    lable = lable[:-1] + 'I'
                i += 1
            return

def reg_fill_labling(line, new_lable, pattern, new):
    tokens, lables = splitTokenAndLable(line)
    searched = re.compile(pattern).search(line)

    if searched:
        reg_labling(tokens, lables, searched, new_lable)
        replaced = re.sub(pattern, new, line).split()[:len(tokens)]
        return ' '.join(replaced) + '\t' + ' '.join(lables) + '\n'
    return line

def insertTab(line):
    tokens, lables = splitTokenAndLable(line)
    return ' '.join(tokens) + '\t' + ' '.join(lables) + '\n'
