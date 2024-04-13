from datetime import datetime

# 文件路径，替换为你的实际文件路径
file_path = 'time_records.txt'

# 从文件中读取时间记录
with open(file_path, 'r') as file:
    times = file.readlines()
    times = [time.strip() for time in times]  # 移除每行的空白字符

# 将字符串格式的时间转换为 datetime 对象，并排序
times = [datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in times]
times.sort()

# 计算相邻时间对的差值（秒）
total_seconds = 0
for i in range(1, len(times), 2):
    total_seconds += (times[i] - times[i-1]).total_seconds()

print("总工作时长（秒）:", total_seconds)
