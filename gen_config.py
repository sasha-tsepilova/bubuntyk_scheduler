

if __name__ == '__main__':
    tasks_descr = '''task_1 1400 14
task_2 1300 13
task_3 1100 11
task_4 1300 13
task_5 1200 12
task_6 1300 13
task_7 700 7
task_8 500 5
task_9 1800 18
task_10 2100 21'''
    memory_descr = '''add_new_resource MEM Mem 0 1 1 none
None 0 0'''
    cores = [4,12,16,24,64,96]
    freqs = [5200,4200,3700,3200,2800,2400]
    descr = [f'# 4x CPU: 4 {core}, {freq} 5200 MHz' for core, freq in zip(cores, freqs)]

    with open('cluster.txt', 'w') as f:
        for i in range(1, 7):
            f.write(f'{descr[i - 1]}\n')
            for j in range(1, 5):
                f.write(f'add_new_resource CPU CPU_{i}_{j} {i}{j} {freqs[i-1]} 10 performance\n'
                        f'{tasks_descr}\n')
            f.write('\n')
        f.write(f'{memory_descr}\n\n\n')

        for i1 in range(1, 7):
            for j1 in range(1, 5):
                for i2 in range(i1, 7):
                    for j2 in range(j1, 5):
                        res = 100
                        if i1 == i2:
                            if j1 == j2:
                                res = 1
                            else:
                                res = 10
                        f.write(f'comm_band {i1}{j1} {i2}{j2} {res}\n')
                f.write('\n')


