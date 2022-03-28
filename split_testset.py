import csv
from sklearn.model_selection import train_test_split

file_path = 'res/intergrated_sangheon.tsv'
file_path = "res/filling.kt"

test_path = 'res/test.tsv'
train_path = 'res/train.tsv'
tokens =[]
lables = []

with open(file_path, 'r', encoding='UTF-8') as f, open(train_path, 'w', newline='', encoding='UTF-8') as train, open(test_path, 'w', newline='', encoding='UTF-8') as test:
    ttrain = csv.writer(train, delimiter='\t')
    ttest = csv.writer(test, delimiter='\t')
    c = csv.reader(f)
    
    for data in f:
        data_token, data_lables = data.split('\t')
        tokens.append(data_token)
        lables.append(data_lables)
    
    train_token, test_token, train_lable, test_lable = train_test_split(tokens, lables, test_size=0.2, shuffle=True, random_state=42)
    
    for a in range(len(train_token)):
        ttrain.writerow([train_token[a], train_lable[a].replace('\n',"")])
    
    for a in range(len(test_token)):
        ttest.writerow([test_token[a], test_lable[a].replace('\n',"")])