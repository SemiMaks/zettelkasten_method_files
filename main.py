import os
import pathlib
from pathlib import Path

from art import *

tprint('zettelkasten', font='bulbhead')
path = Path(pathlib.Path.cwd(), 'notes', 'file.txt')
print('Путь к директории с заметками:')
print(str(path))
print(
    'Готов создать заметку - нажми 1\nХочешь поискать в записях - нажми 2\nХочешь править имеющуюся - нажми 3')
print('-> ', '')
res = int(input())


def rewrite(file):
    print('Вы сделали следующую запись:', end='')
    with open(file, encoding='utf-8') as f_h:
        for line in f_h:
            print(line)
    os.rename('notes/file.txt', 'notes/' + name_note)


try:
    if res == 1:
        print('Ваш выбор:', res)
        with open(path, 'w', encoding='utf-8') as f:
            text_title = input('Название заметки:')
            name_note = text_title + '.txt'
            f.write('Название: ' + text_title)
            text_content = input('Заметка:')
            f.write('\nКонтент: ' + text_content)
            text_hesh = input('Хэш теги:')
            f.write('\nХэштег: ' + text_hesh)

        rewrite('notes/new.txt')

    elif res == 2:
        print('Ваш выбор:', res)
        print('Имеющиеся файлы:')
        print(os.listdir('notes'))
        search = input('Введите название искомого файла:')

    elif res == 3:
        print('Ваш выбор:', res)
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
