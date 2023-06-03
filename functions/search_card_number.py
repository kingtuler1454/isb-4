import multiprocessing as mp
import hashlib
from progress.bar import IncrementalBar
import json

def check_number(tmp: list) -> int:
    """
    Функция которая проверяет хеши и  принимает на вход список, состоящий из данных:
    tmp[0] - подборочная серия цифр карты
    tmp[1] - хеш
    tmp[2] - бин
    tmp[3] - последние цифры карты
    возвращает номер карты если ее хеш совпадает с исходным
    иначе false
    """
    main_card_number_part = tmp[0]
    original_hash = tmp[1]
    bin = tmp[2]
    last_numbers = tmp[3]
    card_number = f"{bin}{main_card_number_part:06d}{last_numbers}"
    if hashlib.sha3_512(card_number.encode()).hexdigest() == original_hash:
        return card_number
    return False


def card_number_selection(
    last_card_numbers: str, bin: str, hash: str, core: int
) -> str:
    """Функция которая генерирует значения для подбора номера карты, на вход принимает:
    last_card_numbers - последние цифры карты
    bin - бин
    hash - исхдный хеш
    core - количество рабочих ядер
    """
    arguments_for_check_number = [
        [i, hash, bin, last_card_numbers] for i in range(10 ** 6)
    ]
    bar = IncrementalBar(" ", max=10 ** 6)
    with mp.Pool(processes=core) as p:
        for result in p.map(check_number, arguments_for_check_number):
            if result:
                print(f"\nWe have found {result} and have terminated pool")
                p.terminate()
                return result
            bar.next()
