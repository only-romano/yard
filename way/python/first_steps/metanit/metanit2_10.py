#! Учебный код по программе Метанит, Глава 2, часть 10. Модули.
#
# Теория.
# Модуль представляет из себя файл с кодом, который можно использовать в
# других программах.  Модуль создаётся в той же папке, что и основная
# программа, если же используется PyCharm то создаётся единый проект.
# Для использования модуля его надо импортировать.
#
# Чтобы обращаться к функциональности модуля, надо получить пространства
# имён модуля.  По умолчанию оно совпадает с именем модуля и можно
# обратиться по схеме : name_of_module.function_in_module() .
#
# Создадим файл модуля module.py. [дальше читай что я в файле том справа
# написала, потому-что иначе то будет не таким приключенческим и ход-->>
# моей мысли будет нарушен и выгледеть я буду глуповатой :) ] ----->>>>>
#                                                          ----->>>>>>>>
# Ооо, стоило только почитать дальше и тут всё, что я хотела - инпуты и
# прочее. 
#
# Программа Банковский счёт (копия в account.py)
import modules.module as module


def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счёта в месяцах: "))
# Нужен коммент, тут чуть не ошиблась введя дефолтное имя модуля.
    result = module.calculate_income(rate, money, period)
    print("Параметры счёта:\n", "Сумма: ", money, "\n", "Ставка: ", rate,
          "\n", "Период: ", period, "\n", "Сумма на счёте в конце периода: ",
          result, "\n\n")

if __name__ == "__main__":      # Зачем это в основном файле программы?
    main()

# Настройка пространства имён.
# 
# Можно переделать пространство имён модуля с по умолчанию на свой лад,
# так ключевое слово "as" позволяет сопоставить модуль с другим
# пространством .
import modules.circle_square as cs
cs.circle_square(5)

# Другой вариант настройки - импорт функциональности модуля в глобальное
# пространство имён текущего модуля с помощью ключевого слова from:
from modules.zadachka0003c import is_primal
print(is_primal(133))
# В данном случае импорт из модуля стороннего в глобальное пространство
# имён функции is_primal.  Поэтому можно будет использовать её без
# указания пространства имён модуля.  Можно импортировать все функции
# из модуля в глобальное пространство одним выражением:
from metanit2_9 import *
say_poop()
say_goodbye()

# Импорт в глобальное пространство имён чреват коллизиями имён функций,
# например, если в том же файле определена функция с тем же именем, то
# при вызове можно получить ошибку.  Лучше избегать импорта в глобальное
# пространство имён.                                Конец.