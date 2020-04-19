import pandas as pd
import unittest
from geopy.geocoders import Nominatim
'''
Данный тест-кейс проверяет обратное (координаты -> адрес) геокодирование.
Для проведения тестирования создаём excel файл с адресами
и координатами. Для корректной работы excel файл должен находиться
в одной директории с файлом теста. Сравнивается адрес в файле и ответ API
при несоответствии выводится сообщение об ошибке. 
'''
class TestAPI(unittest.TestCase):

    def test_reverse(self):
        df = pd.read_excel('reverse.xlsx')
        for index, row in df.iterrows():
            geolocator = Nominatim(user_agent='my-application', timeout=3)
            location = geolocator.geocode(row['Координаты'])
            address = str(location.address)
            try:
                self.assertEqual(row['Адреса'], address)
                print(row['Адреса'], "\n", row['Координаты'] + " == " + address, 'OK')
            except AssertionError as e:
                print ('Ошибка {}'.format(e))

if __name__ == '__main__':
    unittest.main()
