from threading import Thread
import time


class Knight(Thread):
    enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while Knight.enemies > 0:
            time.sleep(1)
            self.days += 1
            Knight.enemies -= self.power
            if Knight.enemies < 0:
                Knight.enemies = 0
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {Knight.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")


knight1 = Knight("Sir Lancelot", 5)
knight2 = Knight("Sir Galahad", 7)


thread1 = Thread(target=knight1.run)
thread2 = Thread(target=knight2.run)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
