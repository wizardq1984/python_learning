# -*- coding: utf-8 -*-
import requests
city = input('你想查询哪个城市的天气：')
req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
# print(req.status_code)
web_data = req.json()
today = web_data['data']['forecast'][0]['date']
high_temp = web_data['data']['forecast'][0]['high'][3:]
low_temp = web_data['data']['forecast'][0]['low'][3:]
weather_type = web_data['data']['forecast'][0]['type']
wind = web_data['data']['forecast'][0]['fengxiang']
wind_stre = web_data['data']['forecast'][0]['fengli'][9:13]
weather_tips = web_data['data']['ganmao']
print(city + ' 今天:%s 天气：%s' % (today, weather_type))
print('最高气温:%s 最低气温：%s' % (high_temp, low_temp))
print('风向：%s, 风力：%s' % (wind, wind_stre))
print('本周%s' % weather_tips)




