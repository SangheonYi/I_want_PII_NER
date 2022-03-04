from asyncio.windows_events import NULL
import json
import csv

file_path = 'D:/nlp_dataset/민원(콜센터)_질의_응답_데이터/Training/금융보험/민원(콜센터)_질의응답_금융보험_사고_및_보상_문의_Training.json'
output_file = '민원(콜센터)_질의응답_금융보험_사고_및_보상_문의_Training.csv'

data = []

with open(file_path, encoding="UTF-8") as json_file, open(output_file, 'w', newline = '') as output:
    json_data = json.load(json_file)
    
    f = csv.writer(output)
    f.writerow(['도메인', '카테고리', '대화셋일련번호', '화자', '문장번호', '고객의도', '상담사의도', 'QA', '고객질문(요청)', '상담사질문(요청)', '고객답변', '상담사답변', '개체명', '용어사전', '지식베이스'])
    
    for datalow in json_data:        
        f.writerow([datalow['도메인'], datalow['카테고리'], datalow['대화셋일련번호'], datalow['화자'], datalow['문장번호'], datalow['고객의도'], datalow['상담사의도'], datalow['QA'], datalow['고객질문(요청)'], datalow['상담사질문(요청)'], datalow['고객답변'], datalow['상담사답변'], datalow['개체명 '], datalow['용어사전'], datalow['지식베이스']])