
import os  # Для работы с директориями в операционной системе импортируем модуль OS



def main():
    input_func = input

    CheckDir = input_func('Введите расположение и имя директории')
    print()

    if os.path.exists(CheckDir):  # Проверяем, существует ли эта директория в нашей системе
        print('Данная директория существует')
    else:
        print('Директории', CheckDir, ' не существует.')
        os.makedirs(CheckDir)  # Создаем новую директорию с именем введенным в imput
        print('Создана директория: ' + CheckDir)

main()