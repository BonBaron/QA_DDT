DDT тест публичного API геокодинга openstreetmap.org
Тестируется прямое (адрес -> координаты) и обратное (координаты -> адрес) геокодирование.

Для проведения тестирования нужно создать excel файл с адресами
и координатами. Для корректной работы excel файл должен находиться
в одной директории с файлом теста. Сравниваются координаты в файле и ответ API
при несоответствии выводится сообщение об ошибке.
