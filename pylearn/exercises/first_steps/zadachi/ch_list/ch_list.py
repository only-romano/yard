'''
Очень интересно конечно что получиться :) какую функцию ты напишешь.
Сохрани скрины промежуточные, Пазялюста )) 
'''

def get_ch_list(ls):
    if isinstance(ls, list) == False:
        raise ValueError()
    else:
        ns = ls[:]
        es = []
        c = -2
        a = int(len(ls)) % 2
        if a == 0:
            while ns != []:
                b = int(len(ns))  % 2
                if b == 0:
                    c += 2
                else:
                    c += 0
                sys = ns.pop(0)
                es.insert(c, sys)
        else:
            while ns != []:
                b = int(len(ns))  % 2
                if b == 0:
                    c += 0
                else:
                    c += 2
                sys = ns.pop(0)
                es.insert(c, sys)
    return es


def test_equals(arg, value):
    print(f'Аргумент: {arg}, '
          f'ожидание: {value} |-> '
          f'результат: {get_ch_list(arg)},')


# Тесты
test_equals([], [])
test_equals([1], [1])
test_equals([1, 2], [2, 1])
test_equals([1, 2, 3], [2, 1, 3])
test_equals([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])
test_equals([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5])