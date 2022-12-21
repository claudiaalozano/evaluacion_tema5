import datetime
import time
import os

while True:
    hora_actual = datetime.datetime.now()
    print(hora_actual.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")