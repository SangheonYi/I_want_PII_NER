with open("res/non_labled", "r", encoding="utf-8") as file, open("res/outlabled", "w", encoding="utf-8") as edited_file:
    while True:
        line = file.readline()
        if not line : break
        token_count = len(line.split()) - 1
        outlable = 'O'
        for i in range(token_count):
            outlable += ' O'
        # print(ord(line[-1]), ord('\n'))
        line.replace('\n', '')
        line.strip()

        if i == 0:
            print(line + outlable, i)
            i += 1
        edited_file.write(line + outlable + '\n')
lables = ['SS_AGE', 'SS_WEIGHT', 'SS_LENGTH', 'SS_GENDER', 'SS_NAME', 'SS_BRAND', 'SS_BIRTH', 'AD_ADDRESS', 'AD_DETAIL', 'ID_PHONE', 'ID_INUM', 'ID_ACCOUNT', 'ID_CARD']