import threading
from time import sleep,time

def wite_words(word_count,file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for n in range(1,word_count+1):
            file.write('Какое-то слово №'+ str(n) + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = time()
wite_words(10,'example_01.txt')
wite_words(30,'example_02.txt')
wite_words(200,'example_03.txt')
wite_words(100,'example_04.txt')
time_end = time()
print(f'Время работы потоков  {round(time_end - time_start, 5)} секунд')

time_start = time()
stream_01 = threading.Thread(target=wite_words,args=(10,'example_05.txt'))
stream_02 = threading.Thread(target=wite_words,args=(30,'example_06.txt'))
stream_03 = threading.Thread(target=wite_words,args=(200,'example_07.txt'))
stream_04 = threading.Thread(target=wite_words,args=(100,'example_08.txt'))

stream_01.start()
stream_02.start()
stream_03.start()
stream_04.start()

stream_01.join()
stream_02.join()
stream_03.join()
stream_04.join()

time_end = time()
print(f'Время работы потоков  {round(time_end - time_start, 5)} секунд')
