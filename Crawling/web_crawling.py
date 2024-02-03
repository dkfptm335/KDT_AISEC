{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 웹 크롤링 실습\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url = r'https://dhlottery.co.kr/store.do?method=topStore&pageGubun=L645'\n",
    "post_data = {'method':'topStore', 'nowPage':'1', 'rankNo':'', 'gameNo':'5133', 'drwNo':'1103', 'schKey':'all', 'schVal':''}\n",
    "response = requests.post(url, data=post_data)\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "name = soup.select('#article > div:nth-child(2) > div > div:nth-child(4) > table > tbody > tr > td:nth-child(2)')\n",
    "category = soup.select('#article > div:nth-child(2) > div > div:nth-child(4) > table > tbody > tr > td:nth-child(3)')\n",
    "address = soup.select('#article > div:nth-child(2) > div > div:nth-child(4) > table > tbody > tr > td:nth-child(4)')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
