import threading
import random
from time import sleep

"""
Crie um programa que recebe um número inteiro n como argumento e cria n threads.
Cada uma dessas threads deve dormir por um tempo aleatório de no máximo 5 segundos.
A main-thread deve esperar todas as threads filhas terminarem de executar para em
seguida escrever na saída padrão o valor de n. Faça a thread-mãe esperar as filhas
de duas maneiras: 1) usando o equivalente à função join em C ou Java; 2) usando
semáforos.
"""


def create_n_threads(n: int):
    for i in range(n):
        t = threading.Thread(target=print('Hello'))
        t.start()
        sleep(random.randint(1, 5))
        t.join()


if __name__ == "__main__":
    n = random.randint(1, 10)
    create_n_threads(n)

    print(f'Number of Threads: {n}')
