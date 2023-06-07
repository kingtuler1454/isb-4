import argparse
import json
import logging

from functions.search_card_number import card_number_selection
from functions.luhn import luhn
from functions.statistic import get_stats


logger = logging.getLogger()
logger.setLevel("INFO")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-set",
        "--settings_path",
        default="files\\settings.json",
        help="Путь к json файлу с данными",
        action="store",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-card",
        "--card_number_search",
        help="Поиск номера карты по хэшу",
        action="store_true",
    )
    group.add_argument(
        "-l",
        "--luhn_alorithm",
        help="Проверить номер карты по алгоритму Луна",
        action="store_true",
    )
    group.add_argument(
        "-st",
        "--statistic",
        help="Сделать график зависимости времени работы от количества ядер",
        action="store_true",
    )
    args = parser.parse_args()
    data_path = args.data_path
    number_card = None
    with open(data_path) as jf:
        settings = json.load(jf)

    if args.card_number_search:
        number_card = card_number_selection(
            settings["last_card_numbers"],
            settings["bins_file"],
            settings["hash_file"],
            settings["processes_amount"],
        )
    if args.lun_alorithm:
        luhn(number_card)
    if args.statistic:
        get_stats(settings)
    else:
        logging.error("Неккоректный ввод")
