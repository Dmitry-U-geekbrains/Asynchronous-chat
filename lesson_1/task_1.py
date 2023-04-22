# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
# проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и также
# проверить тип и содержимое переменных.

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
print(type(word_1), type(word_2), type(word_3))
print(word_1, word_2, word_3)

word_1u = u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_2u = u'\u0441\u043e\u043a\u0435\u0442'
word_3u = u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(word_1u), type(word_2u)), type(word_3u)
print(word_1u, word_2u, word_3u)

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

new_word = [b'class', b'function', b'method']

for line in new_word:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
# байтовом типе.

for i in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(i, type(i), i.encode('ascii'), ' - Выполнено успешно ')
    except:
        print(i, type(i), ' - Недопустимый ввод')

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
# строкового представления в байтовое и выполнить обратное преобразование (используя
# методы encode и decode)

for i in ['разработка', 'администрирование', 'protocol', 'standard']:
    a = i.encode('utf-8', 'replace')
    b = a.decode('utf-8')
    print(i, a, b)

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.

import subprocess

for resource in ['yandex.ru', 'youtube.com']:
    args = ['ping', resource]
    my_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in my_ping.stdout:
        print(line.decode('cp866').encode('utf-8').decode('utf-8'))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

test_file = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as f_n:
    for i in test_file:
        f_n.write(i + '\n')
    f_n.seek(0)
print(f_n)

file_coding = locale.getpreferredencoding()

with open('test_file.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)
    f_n.seek(0)
