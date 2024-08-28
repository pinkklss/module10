from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            x = randint(50,500)
            self.balance += x

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'\nПополнение:{x}. Баланс:{self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            x = randint(50, 500)

            print(f'\nЗапрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'\nСнятие: {x}. Баланс: {self.balance}')
            else:
                print('\nЗапрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
