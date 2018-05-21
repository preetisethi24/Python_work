#import psutil
#print(psutil.virtual_memory())


    # return the memory usage in MB
def memory_usage_psutil():
    import psutil
    import os
    for pid in psutil.pids():
        print" PID is :{}".format(pid)
        process = psutil.Process(pid)
        #mem = process.memory_info()[0] / float(2 ** 20)
        mem = process.memory_info()
    return mem

print(memory_usage_psutil())
