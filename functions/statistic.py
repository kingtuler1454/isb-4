from matplotlib import pyplot as plt
from time import time

from search_card_number import  card_number_selection

def get_stats():
    times = []
    for i in range(4):
        start = time()
        card_number_selection('5274',
           '437783',                
'e537d605a9f957a2c6ccb8cb2bb59537675e048c7ef78f86389a333d54feb154270a0f9df684f2b0d0e30c4eee9403bfd53b8e32af89f6fba9fd16aafdfa7420',i+1)
        times.append(time()-start)
    print(times)
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Время')
    plt.xlabel('Колчество ядер')
    plt.title('Зависимость времени от скорости работы')
    plt.plot(
        list(x+1 for x in range(4)), times, color="red")
    plt.savefig('grafic')
if __name__=='__main__':
    get_stats()
