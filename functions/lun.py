def lun(number: str) -> bool:
    """Функция алгоритма Луна
    number - номер карты
    вернёт true если номер прошёл проверку и false иначе
    """
    if number:
        number = list(reversed(number))
        for i in range(len(number)):
            if i % 2 == 1:
                if int(number[i]) * 2 >= 10:
                    two_numbers = list(str(int(number[i]) * 2))
                    number[i] = int(two_numbers[0]) + int(two_numbers[1])
                else:
                    number[i] = int(number[i]) * 2
        s = 0
        for i in range(1, len(number)):
            s += int(number[i])
        c = 10 - ((s % 10) % 10)
        if str(c) == number[0]:
            print('Номер карты прошел алгоритм Луна')
            return True
        print('Номер карты не прошел алгоритм Луна')
        return False
    print('Неккоректный номер')
    return False
