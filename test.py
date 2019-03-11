from epics import caget
from time import sleep

while(1):
    w = caget('C3:EXP-modbusDocker')
    print(w)
    sleep(0.1)

print('We go to the end')
