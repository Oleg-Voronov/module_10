from queue import Queue
from random import randint
from time import sleep
import threading

N_ = 6 # количество столов +1

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        sleep(randint(3,10))

class Cafe:
    def __init__(self,*tables):
        self.tables = tables
        self.que = Queue()

    def tables_empty(self):
        rez = True
        for t in self.tables:
            if t.guest != None:
                rez = False
                break
        return rez

    def guest_arrival(self,*guests):
        def copy_(a,b):
            for i in range(a,b):
                self.tables[i].guest = guests[i]
                print(f'{self.tables[i].guest.name} сел(-а) за стол номер {self.tables[i].number}')
                self.tables[i].guest.start()
        k=len(guests)
        l=len(self.tables)
        if k>l:
            copy_(0,l)
            for i in range(l,k):
                self.que.put(guests[i])
                print(f'{guests[i].name} в очереди')
        else:
            copy_(0,k)

    def discuss_guests(self):
        while not self.que.empty() or not self.tables_empty():
            for t in self.tables:
                if t.guest != None and not t.guest.is_alive():
                    print(f'{t.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {t.number} свободен.')
                    t.guest = None
                    if not self.que.empty():
                        t.guest = self.que.get()
                        t.guest.start()
                        print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')

tables = [Table(number) for number in range(1, N_)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe_ = Cafe(*tables)
cafe_.guest_arrival(*guests)
cafe_.discuss_guests()
