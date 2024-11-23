import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))


class Cafe:
    def __init__(self, queue, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table_free = next((table for table in self.tables if table.guest is None), None)
            if table_free:
                table_free.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {table_free.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def  discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()