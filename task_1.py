time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = []
summary = 0

for i in time_str.split(','):
    time_list.extend(i.split())

for v in time_list:
    if v.endswith('h'):
        number = int(v[:-1])
        summary += 60*number
    if v.endswith('m'):
        number = int(v[:-1])
        summary += number
    if v.endswith('s'):
        number = int(v[:-1])
        summary += number/60    

print('Общее количество минут: ', int(summary))