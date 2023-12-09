import requests
import json
import pprint

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=ru&'
       'apiKey=1f10d9fcb90542dd9757640309a1c71e')

def top_10_news(url: str) -> dict:
    final_dict = {}
    try:
        response = requests.get(url)
        for i in range(10):
            final_dict[i] = response.json()['articles'][i]
    except Exception:
        ('Ошибка получения информации от сервера')
    finally:
        return final_dict


# Пример вывода финального словаря
pprint.pprint(top_10_news(url))