class Categorization:
    
    # 주소 범주화 (시/도 + 시/군/구)
    def categorization_address(self, data):
        return data.split(' ')[0] + ' ' + data.split(' ')[1]