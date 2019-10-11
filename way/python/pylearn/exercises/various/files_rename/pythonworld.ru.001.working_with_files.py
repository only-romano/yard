#! Pythonworld.ru  Работа с файлами.  Часть 1: открытие файла.

# Решил ещё разок пробежаться по этой теме.  Когда ты мне её давал я ещё
# не полностью изучил её и пользовался только командами для записи в
# текстовый файл.  Сейчас же рассмотрю подробнее материал и изучу работу
# с файлами.

f = open('../d016/test01.txt', 'r')

# Путь может быть абсолютным или относительным.  Режимы работы с файлом:
# 'r' = открытие на чтение (является значением по умолчанию).
# 'w' = открытие на запись, содержимое файла удаляется, если файла не
# существует, создается новый.
# 'x' = открытие на запись, если файла не существует, иначе исключение.
# 'a' = открытие на дозапись, информация добавляется в конец файла.
# 'b' = открытие в двоичном режиме.
# 't' = открытие в текстовом режиме (является значением по умолчанию).
# '+' = открытие на чтение и запись.
#
# Про 'x' не понял - так он создастся только если не существует или
# наоборот - вывдаст исключение если он не существует?
#
# Режимы могут быть объединены, то есть, к примеру, 'rb' - чтение в
# двоичном режиме.  По умолчанию режим равен 'rt'.  Последний аргумент,
# encoding, нужен только в текстовом режиме чтения файла.  Этот аргумент
# задает кодировку.

f.read()        # Если аргумент пуст - весь файл читает, иначе заданное
                # колличество символов.
print("\n")

f.read(7)       # Аргумент должен быть целым числом.

# С удивлением для себя обнаружил, что прочтя однин раз часть файла,
# следующее прочтение начинается с места окончания прошлого прочтения.

f = open('../d016/test01.txt')
for line in f:      # Разбивка по абзацам.  Работает в терминале, но
        line        # не показывает результата в интерпритаторе.


#! Pythonworld.ru  Работа с файлами.  Часть 2: запись файла.

a = [str(i) + str(i-1) for i in range(20)]      # Здесь.

# Хочу научиться так же чётко и лаконично выражать мысль как выше.

f = open('../d016/test02.txt', 'w')

for index in a:
    f.write(index + "\n")

# После окончания работы с файлом его обязательно нужно закрыть.
f.close()

f = open('../d016/test02.txt', 'r')

a = [line.strip() for line in f]    # Обожаю такие записи.

print(a)

f.close()