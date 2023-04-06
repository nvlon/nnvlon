#скачать requests / beutifulsoup4
import requests
from bs4 import BeautifulSoup as bs

from django.views.decorators.csrf import csrf_exempt


URL= 'http://toyboss.kg/'

HEADERS = {
    'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" ,
}

#старт
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS ,params=params)
    return req

#get data
@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='product-right')
    sausage_toyboss =[]

    for item in items:
        sausage_toyboss.append(
            {
                'title_name': item.find('div',class_='sertivicates__card-block').get_text(),
                'title_url':URL + item.find('h5').get('h5'),
                'image':URL + item.find('div', class_='sertivicates__card-img').find('img').get('src'),
            }
        )

    return sausage_toyboss
#EndParse
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code ==200:
        sausage=[]
        for page in range(0,1):
            html = get_html(f'http://toyboss.kg/ru/categories/index.htm', params= page)
            sausage.extend(get_data(html.text))
        return sausage
    else:
        raise Exception('Error in parser')
