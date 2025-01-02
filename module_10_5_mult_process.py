from multiprocessing import Pool
import datetime

def read_info(name):
    with open(name,'r') as file:
        data = file.readlines()

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# ------------- файлы по очереди ------------
    t_start = datetime.datetime.now()
    all_data = map(read_info,filenames)
    rez1 = list(all_data)
    t_end = datetime.datetime.now()
    print(t_end-t_start)

# -------------- мультипроцесс --------------
    t_start = datetime.datetime.now()
    with Pool(len(filenames)) as pool:
        rez2 =list(pool.map(read_info,filenames))
    t_end = datetime.datetime.now()
    print(t_end-t_start)
