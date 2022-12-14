import fnmatch
import os
import pathlib
import time
from pathlib import Path

from art import *

res = 0
path = ""


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


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
        return result


def main():
    global name_note
    intro()
    choose()
    try:
        if res == 1:
            print('Ваш выбор:', res)
            with open(path, 'w', encoding='utf-8') as f:
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                text_title = input('Название заметки: ')
                name_note = text_title + '.txt'
                name_note = name_note.lower()
                f.write('Название: ' + text_title)
                text_content = input('Заметка: ')
                f.write('\nКонтент: ' + text_content)
                text_hesh = input('Хэш теги: ')
                f.write('\nХэштег: ' + text_hesh)
                f.write('\n\nЗапись сделана: ' + now_time + '\n')

            rewrite('notes/file.txt')

        elif res == 2:
            print('Ваш выбор:', res)
            # print('Имеющиеся файлы:')
            # print(os.listdir('notes'))
            files = os.listdir('notes')
            print('Что ищем?:')
            search = input()
            if search in files:
                print('Есть совпадение:')
                print(search)
                print('Содержание файла:')
                with open('notes/' + search, 'r', encoding='utf-8') as f:
                    for line in f:
                        print(line)
            else:
                print('Совпадений нет')


        elif res == 3:
            print('Ваш выбор:', res)
            print('Имеющиеся файлы:')
            print(os.listdir('notes'))
            print('Какой файл правим(укажите с расширением - файл.txt)?')
            rew_file = input()
            print('Выбран файл ', rew_file)
            print('Что требуется сделать?\n1 - удалить\n2 - изменить')
            try:
                shoose = int(input())
                if shoose == 1:
                    print('Удаляю заметку ', rew_file)
                    os.remove('notes/' + rew_file)
                elif shoose == 2:
                    print('Введите текст, я его добавлю:')
                    add_text = input()
                    with open('notes/' + rew_file, 'a', encoding='utf-8') as f:
                        f.write('Добавлено: ' + add_text)
            except Exception as er:
                print('Ошибка', er)
                choose()

        else:
            print('Not')
    except Exception as er:
        print('Ошибка', er)
    finally:
        print('Работа программы завершена!')


if __name__ == "__main__":
    main()
