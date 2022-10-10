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
    elif res == 3:
        print('Имеющиеся файлы:')
        print(os.listdir('notes'))
        print('Какой файл правим?')
        rew_file = input()
        print('Выбран файл ', rew_file)
    else:
        print('Not')
except Exception as er:
    print('Ошибка', er)
finally:
    print('Работа программы завершена!')
