from threading import Thread
import time

enemies = 100


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        global enemies
        while enemies > 0:
            time.sleep(1)
            self.days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")


knight1 = Knight("Sir Lancelot", 5)
knight2 = Knight("Sir Galahad", 7)


thread1 = Thread(target=knight1.run)
thread2 = Thread(target=knight2.run)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
