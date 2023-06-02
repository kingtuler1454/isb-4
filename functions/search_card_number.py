import multiprocessing as mp
import hashlib
from progress.bar import IncrementalBar

def check_number(tmp) :
    main_card_number_part=tmp[0]
    original_hash=tmp[1]
    bins=tmp[2]
    last_numbers=tmp[3]
    """
    Функция которая проверяет хеши и  принимает на вход кортеж, состоящий из данных:
    tmp[0] - подборочная серия цифр карты
    tmp[1] - хеш
    tmp[2] - бин
    tmp[3] - последние цифры карты
    возвращает номер карты если ее хеш совпадает с исходным
    иначе false
    """
    card_number = f"{bins}{main_card_number_part:06d}{last_numbers}"
    if hashlib.sha3_512(card_number.encode()).hexdigest() == original_hash: return card_number
    return False


def card_number_selection(last_card_numbers:str, bin:str, hash:str,core: int):
    """Функция которая генерирует значения для подбора номера карты, на вход принимает:
    last_card_numbers - последние цифры карты
    bin - бин
    hash - исхдный хеш
    core - количество рабочих ядер
    """
    arguments_for_check_number=[(i, hash, bin, last_card_numbers)  for i in range(10**6)]
    bar = IncrementalBar( " ", max=10**6 ) 
    with mp.Pool(processes=mp.cpu_count()) as p:
        for result in p.map(check_number,arguments_for_check_number):
                if result:
                    print(f'\nWe have found {result} and have terminated pool')
                    p.terminate()
                    break
                bar.next()


if __name__=='__main__':
     card_number_selection('5274',
           '437783',                
'e537d605a9f957a2c6ccb8cb2bb59537675e048c7ef78f86389a333d54feb154270a0f9df684f2b0d0e30c4eee9403bfd53b8e32af89f6fba9fd16aafdfa7420'

)