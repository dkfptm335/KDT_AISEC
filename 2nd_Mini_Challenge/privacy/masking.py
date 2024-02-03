class Masking:
    
    def masking_email(self, data):
              
        id = data.split('@')[0]
        # id의 첫 번째 문자를 제외한 나머지 문자를 '*'로 치환
        id = id[0] + '*' * (len(id) - 1)
        # id와 도메인을 '@'로 연결
        return id + '@' + data.split('@')[1]