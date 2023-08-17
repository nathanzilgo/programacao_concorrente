import threading
import random
from time import sleep

"""
Crie um programa que recebe um número inteiro n como argumento e cria n threads.
Cada uma dessas threads deve dormir por um tempo aleatório de no máximo 5 segundos.
Depois que acordar, cada thread deve sortear um outro número aleatório s (entre 0
e 10). Somente depois de todas as n threads terminarem suas escolhas (ou seja, ao
fim da primeira fase), começamos a segunda fase. Nesta segunda fase, a n-ésima
thread criada deve dormir pelo tempo s escolhido pela thread n - 1 (faça a contagem
de maneira modular, ou seja, a primeira thread dorme conforme o número sorteado
pela última). Use semáforos.
"""


def create_n_threads(n: int):
    for i in range(n):
        t = threading.Thread(target=print("Hello"))
        t.start()
        sleep(random.randint(1, 5))
        s = random.randint(0, 10)
        t.join()


if __name__ == "__main__":
    n = random.randint(1, 10)
    create_n_threads(n)

    print(f"Number of Threads: {n}")
