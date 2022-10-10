import os
import pathlib
from pathlib import Path

from art import *

path = Path(pathlib.Path.cwd(), 'notes', 'file.txt')
print(str(path))

tprint('zettelkasten', font='bulbhead')
print(
    'Готов создать заметку - нажми 1\nХочешь поискать в записях - нажми 2\nХочешь править имеющуюся - нажми 3')
print('-> ', '')
res = int(input())

try:
    if res == 1:
        print('Ваш выбор:', res)
        # name_notes = input('Название файла (имя.txt): ')
        with open(path, 'a', encoding='utf-8') as f:
            f.write('Новый текст')
    elif res == 2:
        print('Имеющиеся файлы:')
        print(os.listdir('notes'))
        search = input('Введите название искомого файла:')
    else:
        print('Not')
except Exception as er:
    print('Ошибка', er)
finally:
    print('Работа программы завершена!')
