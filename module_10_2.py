import threading
import time

class Knight (threading.Thread):
    def __init__(self, name, power, enemies = 100, days = 0):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days = days

    def run(self):
        print(f'{self.name}, на нас напали!"')
        while self.enemies:
            self.enemies -= self.power
            self.days += 1
            print(f'{self.name} сражается {self.days}..., осталось {self.enemies} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')