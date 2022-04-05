import sys
sys.path.append('/home/sayi/workspace/pii/I_want_PII_NER/res')
print(sys.path)
from res.labling_tool import *
import re
from res.Sentence import Sentence

root_path = '/home/sayi/workspace/pii/'
project_path = root_path + 'I_want_PII_NER/'
file_path = 'res/intergrated_sangheon.tsv'
file_path = "res/filling.kt"
file_path = "new_one.tsv"
file_path = "res/spacing_case.tsv"
file_path = "res/kssed.tsv"
out_file = "res/duplabeld.tsv"

PRE = "pre"
POST = "post"
LEARNING = "learning"
PREDICT = "predict"
  
unclassified_set = set([])
other_set = set(['으로', '번으로', '세로', '-번으로', ')으로', ')로', '-으로', '대로', '맞으십니까?', '맞습니까?', '맞으신가요?', '맞나요?', '계좌는', '고객콜센터(', '고객센터(', '보상콜센터(', '콜센터(', '대', '이었대', '대다.', '임', '임을', '임?', '사고신고', '/개신교)의', '신모(', '신가요', '필지', '최모(', '총리(', '충인', '태평', '틀못', '평화주공', '풍납', '하구', '하는데...'])
not_other = set([
    # address 아파트, 로, 동, 호, 마을, 길, 번지, 역, 타워, 층, 시티, 쌍, 대, 산, 밸리, 빌딩, 롯데, 단지, 지하, 방, 카페, 신,
    '한솔센트럴파크', '차아파트지점', '단지아파트아파트', '차아파트', '상계주공아파트', '단지아파트', '가현대아파트', '차아파트입니까?', '차e-편한세상아파트', '리선명아파트',
     '관광로', '올림픽로', '방배천로', '동소문로', '부일로', '답십리로', '수표로', '연서로', '신흥로', '방축로',  '메트로팔레스', '당산로', '행원로', '북성로', '안산천동로', '설촌로', '태복산로', '통일로', '서동로', '광교중앙로', '부산대학로', '김포대로', '창훈로', '봉명로', '서초대로', '푸른들판로', '감포로', '중앙로', '서둔로', '남부순환로', '강남대로', '언주로', '동편로', '산본로', '월계로', '천도로', '산성로', '학산로', '호로', '여의대방로', '조마루로', '운천로', '동으로', '산본천로', '번길로', '대림로', '동일로', '평촌대로', '호국로', '가람로', '소양로', '고산자로', '군분로', '천혜로', '만리산로', '색달로', '회기로', '창해로', '충장로', '동패로', '칠십팔키로', '동계천로', '독정이로', '와우산로', '양화로', '충무로', '메타프로방스', '전포대로', '길로', 
     '동역에서', '삼선동', '동', '동맞습니까?', '동이요.', '양평동', '노원동', '명동', '동지점', '동,', '평화동', '당산동', '효자동', '자산동', 
    '월계삼호', '호입니다.', '호호요.', '항호', '용호', '호입니다', '호계매곡', '금호산', '호선', '호.', '호,', '천호', '호요.', '호', '(용호', '호이고', '산호그린',
    '산내마을', '은빛마을', '장재리용연마을휴먼시아', '중산마을', '백마마을', '청송마을현대',
    '하오개길', '장덕북길', '길', '나길', '안길', '번길', '산양큰길', '번길입니다.', '길맞습니까?', '가길', '신길', '길요.', '번길에서', '번안길', '라길', '화성길', 
    '번지라', '번지,', '번지', '번지입니다.', '번지는', '번지.', '번지요.',
    '시코르플래그십강남역점(강남역',
    '에이스하이엔드타워', '이앤씨벤쳐드림타워',
    '층)', '층!!', '층이요.', '층입니다.', '층에', '층.', '층입니다!', '층,', '층', '층으로',
    '마린시티',
    '쌍용아진', '쌍문', '쌍용',
    '대연', '현대', '백석예대', '다대', '대우디오슈페리움', '대저', '대능', '이화여대', '대명',
    '당산', '독산', '용산', '산', '연산', '철산', '송당리산', '낙산성곽서',
    '우림라이온스밸리',
    '노블레스빌딩',
    '롯데', '롯데인벤스',
    '차단지', '단지', '유통단지',
    '지하',
    '우방', '교방남', '방화', '방배',
    '카페',
    '신설', '신암', 
    '덕명', '풍덕천',



    # age 살, 세, 개월
    '살이고,', '살밖에', '살의', '살이다', '살이구요..', '살이잖아!', '살이라니', '살많다', '살...', '살이래..', '살이다.', '살인데', '살이라며', '살', '살이고', '살이니', '살!!', '살이되어', '살인가?', '살이라고', '살인', '살이잖아', '살!', '살에', '살이지만', '살이니까', '살이면', '살?', '살...ㅋ', '살입니다.', '살이라', '살이', '살..', '살.', '살,', '살은', '살이에요~', '살짜리',
    '세,', '세를', '세라고?', '세입니다.', '세)의', '세☆)', '세인데도!!!', '세,박사)', '세임,', '세인', '세야', '세면', '세),', '세의', '세다.', '세는', '세.', '세)', '세에', '세가', '세)와', '세라는', '세', '세된', '세되신', '세)가', '세에도', '세와', '세)로',
    '개월아기', '개월', '개월인', '개월이고', '개월에', '개월접어선',

    # weight
    '키로', '킬로라니.', '킬로', 'kg', 'KG', 'Kg',
    # length
    "센티", "센티", "센치", "cm",
    # birth 일, 년, 월
    '일입니다.', '일!', '일>', '일이', '일..', '일날', '일이라', '일이엇는뎀', '일?', '일', '일생', '일!!', '일은', '일입니다', '일인데', '일,', '일도', '일이더구만요', '일이야?', '일에', '일거', '일이요', '일아니야?', '일이야', '생일인데', '일이요.',
    '년', '년에', '년생',
    '월,', '월', '월평', '월.....?',

    # 번
    '번입니다', '학번', '번이요.', '번요.', '번덕', '번이요', '번가', '번출구',

    # etc
    '하안', '한화', '합포북', '행당', '홍은', '황금', '효자', '휘경',
    
])
should_check = set([
    '로', '번'
])
few_cases = set(['자양', '장기', '장림', '장위', '장전', '전원', '정릉', '정서진', '정왕', '제', '주간', '주례', '주면', '주안', '죽도시장', '중', '중계', '중곡', '지막', '진입을', '쨜', '쪽구름', '차', '차맨션', '창', '책향기로', '청평', '체육관'])
wait = set([])
def add_subword(spaced_tokens):
    for token in spaced_tokens:
        if not token.isnumeric() :
            if "이" in token and token not in other_set.union(not_other):
                wait.add(token)
            elif token not in other_set.union(not_other):
                unclassified_set.add(token)
            if token in few_cases:
                print(f'{token}👩‍🦳 in ')

def spacing(pattern, token, mode):
    searched = re.compile(pattern).search(token)
    while searched:
        searched = searched.group()
        index = token.find(searched) + 1
        if mode == POST:
            index += len(searched) - 2
        token = token[:index] + ' ' + token[index:]
        # print(f"{mode} {searched} space at {index} in {token}")
        searched = re.compile(pattern).search(token)
    return token

def spacing_until_unsearched(sentence, mode=LEARNING):
    for i, token in enumerate(sentence.tokens):
        sapced_token = spacing('[^\s\d]\d+', token, PRE)
        sapced_token = spacing('\d+[^\s\d]', sapced_token, POST)
        sapced_token = spacing('((키로)|(년생)|(Kg)|(KG)|(kg)|(cm)|(센티)|(센치))\S', sapced_token, POST)
        if sapced_token == token:
            sentence.new_tokens.append(token)
        else:
            spaced_tokens = sapced_token.split()
            if sentence.labels[i] != 'O':
                add_subword(spaced_tokens)
            if mode == LEARNING:
                sentence.duplicate_labels(i, spaced_tokens)
                # print(i, sentence.labels)
            sentence.append_new_tokens(spaced_tokens)
    is_valid_lable(sentence.labels, sentence.new_tokens)

with open(file_path, 'r', encoding='UTF-8') as res_file, open(out_file, "w", encoding="utf-8") as edited_file:
    sentences = []
    for i, line in enumerate(res_file):
        # if i > 20:
            # break
        tokens, labels = splitTokenAndLable(line)
        sentence = Sentence(tokens, labels)
        sentences.append(sentence)
        spacing_until_unsearched(sentences[-1])
        edited_file.write(sentence.get_new_line())
    unclassified_set = sorted(list(unclassified_set))
    print(unclassified_set)
    print(wait)