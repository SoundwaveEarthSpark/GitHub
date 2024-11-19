from time import sleep
import random
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            funds = random.randint(50, 500)
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            with self.lock:
                self.balance += funds
                print(f'Пополнение: {funds}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            cut = random.randint(50, 500)
            print(f"Запрос на {cut}")
            with self.lock:
                if cut > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()
                else:
                    self.balance -= cut
                    print(f"Снятие: {cut}. Баланс: {self.balance}")


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')