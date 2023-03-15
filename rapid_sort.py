import timeit
import time
import random
from prettytable import PrettyTable

def is_sorted(data) -> bool:
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data) -> list:
    while not is_sorted(data):
        random.shuffle(data)
    return data

mult= [10, 100, 1000, 10000, 100000]
temps = []
for i in range(len(mult)):
    a = []
    for j in range(mult[i]):
        a.append(random.randint(-1000,1000))
    temps.append(timeit.timeit("bogosort(a)",setup="from __main__ import bogosort, a", number=1))
    
table= PrettyTable(["Nombre d'éléments", "Temps de tri"], padding_width=5)
table.title = "Quantum Bogosort"
for k in range(len(mult)):
    table.add_row([mult[k], temps[k]])       #notation scientifique a 3chiffres après la virgule
table.align["Nombre d'éléments"] = "l"
table.align["Temps de tri"] = "r"

print(table)
