import re
from random_data import *

B_LABLES = ['SS_AGE-B', 'SS_WEIGHT-B', 'SS_LENGTH-B', 'SS_BIRTH-B', 'SS_NAME-B', 'SS_BRAND-B',
    'AD_ADDRESS-B', 'AD_DETAIL-B',
    'ID_PHONE-B', 'ID_INUM-B', 'ID_ACCOUNT-B', 'ID_CARD-B']

def splitTokenAndLable(line):
    seperator = '\t'
    if seperator in line:
        tokens, lables = line.split(seperator)
        return tokens.split(), lables.split()
    print(line, f" cant split by unicode {ord(seperator)}")
    return line, []

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

def is_valid_lable(lables, tokens, b_lables=B_LABLES):
    i_lables = [b_lable[:-1] + 'I' for b_lable in b_lables]
    line = ' '.join(tokens)
    if len(tokens) != len(lables):
            print(f"different length tokens {len(tokens)} lables {len(lables)} at {line}")
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

def lableExclude(lables, remain_group):
    cnt = 0
    i_group = [remain_lable[:-1] + 'I' for remain_lable in remain_group]
    for i, lable in enumerate(lables):
        if not (lable in remain_group or lable in i_group):
            cnt += 1
            lables[i] = 'O'
    return cnt