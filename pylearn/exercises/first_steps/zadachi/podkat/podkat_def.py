#! Подкат к программистке.


# Вариант с библиотекой.

def podkat(a):
    print("Малышка, я, кажется, влюблён, пойдём сегодня ночью гулять?)")
    right_answers = ("да конечно идём афк пошли идём мяф го игого ждала тебя"
        "гоу хочу хотела красава мечтаю давай ага супер пойдём гулять")
    for key in a:
        print(a[key])
        if str(a[key].lower()) in right_answers:
            return 'Сегодня кому-то повезло\n'
        else:
            print("Некорректный ответ, повторите попытку:")
    return 'Заебала\n'


def test_podkat(arg1, value):
    print(f'Аргумент 1: {arg1}, '
          f'ожидание: {value} |-> '
          f'результат: {podkat(arg1)}\n')


# Тесты
test_podkat({0: "Пойдём гулять"}, "Сегодня кому-то повезло")
test_podkat({0: "Нет", 1: "Отстаниь", 2: "Как ты бесишь",
             3: "Я позову ментов", 4: "Аааааааа!", 5: "Блядь, ну пиздец..",
             6: "Да конечно идём афк пошли идём мяф го игого ждала тебя"},
            "Сегодня кому-то повезло")
test_podkat({0: "Нихт", 1: "Пошёл нафиг", 2: "Ты не в моём вкусе",
             3: "Да мне пофиг", 4: "Хоть целый день спрашивай", 5: "Неа",
             6: "Давай гогого. Шутка", 7: "Иди нахер"},
            "Заебала")
