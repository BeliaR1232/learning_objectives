'''В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. 
В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.'''


import requests
import json


client_id = 'c34f16ffbb4c6ae8e3fd'
client_secret = '7a79ebb5f997640f2bb297e44bdc039e'


r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                        })
j = json.loads(r.text)
token = j["token"]

artists = []

with open('dataset_24476_4.txt') as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = f'https://api.artsy.net/api/artists/{artist_id}'
        params = {'xapp_token': token}
        resp = requests.get(url, params = params).text
        data = json.loads(resp)
        artists.append(
            {'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(artists, key = lambda x: (x['birthday'], x['name'])):
    print(artist['name'])
