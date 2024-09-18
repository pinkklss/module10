from threading import Thread, Lock
from time import sleep


s_print_lock = Lock()


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!', flush=True)
        enemies = 100
        counter_days = 0
        while enemies > 0:
            enemies -= min(self.power, enemies)
            counter_days += 1
            sleep(1)
            with s_print_lock:
                print(f'{self.name} сражается {counter_days} день(дня)...,  осталось {enemies} воинов.',
                      flush=True)
        with s_print_lock:
            print(f'{self.name} одержал победу спустя {counter_days} дней(дня)!', flush=True)


knight1 = Knight("Sir Lancelot", 5)
knight2 = Knight("Sir Galahad", 7)


thread1 = Thread(target=knight1.run)
thread2 = Thread(target=knight2.run)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
