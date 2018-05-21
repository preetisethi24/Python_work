import psutil
for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    if proc.info['name']=='Python':
        try:
            mem=proc.memory_info()[0]/float(2**20)
        except psutil.AccessDenied:
            pass
        else:
            print("For Process {} with pid {}:".format(proc.info['name'],proc.info['pid']))
            print("rss memory is {}:".format(mem))
