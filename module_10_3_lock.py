import threading
from random import randint
from time import sleep

N_=100

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        count = 0
        self.lock.acquire()
        while count < N_:
            k = randint(50,500)
            self.balance += k
            sleep(0.001)
            print(f'Пополнение: {k}. Баланс: {self.balance}')
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            count +=1

    def take(self):
        count = 0
        while count < N_:
            k = randint(50,500)
            print(f'Запрос на {k}')
            if self.balance >= k:
                self.balance -=k
                print(f'Снятие: {k}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            count +=1

bank_ = Bank()

th_dep = threading.Thread(target=Bank.deposit,args=(bank_,))
th_take = threading.Thread(target=Bank.take,args=(bank_,))

th_dep.start()
th_take.start()
th_dep.join()
th_take.join()

print(f'Итоговый баланс: {bank_.balance}')
