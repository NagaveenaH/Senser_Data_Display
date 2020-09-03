import requests

def weather():
    city='Bangalore'
    url='https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02'.format(city)
    result=requests.get(url)
    ouput=result.jason()
    temprature=ouput['main']['temp']
    pressure=ouput['main']['pressure']
    humidity=ouput['main']['humidity']
    print(temprature)
    print(pressure)
    print(humidity)