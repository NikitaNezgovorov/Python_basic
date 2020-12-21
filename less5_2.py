import requests

url = "http://komotoz.ru/photo/zhivotnye/images/schegol/schegol_14.jpg"


response = requests.get(url)

file = open('image.jpg', 'wb')
try:
    file.write(response)
except IOError:
    pass
finally:
    file.close()


