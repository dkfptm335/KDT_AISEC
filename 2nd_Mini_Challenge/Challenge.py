import pandas as pd
from privacy.masking import Masking
from privacy.replacing import Replacing
from privacy.rounding import Rounding
from privacy.categorization import Categorization
from faker import Faker
from tqdm import tqdm
import warnings

warnings.filterwarnings('ignore')

masking = Masking()
replacing = Replacing()
rounding = Rounding()
categorization = Categorization()
faker = Faker("ko_KR")

data = pd.read_csv('data.csv', encoding='cp949')

# 회원번호 삭제
data.drop('회원번호', axis=1, inplace=True)

# 이름 무작위 변경
# for i in tqdm(range(len(data))):
#     original_name = data['이름'][i]
#     if data['성별'][i] == '남':
#         data['이름'][i] = faker.name_male()
#     else:
#         data['이름'][i] = faker.name_female()
        
# 이름 휴리스틱 가명화
data['이름'] = data['성별'].apply(replacing.heuristic_pseudonymization_name)

# 이메일 마스킹 (abcdefg@naver.com → ****@naver.com)
data['이메일'] = data['이메일'].apply(masking.masking_email)

# 나이 제어 라운딩 (나이 15 → 10대)
data['나이'] = data['나이'].apply(rounding.rounding_age)

# 생년월일 형식 변경 (yyyy-mm-dd → yyy0년 mm월)
data['생년월일'] = data['생년월일'].apply(replacing.replacing_birthdate)

# 주소 범주화 (시/도 + 시/군/구)
data['주소'] = data['주소'].apply(categorization.categorization_address)

# 결과 확인
print(data.head(10))

# 결과 저장
data.to_csv('[KDT_AISEC_1기] 개인정보 비식별 1차 미니 챌린지_v0.1_cp949.csv', encoding='cp949', index=False)
data.to_csv('[KDT_AISEC_1기] 개인정보 비식별 1차 미니 챌린지_v0.1_utf-8-sig.csv', encoding='utf-8-sig', index=False)