import pandas as pd
import unittest
from geopy.geocoders import Nominatim
'''
Данный тест-кейс проверяет прямое (адрес -> координаты) геокодирование.
Для проведения тестирования создаём excel файл с адресами
и координатами. Для корректной работы excel файл должен находиться
в одной директории с файлом теста. Сравниваются координаты в файле и ответ API
при несоответствии выводится сообщение об ошибке.  
'''
class TestAPI(unittest.TestCase):
    
    def test_direct(self):
        df = pd.read_excel('direct.xlsx')
        for index, row in df.iterrows():
            geolocator = Nominatim(user_agent='my-application', timeout=3)
            location = geolocator.geocode(row['Адреса'])
            latitude = str(location.latitude)
            longitude = str(location.longitude)
            coordinate = latitude + ", " + longitude
            try:
                self.assertEqual(row['Координаты'], coordinate)
                print(row['Адреса'], "\n", row['Координаты'] + " == " + coordinate, 'OK')
            except AssertionError as e:
                print (row['Адреса'], 'Ошибка {}'.format(e))

if __name__ == '__main__':
    unittest.main()
