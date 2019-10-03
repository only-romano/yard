#! Учебный модуль для файла metanit2_10.py.
#
def calculate_income(rate, money, month):
    if money <= 0:
        return 0

    for i in range(1, month+1):
        money = round(money + money * rate / 100 / 12, 2)
        return money


def main():
    rate = 10
    money = 100000
    period = 12

    result = calculate_income(rate, money, period)
    print("Параметры счёта:\n", "Сумма: ", money, "\n", "Ставка: ", rate,
          "\n", "Период: ", period, "\n", "Сумма на счёте в конце периода: ",
          result, "\nЭто тестирование\nЭто тестирование\nЭто тестирование")


if __name__ == "__main__":
    main()


# Сам модуль я не разбирала.  Хотела, конечно, сделать инпуты во все
# суммы, но какой смысл, если рэйт не рассчитать сейчас реальный, да и
# зачем.  Решила не ставить инпут.  Не понимаю, кто сейчас в долларах
# под такой процент берёт деньги.  Врушки.
#
# Первую функцию я, конечно, поняла - там защита от ошибки, если денег
# меньше нуля и, собственно, калькулятор денег, учитывающий деньги и
# проценты с них. Ну и ограничиваока до 2 знаков после запятой.
#
# Главную же функцию с указаниями - всё ясно, но один вопрос - вот
# присваевается переменная result для удобства просто или принт не
# напечатал бы результат вывода функции?  Или если бы её запустить в
# принте - она бы не сработала и не посчитала бы? Я имею ввиду:
# print(....., calculate_income(rate, money, peeiod)) - он бы выдал
# результат или функция бы не запустилась из принта?
#
# Последнее условное выражение я вообще не поняла...  То есть, если
# если имя введут "main", то запустится главная функция или что ?  Ну,
# я ещё не смотрела основной код занятия, решила сначала модуль
# разобрать.  Может там будет понятно.
#
# Конец.
#
# Не конец.  Дальше в абзаце пишут всё, я поторопилась. Оказывается,
# главная функция приведена для тестирования.  Ну, так написали, я так
# поняла что за счёт заданных параметров.  По поводу крайнего выражения,
# переменная __name__ указывает на имя файла\модуля, но для главного
# модуля эта переменная всегда __main__ независимо от имени файла -
# (Это только в этом так или везде так?  То есть это прописали в этом
# выражении и это так стало или это всегда по умолчанию?) Аааа, понятно,
# дальше пишут - если его самостоятельно, то он запустится, если как
# модуль - то тест не запустится.  Ясненько :)  Для этого и крайнее
# выражение, чтобы он запускался только когда сам исполняется - хитро.
# Конец :)