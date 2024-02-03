import math
import random

class Replacing:
    
    def replacing_birthdate(self, data):
        # 1996-01-01 -> 1990년 01월
        year = math.floor(int(data.split('-')[0]) / 10) * 10
        month = data.split('-')[1]
        return str(year) + '년 ' + month + '월'
    
    def heuristic_pseudonymization_name(self, data):
        # 성별이 '남'이면 다음 중 하나로 변경
        # 홍길동, 임꺽정, 장길산, 이몽룡, 한석봉
        # 성별이 '여'이면 다음 중 하나로 변경
        # 성춘향, 황진이, 장희빈, 신사임당, 허난설헌
        male_names = ['홍길동', '임꺽정', '장길산', '이몽룡', '한석봉']
        female_names = ['성춘향', '황진이', '장희빈', '신사임당', '허난설헌']
        
        # 0~4 사이의 랜덤 정수 생성
        random_index = random.randint(0, 4)
        
        if data == '남':
            return male_names[random_index]
        else:
            return female_names[random_index]