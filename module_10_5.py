from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line.strip())
            if not line:
                break
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]
start_time = time.time()
for filename in filenames:
    read_info(filename)
end_time = time.time()
print(f'{end_time-start_time} (линейный)')

if __name__ == '__main__':
    start_time = time.time()
    with Pool() as pool:
        result = pool.map(read_info, filenames)
    #process = multiprocessing.Process(target=read_info, args=filenames )
    end_time = time.time()
    print(f'{end_time - start_time} (многопроцессный)')