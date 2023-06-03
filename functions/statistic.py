from matplotlib import pyplot as plt
from time import time

from search_card_number import card_number_selection


def get_stats(settings: dict) -> None:
    """
    функция создающая статистику по кол-ву использования ядер и скорости работы скрипта
    принимает на вход  словарь с исходными данными
    """
    times = []
    for bin in settings["bins"]:
        for i in range(settings["core"]):
            start = time()
            card_number_selection(
                settings["last_numbers"], bin, settings["hash"], i + 1
            )
            times.append(time() - start)
    fig = plt.figure(figsize=(5, 5))
    plt.ylabel("Время")
    plt.xlabel("Колчество ядер")
    plt.title("Зависимость времени от скорости работы")
    plt.plot(list(x + 1 for x in range(settings["core"])), times[4:], color="red")
    plt.savefig("files\grafic")
