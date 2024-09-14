from datetime import datetime
start_time = datetime.strptime("2:13:57","%H:%M:%S")
print(start_time)
end_time = datetime.strptime("11:47:57","%H:%M:%S")
print(end_time)
get_diff = start_time - end_time
print(get_diff)
print(get_diff.total_seconds())