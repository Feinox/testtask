# testtask
* Для тестового задания, веб-сервис создавался при помощи фреймворка Flask.
* Открыть файлы server.py (находится в папке server), client.py, test_numbers.py (находятся в папке test) в интерпретаторе.
* Для работы сервера необходимо запустить файл server.py в интерпретаторе, пердварительно добавив фреймворк Flask.
* Терминал выдаст ссылку, * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) .
* Дописав /number и обновив страницу получаем рандомное число в интервале (1, 500) http://127.0.0.1:5000/number
* При запуске файла client.py происходит GET запрос.
* Для работы теста необходимо запустить файл test_numbers.py при помощи pytest.
* Если сгенерированное число являтся простым, то в терминале будет выведено следующее:

 test/test_numbers.py::test_number PASSED                                 [100%]257 is a prime number

============================== 1 passed in 0.67s ==============================

Process finished with exit code 0

* в ином случае:

test/test_numbers.py::test_number FAILED                                 [100%]384 is not a prime number
