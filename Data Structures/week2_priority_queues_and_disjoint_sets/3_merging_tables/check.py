from multiprocessing import Process, cpu_count
core_count = cpu_count()
for i in range(0, len(final_res), core_count):
    process = []
    process.append(Process(target=trans, args=(final_result[i * core_count : (i + 1) * core_count])))

for p in process:
    p.start()
for p in process:
    p.join()


