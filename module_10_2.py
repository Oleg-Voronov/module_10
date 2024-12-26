import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self,name,power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
    def run(self):
        enemy = 100
        days_count = 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            days_count +=1
            enemy = enemy - self.power
            if enemy < 0: enemy = 0
            print(f'{self.name} сражается {days_count} дней(день)>..., осталось {enemy} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
