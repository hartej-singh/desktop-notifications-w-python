import psutil, datetime, time, schedule, openpyxl, os
from plyer import notification

#print(os.getcwd())
pid = int(input("Enter process ID: "))

cpuusage = psutil.cpu_percent(interval=1)
memusage = psutil.virtual_memory().percent

def warning():
    cpuusage = psutil.cpu_percent(interval=1)
    if cpuusage > 50:
        print("CPU Usage is above 50%", cpuusage)
    
    memusage = psutil.virtual_memory().percent
    if memusage > 50:
        print("Memory Usage is above 50%", memusage)

def monitor():
    time = datetime.datetime.now().strftime("%Y%m%d - %H:%M:%S")
    p = psutil.Process(pid)
    cpu = p.cpu_percent(interval=1) / psutil.cpu_count()

    memory_mb = p.memory_full_info().rss / (1024*1024)
    memory = p.memory_percent()

    path = "Monitor_result.xlsx"
    file = openpyxl.load_workbook(path)
    sheet = file.active

    sheet.cell(column=1, row=sheet.max_row+1, value=time)
    sheet.cell(column=2, row=sheet.max_row, value=pid)
    sheet.cell(column=3, row=sheet.max_row, value=cpu)
    sheet.cell(column=4, row=sheet.max_row, value=memory_mb)
    sheet.cell(column=5, row=sheet.max_row, value=memory)
    file.save(path)

schedule.every(1).second.do(warning)
schedule.every(5).seconds.do(monitor)

while True:
    if (cpuusage > 90):
        notification.notify(
        title="CPU Usage",
        message="CPU Usage is "+ str(cpuusage),
        timeout=10
    )
    if (memusage > 90):
        notification.notify(
        title="Memory Usage",
        message="Memory Usage is " + str(memusage),
        timeout=10
    )
    schedule.run_pending()
    time.sleep(1)
