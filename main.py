import os
import pathlib
from pathlib import Path

from art import *

res = 0
path = 0


def intro():
    global path
    tprint('zettelkasten', font='bulbhead')
    path = Path(pathlib.Path.cwd(), 'notes', 'file.txt')
    print('Путь к директории с заметками:')
    print(str(path))


def choose():
    global res
    try:
        print()
        print('Если готов:\nсоздать заметку - жми 1\nискать в записях - жми 2\nправить имеющиеся - жми 3')
        print('---> ', '')
        res = int(input())
    except Exception as er:
        print('Ошибка ', er)


def rewrite(file):
    try:
        print('Вы сделали следующую запись:')
        with open(file, encoding='utf-8') as f_h:
            for line in f_h:
                print(line, end='')
                print()
        os.rename('notes/file.txt', 'notes/' + name_note)
    except Exception as er:
        print('Ошибка ', er)


def main():
    global name_note
    intro()
    choose()
    try:
        if res == 1:
            print('Ваш выбор:', res)
            with open(path, 'w', encoding='utf-8') as f:
                text_title = input('Название заметки:')
                name_note = text_title + '.txt'
                name_note = name_note.lower()
                f.write('Название: ' + text_title)
                text_content = input('Заметка:')
                f.write('\nКонтент: ' + text_content)
                text_hesh = input('Хэш теги:')
                f.write('\nХэштег: ' + text_hesh)

            rewrite('notes/file.txt')

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


if __name__ == "__main__":
    main()
