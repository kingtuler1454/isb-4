from functions.search_card_number import card_number_selection

import argparse
import json






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings_path', default='files\\settings.json',help='Путь к json файлу с данными', action='store')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument( '-card', '--card_number_search', help='Поиск номера карты по хэшу', action='store_true')
    group.add_argument('-st', '--statistic', help='Вывод зависимости времени выполненя от кол-ва потоков', action='store_true')
    args = parser.parse_args()
    data_path = args.data_path

    with open(data_path) as jf:
        settings = json.load(jf)


    if args.card_number_search:
       card_number_selection(settings["last_card_numbers"],settings["bins_file"],settings["hash_file"], settings["processes_amount"])

    else:
        print("is something wrong")

if __name__ == "__main__":
   card_number_selection('5274',
           '437783',                
'e537d605a9f957a2c6ccb8cb2bb59537675e048c7ef78f86389a333d54feb154270a0f9df684f2b0d0e30c4eee9403bfd53b8e32af89f6fba9fd16aafdfa7420'

)